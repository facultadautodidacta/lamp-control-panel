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

# Crear directorios
echo -e "${YELLOW}📁 Creando directorios...${NC}"
mkdir -p /opt/lamp-control-panel
mkdir -p /usr/share/applications
mkdir -p /usr/share/icons/hicolor/256x256/apps

# Copiar archivos del programa
echo "� Copiando archivos..."
cp panel_control.py /opt/lamp-control-panel/
cp config.py /opt/lamp-control-panel/
cp servicios.py /opt/lamp-control-panel/
cp componentes.py /opt/lamp-control-panel/
cp logo.png /opt/lamp-control-panel/

# Copiar icono al sistema
echo "🎨 Instalando icono del sistema..."
mkdir -p /usr/share/pixmaps
cp logo.png /usr/share/pixmaps/lamp-control-panel.png
if [ -f lamp-icon.ico ]; then
    cp lamp-icon.ico /usr/share/pixmaps/lamp-control-panel.ico
fi

# Hacer ejecutable

# Copiar logo al directorio de iconos del sistema
cp logo.png /usr/share/icons/hicolor/256x256/apps/lamp-control-panel.png

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
