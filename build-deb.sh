#!/bin/bash
#
# Script para construir el paquete .deb
# Ejecuta: ./build-deb.sh
#

set -e

# Obtener directorio del script
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
cd "$SCRIPT_DIR"

echo "🔧 Construyendo paquete .deb para Panel de Control LAMP..."

# Limpiar construcción anterior (solo directorios de instalación, no DEBIAN)
rm -rf debian-package/opt
rm -rf debian-package/usr
rm -f lamp-control-panel_*.deb

# Crear estructura de directorios
mkdir -p debian-package/opt/lamp-control-panel
mkdir -p debian-package/usr/local/bin
mkdir -p debian-package/usr/share/applications
mkdir -p debian-package/usr/share/icons/hicolor/256x256/apps

# Copiar archivos del programa
cp panel_control.py debian-package/opt/lamp-control-panel/
cp config.py debian-package/opt/lamp-control-panel/
cp servicios.py debian-package/opt/lamp-control-panel/
cp componentes.py debian-package/opt/lamp-control-panel/
cp logo.png debian-package/opt/lamp-control-panel/

# Hacer ejecutable
chmod +x debian-package/opt/lamp-control-panel/panel_control.py

# Crear archivo .desktop
cat > debian-package/usr/share/applications/lamp-control-panel.desktop << 'EOF'
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
EOF

# Copiar icono
cp logo.png debian-package/usr/share/icons/hicolor/256x256/apps/lamp-control-panel.png

# Crear enlace simbólico en el directorio correcto
( cd debian-package/usr/local/bin && ln -sf /opt/lamp-control-panel/panel_control.py lamp-panel )

# Construir paquete (desde el directorio raíz del script)
dpkg-deb --build debian-package lamp-control-panel_1.0.0_all.deb

echo ""
echo "✅ Paquete creado: lamp-control-panel_1.0.0_all.deb"
echo ""
echo "📦 Para instalar:"
echo "   sudo dpkg -i lamp-control-panel_1.0.0_all.deb"
echo "   sudo apt-get install -f  # Si faltan dependencias"
echo ""
