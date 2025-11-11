# Contribuyendo a Panel de Control LAMP

¡Gracias por tu interés en contribuir! 🎉

## 🤝 Cómo Contribuir

### 1. Fork y Clone
```bash
git clone https://github.com/TU_USUARIO/lamp-control-panel.git
cd lamp-control-panel
```

### 2. Crea una Rama
```bash
git checkout -b feature/nueva-funcionalidad
# o
git checkout -b fix/correccion-bug
```

### 3. Haz tus Cambios
- Escribe código limpio y documentado
- Sigue el estilo de código existente
- Agrega comentarios donde sea necesario
- Prueba tus cambios

### 4. Commit y Push
```bash
git add .
git commit -m "feat: descripción de tu cambio"
git push origin feature/nueva-funcionalidad
```

### 5. Pull Request
- Ve a GitHub y crea un Pull Request
- Describe los cambios realizados
- Referencia issues relacionados

## 📋 Estilo de Código

### Python
- PEP 8 para estilo de código
- Docstrings para funciones y clases
- Type hints cuando sea posible
- Nombres descriptivos en español

### Commits
Usamos [Conventional Commits](https://www.conventionalcommits.org/):

- `feat:` Nueva funcionalidad
- `fix:` Corrección de bug
- `docs:` Cambios en documentación
- `style:` Formato, espacios, etc
- `refactor:` Refactorización de código
- `test:` Agregar o modificar tests
- `chore:` Tareas de mantenimiento

## 🐛 Reportar Bugs

Usa GitHub Issues e incluye:
- Descripción clara del problema
- Pasos para reproducir
- Comportamiento esperado vs actual
- Screenshots si aplica
- Sistema operativo y versión
- Logs de error

## 💡 Sugerir Funcionalidades

¿Tienes una idea? ¡Genial!
1. Abre un Issue con etiqueta `enhancement`
2. Describe la funcionalidad
3. Explica el caso de uso
4. Si es posible, propón una implementación

## 🧪 Testing

Antes de enviar tu PR:
```bash
# Prueba tu código
python3 panel_control.py

# Verifica que funcione con sudo
sudo python3 panel_control.py
```

## 📝 Áreas donde Puedes Ayudar

- 🌐 Agregar soporte para más servicios (PHP-FPM, PostgreSQL, etc.)
- 🎨 Mejorar el diseño de la interfaz
- 🐧 Soporte para otras distribuciones (Arch, Fedora, etc.)
- 🌍 Traducciones a otros idiomas
- 📚 Mejorar la documentación
- 🧪 Agregar tests automatizados
- 🔧 Optimizaciones de rendimiento

## ✅ Code Review

Todos los PR serán revisados:
- Código limpio y legible
- Funcionalidad probada
- Sin errores obvios
- Documentación actualizada

## 📜 Licencia

Al contribuir, aceptas que tu código será licenciado bajo MIT License.

## 🙏 Agradecimientos

¡Gracias por hacer este proyecto mejor!

---

Desarrollado con ❤️ por RAS y la comunidad
