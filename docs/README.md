# 🖥️ Panel de Control LAMP

<div align="center">

![License](https://img.shields.io/badge/license-MIT-blue.svg)
![Python](https://img.shields.io/badge/python-3.x-green.svg)
![Platform](https://img.shields.io/badge/platform-Debian%20|%20Ubuntu-orange.svg)

**Panel de control gráfico profesional para gestionar servicios LAMP en sistemas basados en Debian**

[Características](#-características) •
[Instalación](#-instalación) •
[Uso](#-uso) •
[Contribuir](#-contribuir) •
[Licencia](#-licencia)

</div>

---

## 📋 Características

- ✅ **Interfaz gráfica moderna** con diseño por pestañas
- ⚙️ **Control completo de servicios**
  - Apache Web Server (iniciar, detener, reiniciar)
  - MySQL/MariaDB Database (iniciar, detener, reiniciar)
- 🚦 **Indicadores de estado en tiempo real**
- 📋 **Visor de logs de error**
  - Logs tradicionales de archivos
  - Logs desde systemd journal
  - Búsqueda inteligente de logs
- 🔐 **Autenticación con contraseña única** (se pide solo una vez por sesión)
- 🎨 **Tema oscuro elegante** (Catppuccin inspired)
- 🏗️ **Arquitectura modular** y fácil de mantener
- 🐧 **Compatible con todos los derivados de Debian**
  - Ubuntu
  - Linux Mint
  - Pop!_OS
  - Debian
  - Y más...

## 🖼️ Capturas

### Autenticación Segura
![Solicitud de contraseña](screenshots/01-autenticacion.png)

### Panel de Control de Servicios
![Control de Apache y MySQL](screenshots/02-panel-servicios.png)

### Visor de Logs Integrado
![Logs de errores](screenshots/03-visor-logs.png)

## 📦 Instalación

### Opción 1: Script de Instalación (Recomendado)

```bash
# Clonar el repositorio
git clone https://github.com/TU_USUARIO/lamp-control-panel.git
cd lamp-control-panel

# Ejecutar instalador
sudo ./install.sh
```

### Opción 2: Paquete .deb

```bash
# Construir el paquete
./build-deb.sh

# Instalar
sudo dpkg -i lamp-control-panel_1.0.0_all.deb
sudo apt-get install -f  # Si faltan dependencias
```

### Opción 3: Instalación Manual

```bash
# Instalar dependencias
sudo apt-get update
sudo apt-get install python3 python3-tk python3-pil python3-pil.imagetk

# Ejecutar directamente
python3 panel_control.py
```

## 🚀 Uso

### Desde el Menú de Aplicaciones
Busca **"Panel de Control LAMP"** en el menú de aplicaciones de tu sistema

### Desde Terminal
```bash
lamp-panel
```

### Ejecución Directa
```bash
python3 /opt/lamp-control-panel/panel_control.py
```

## 🔧 Requisitos del Sistema

- **Sistema Operativo:** Debian, Ubuntu o derivados
- **Python:** 3.x
- **Servicios:** systemd
- **Privilegios:** sudo/root para controlar servicios

### Dependencias

```
python3
python3-tk
python3-pil
python3-pil.imagetk
systemd
policykit-1
```

## 📁 Estructura del Proyecto

```
panelControl/
├── panel_control.py       # Aplicación principal
├── config.py             # Configuración (colores, fuentes, rutas)
├── servicios.py          # Gestor de servicios del sistema
├── componentes.py        # Componentes visuales reutilizables
├── logo.png             # Logo de la aplicación
├── install.sh           # Script de instalación
├── uninstall.sh         # Script de desinstalación
├── build-deb.sh         # Constructor de paquete .deb
├── debian-package/      # Estructura para paquete Debian
│   └── DEBIAN/
│       ├── control      # Metadatos del paquete
│       ├── postinst     # Script post-instalación
│       └── postrm       # Script post-eliminación
├── README.md            # Este archivo
├── LICENSE              # Licencia MIT
└── CONTRIBUTING.md      # Guía de contribución
```

## 🗑️ Desinstalación

### Si instalaste con script:
```bash
sudo ./uninstall.sh
```

### Si instalaste con .deb:
```bash
sudo apt-get remove lamp-control-panel
```

## 🤝 Contribuir

¡Las contribuciones son bienvenidas! Por favor lee [CONTRIBUTING.md](CONTRIBUTING.md) para detalles sobre nuestro código de conducta y el proceso para enviar pull requests.

### Áreas donde puedes ayudar:
- 🌐 Soporte para más servicios (PHP-FPM, PostgreSQL, Nginx, etc.)
- 🎨 Mejoras en la interfaz
- 🐧 Soporte para otras distros (Arch, Fedora, etc.)
- 🌍 Traducciones
- 📚 Documentación
- 🧪 Tests automatizados

## 🐛 Reportar Issues

Encontraste un bug? [Abre un issue](https://github.com/TU_USUARIO/lamp-control-panel/issues)

## 📝 Changelog

### v1.0.0 (2025-11-11)
- ✨ Release inicial
- ⚙️ Control de Apache y MySQL/MariaDB
- 📋 Visor de logs con múltiples fuentes
- 🎨 Interfaz con pestañas
- 🔐 Sistema de autenticación mejorado

## 📄 Licencia

Este proyecto está licenciado bajo la Licencia MIT - ver el archivo [LICENSE](LICENSE) para más detalles.

## 👨‍� Autor

**RAS (Roldan Aquino)**

## 🙏 Agradecimientos

- Inspirado en la necesidad de una herramienta simple para gestionar LAMP
- Diseño de colores basado en Catppuccin
- Comunidad de código abierto por las herramientas y librerías

---

<div align="center">

**Desarrollado con ❤️ por RAS**

Si este proyecto te ayuda, ¡dale una ⭐ en GitHub!

</div>
