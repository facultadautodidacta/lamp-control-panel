#!/bin/bash
#
# Script de desinstalación para Panel de Control LAMP
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
echo "║  Panel de Control LAMP - Desinstalador  ║"
echo "║           Desarrollado por RAS           ║"
echo "╚══════════════════════════════════════════╝"
echo -e "${NC}"

# Verificar si se ejecuta como root
if [ "$EUID" -ne 0 ]; then 
    echo -e "${RED}❌ Este script debe ejecutarse como root (usa sudo)${NC}"
    exit 1
fi

echo -e "${YELLOW}🗑️  Desinstalando Panel de Control LAMP...${NC}"

# Eliminar enlace simbólico
if [ -L "/usr/local/bin/lamp-panel" ]; then
    rm /usr/local/bin/lamp-panel
    echo -e "${GREEN}✓ Enlace simbólico eliminado${NC}"
fi

# Eliminar archivos del programa
if [ -d "/opt/lamp-control-panel" ]; then
    rm -rf /opt/lamp-control-panel
    echo -e "${GREEN}✓ Archivos del programa eliminados${NC}"
fi

# Eliminar archivo .desktop
if [ -f "/usr/share/applications/lamp-control-panel.desktop" ]; then
    rm /usr/share/applications/lamp-control-panel.desktop
    echo -e "${GREEN}✓ Entrada del menú eliminada${NC}"
fi

# Eliminar icono
if [ -f "/usr/share/icons/hicolor/256x256/apps/lamp-control-panel.png" ]; then
    rm /usr/share/icons/hicolor/256x256/apps/lamp-control-panel.png
    echo -e "${GREEN}✓ Icono eliminado${NC}"
fi

# Actualizar caché
echo -e "${YELLOW}🔄 Actualizando caché del sistema...${NC}"
gtk-update-icon-cache /usr/share/icons/hicolor/ 2>/dev/null || true
update-desktop-database /usr/share/applications/ 2>/dev/null || true

echo ""
echo -e "${GREEN}╔══════════════════════════════════════════╗${NC}"
echo -e "${GREEN}║  ✅ Desinstalación completada con éxito  ║${NC}"
echo -e "${GREEN}╚══════════════════════════════════════════╝${NC}"
echo ""
echo -e "${BLUE}📝 Nota: Las dependencias de Python no fueron eliminadas${NC}"
echo -e "   Si deseas eliminarlas también, ejecuta:${NC}"
echo -e "   ${YELLOW}sudo apt-get remove python3-tk python3-pil python3-pil.imagetk${NC}"
echo ""
