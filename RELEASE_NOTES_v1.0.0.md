# 🎉 Panel de Control LAMP v1.0.0

**Primera versión oficial** - Herramienta gráfica para gestionar Apache y MySQL/MariaDB en Debian/Ubuntu.

---

## ✨ Características

- ⚙️ **Control de Apache** - Iniciar, detener y reiniciar el servidor web
- 🔵 **Control de MySQL/MariaDB** - Gestión completa de la base de datos
- 🚦 **Indicadores en tiempo real** - Ve el estado actual de cada servicio
- 📋 **Visor de logs** - Consulta errores de Apache y MySQL fácilmente
- 📊 **Soporte journalctl** - Lee logs del sistema con un click
- 🎨 **Tema oscuro moderno** - Interfaz elegante y profesional
- 🔐 **Autenticación única** - Solo pide contraseña una vez
- 📑 **Interfaz con pestañas** - Servicios y logs organizados

---

## 📦 Instalación

### Método 1: Paquete .deb
```bash
wget https://github.com/facultadautodidacta/lamp-control-panel/releases/download/v1.0.0/lamp-control-panel_1.0.0_all.deb
sudo dpkg -i lamp-control-panel_1.0.0_all.deb
sudo apt-get install -f
```

### Método 2: Script de instalación
```bash
git clone https://github.com/facultadautodidacta/lamp-control-panel.git
cd lamp-control-panel/scripts
sudo ./install.sh
```

### Método 3: Ejecutar desde código
```bash
git clone https://github.com/facultadautodidacta/lamp-control-panel.git
cd lamp-control-panel
sudo apt-get install python3-tk python3-pil python3-pil.imagetk
python3 src/panel_control.py
```

---

## 🚀 Uso

Después de instalar:

```bash
# Desde terminal
lamp-panel

# O busca "Panel de Control LAMP" en el menú de aplicaciones
```

---

## 🔧 Requisitos

- **Sistema**: Debian, Ubuntu, Linux Mint, Pop!_OS o similares
- **Python**: 3.x
- **Servicios**: Apache2 y MySQL/MariaDB instalados
- **Otros**: systemd, policykit-1

---

## 📸 Capturas

### 🔐 Autenticación
![Solicitud de contraseña](https://raw.githubusercontent.com/facultadautodidacta/lamp-control-panel/main/docs/screenshots/01-autenticacion.png)

*Solicita contraseña una sola vez al iniciar*

### ⚙️ Panel de Control
![Control de servicios](https://raw.githubusercontent.com/facultadautodidacta/lamp-control-panel/main/docs/screenshots/02-panel-servicios.png)

*Gestiona Apache y MySQL con indicadores de estado en tiempo real*

### 📋 Visor de Logs
![Logs de error](https://raw.githubusercontent.com/facultadautodidacta/lamp-control-panel/main/docs/screenshots/03-visor-logs.png)

*Consulta logs de Apache, MySQL y journalctl sin salir de la aplicación*

---

## 🐛 Nota Importante

El icono en la barra de tareas puede aparecer genérico cuando se ejecuta desde terminal. Esto es una limitación de Tkinter en Linux. Al lanzar desde el menú de aplicaciones funciona correctamente.

---

## 🚀 Próximas Mejoras

En futuras versiones:
- Soporte para PHP-FPM y Nginx
- Multi-idioma (español/inglés)
- Gráficos de rendimiento
- Backups de bases de datos

---

## 📁 Archivos

- **lamp-control-panel_1.0.0_all.deb** (12 KB)

**SHA256:**
```
6c386c6634bc02e2683fe93bab8642362f9c55ce947457c1899f962080e1f124
```

---

## 🤝 Contribuir

¿Encontraste un bug o tienes una idea?

- [Reportar problema](https://github.com/facultadautodidacta/lamp-control-panel/issues)
- [Ver código fuente](https://github.com/facultadautodidacta/lamp-control-panel)
- [Guía de contribución](https://github.com/facultadautodidacta/lamp-control-panel/blob/main/docs/CONTRIBUTING.md)

---

## 📄 Licencia

MIT License - Uso libre para cualquier propósito.

---

<div align="center">

**Desarrollado por RAS**

⭐ Si te gusta el proyecto, deja una estrella en GitHub

[Documentación](https://github.com/facultadautodidacta/lamp-control-panel/blob/main/docs/README.md) • [Repositorio](https://github.com/facultadautodidacta/lamp-control-panel)

</div>
