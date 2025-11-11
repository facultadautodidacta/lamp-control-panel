#!/bin/bash
#
# Script para construir el paquete .deb
# Ejecuta: cd scripts && ./build-deb.sh
#

set -e

# Obtener directorio del proyecto (un nivel arriba del script)
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
PROJECT_ROOT="$( cd "$SCRIPT_DIR/.." && pwd )"
cd "$PROJECT_ROOT"

echo "🔧 Construyendo paquete .deb para Panel de Control LAMP..."

# Limpiar construcción anterior
rm -rf packaging/debian/opt
rm -rf packaging/debian/usr
rm -f lamp-control-panel_*.deb

# Crear estructura de directorios
mkdir -p packaging/debian/opt/lamp-control-panel
mkdir -p packaging/debian/usr/local/bin
mkdir -p packaging/debian/usr/share/applications
mkdir -p packaging/debian/usr/share/icons/hicolor/256x256/apps

# Copiar archivos del programa
cp src/panel_control.py packaging/debian/opt/lamp-control-panel/
cp src/config.py packaging/debian/opt/lamp-control-panel/
cp src/servicios.py packaging/debian/opt/lamp-control-panel/
cp src/componentes.py packaging/debian/opt/lamp-control-panel/
cp assets/logo.png packaging/debian/opt/lamp-control-panel/

# Hacer ejecutable
chmod +x packaging/debian/opt/lamp-control-panel/panel_control.py

# Crear archivo .desktop
cat > packaging/debian/usr/share/applications/lamp-control-panel.desktop << 'EOF'
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

# Copiar icono
cp assets/logo.png packaging/debian/usr/share/icons/hicolor/256x256/apps/lamp-control-panel.png

# Crear enlace simbólico en el directorio correcto
( cd packaging/debian/usr/local/bin && ln -sf /opt/lamp-control-panel/panel_control.py lamp-panel )

# Construir paquete (desde el directorio raíz del script)
dpkg-deb --build packaging/debian lamp-control-panel_1.0.0_all.deb

echo ""
echo "✅ Paquete creado: lamp-control-panel_1.0.0_all.deb"
echo ""
echo "📦 Para instalar:"
echo "   sudo dpkg -i lamp-control-panel_1.0.0_all.deb"
echo "   sudo apt-get install -f  # Si faltan dependencias"
echo ""
