#!/bin/bash
#
# Script de instalación para Panel de Control LAMP
# Desarrollado por RAS - 2025
#

set -e

# Colores para output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # Sin color

echo -e "${BLUE}"
echo "╔══════════════════════════════════════════╗"
echo "║   Panel de Control LAMP - Instalador    ║"
echo "║           Desarrollado por RAS           ║"
echo "╚══════════════════════════════════════════╝"
echo -e "${NC}"

# Verificar si se ejecuta como root
if [ "$EUID" -ne 0 ]; then 
    echo -e "${RED}❌ Este script debe ejecutarse como root (usa sudo)${NC}"
    exit 1
fi

echo -e "${YELLOW}📦 Instalando dependencias...${NC}"

# Actualizar repositorios
apt-get update -qq

# Instalar dependencias
apt-get install -y \
    python3 \
    python3-tk \
    python3-pil \
    python3-pil.imagetk \
    systemd \
    policycoreutils \
    > /dev/null 2>&1

echo -e "${GREEN}✓ Dependencias instaladas${NC}"

# Verificar si Apache y MySQL están instalados
echo -e "${YELLOW}🔍 Verificando servicios LAMP...${NC}"

APACHE_INSTALLED=false
MYSQL_INSTALLED=false

# Verificar Apache
if systemctl list-unit-files | grep -q "apache2.service"; then
    APACHE_INSTALLED=true
    echo -e "${GREEN}  ✓ Apache2 detectado${NC}"
else
    echo -e "${YELLOW}  ⚠ Apache2 no está instalado${NC}"
fi

# Verificar MySQL/MariaDB
if systemctl list-unit-files | grep -qE "(mysql|mariadb).service"; then
    MYSQL_INSTALLED=true
    echo -e "${GREEN}  ✓ MySQL/MariaDB detectado${NC}"
else
    echo -e "${YELLOW}  ⚠ MySQL/MariaDB no está instalado${NC}"
fi

# Advertencia si faltan servicios
if [ "$APACHE_INSTALLED" = false ] || [ "$MYSQL_INSTALLED" = false ]; then
    echo ""
    echo -e "${YELLOW}╔════════════════════════════════════════════════════╗${NC}"
    echo -e "${YELLOW}║            ⚠️  ADVERTENCIA IMPORTANTE               ║${NC}"
    echo -e "${YELLOW}╚════════════════════════════════════════════════════╝${NC}"
    echo ""
    echo -e "${YELLOW}El Panel de Control LAMP requiere que los servicios${NC}"
    echo -e "${YELLOW}estén instalados para funcionar correctamente.${NC}"
    echo ""
    
    if [ "$APACHE_INSTALLED" = false ]; then
        echo -e "${CYAN}Para instalar Apache:${NC}"
        echo -e "  sudo apt-get install apache2"
        echo ""
    fi
    
    if [ "$MYSQL_INSTALLED" = false ]; then
        echo -e "${CYAN}Para instalar MySQL:${NC}"
        echo -e "  sudo apt-get install mysql-server"
        echo -e "${CYAN}O MariaDB:${NC}"
        echo -e "  sudo apt-get install mariadb-server"
        echo ""
    fi
    
    echo -e "${YELLOW}¿Deseas continuar con la instalación de todas formas? [s/N]${NC}"
    read -r response
    
    if [[ ! "$response" =~ ^[Ss]$ ]]; then
        echo -e "${RED}❌ Instalación cancelada${NC}"
        echo -e "${CYAN}💡 Instala los servicios LAMP primero y vuelve a ejecutar este script${NC}"
        exit 0
    fi
    
    echo -e "${YELLOW}⚠️  Continuando con la instalación...${NC}"
    echo ""
fi

# Crear directorios
echo -e "${YELLOW}📁 Creando directorios...${NC}"
mkdir -p /opt/lamp-control-panel
mkdir -p /usr/share/applications
mkdir -p /usr/share/icons/hicolor/256x256/apps

# Copiar archivos del programa
echo "📁 Copiando archivos..."
cp ../src/panel_control.py /opt/lamp-control-panel/
cp ../src/config.py /opt/lamp-control-panel/
cp ../src/servicios.py /opt/lamp-control-panel/
cp ../src/componentes.py /opt/lamp-control-panel/
cp ../assets/logo.png /opt/lamp-control-panel/

# Copiar icono al sistema
echo "🎨 Instalando icono del sistema..."
mkdir -p /usr/share/pixmaps
cp ../assets/logo.png /usr/share/pixmaps/lamp-control-panel.png
if [ -f ../assets/lamp-icon.ico ]; then
    cp ../assets/lamp-icon.ico /usr/share/pixmaps/lamp-control-panel.ico
fi

# Hacer ejecutable

# Copiar logo al directorio de iconos del sistema
cp ../assets/logo.png /usr/share/icons/hicolor/256x256/apps/lamp-control-panel.png

# Hacer ejecutable el script principal
chmod +x /opt/lamp-control-panel/panel_control.py

# Crear enlace simbólico en /usr/local/bin
echo -e "${YELLOW}🔗 Creando enlace simbólico...${NC}"
ln -sf /opt/lamp-control-panel/panel_control.py /usr/local/bin/lamp-panel

# Crear archivo .desktop
echo -e "${YELLOW}🖥️  Creando entrada en el menú...${NC}"
cat > /usr/share/applications/lamp-control-panel.desktop << 'EOF'
[Desktop Entry]
Version=1.0
Type=Application
Name=Panel de Control LAMP
Comment=Gestiona servicios Apache, MySQL/MariaDB
Icon=lamp-control-panel
Exec=python3 /opt/lamp-control-panel/panel_control.py
Terminal=false
Categories=System;Settings;
Keywords=lamp;apache;mysql;mariadb;server;
StartupNotify=true
StartupWMClass=LAMP-Control-Panel
EOF

# Actualizar caché de iconos
echo -e "${YELLOW}🔄 Actualizando caché de iconos...${NC}"
gtk-update-icon-cache /usr/share/icons/hicolor/ 2>/dev/null || true
update-desktop-database /usr/share/applications/ 2>/dev/null || true

echo ""
echo -e "${GREEN}╔══════════════════════════════════════════╗${NC}"
echo -e "${GREEN}║     ✅ Instalación completada con éxito  ║${NC}"
echo -e "${GREEN}╚══════════════════════════════════════════╝${NC}"
echo ""
echo -e "${BLUE}📌 Cómo usar:${NC}"
echo -e "   1️⃣  Desde el menú de aplicaciones: busca 'Panel de Control LAMP'"
echo -e "   2️⃣  Desde terminal: ${GREEN}lamp-panel${NC}"
echo -e "   3️⃣  Directo: ${GREEN}python3 /opt/lamp-control-panel/panel_control.py${NC}"
echo ""
echo -e "${YELLOW}⚠️  Nota: Se te pedirá la contraseña de sudo al iniciar la aplicación${NC}"
echo ""
