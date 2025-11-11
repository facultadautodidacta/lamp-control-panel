"""
Componentes de la interfaz gráfica
Contiene clases para crear secciones de servicios y elementos visuales
"""

import tkinter as tk
from tkinter import ttk, scrolledtext
import subprocess
from config import TemaOscuro, ConfiguracionApp, RutasLogs


class SeccionServicio:
    """Clase base para crear una sección de control de servicio"""
    
    def __init__(self, parent, nombre_servicio, icono, tema, fila, callback_iniciar, 
                 callback_detener, callback_reiniciar):
        """
        Inicializa una sección de servicio
        
        Args:
            parent: Frame padre donde se creará la sección
            nombre_servicio: Nombre del servicio (para mostrar)
            icono: Emoji o icono para el servicio
            tema: Instancia de TemaOscuro
            fila: Número de fila donde se colocará la sección
            callback_iniciar: Función a llamar al iniciar
            callback_detener: Función a llamar al detener
            callback_reiniciar: Función a llamar al reiniciar
        """
        self.parent = parent
        self.nombre_servicio = nombre_servicio
        self.icono = icono
        self.tema = tema
        self.fila = fila
        self.callback_iniciar = callback_iniciar
        self.callback_detener = callback_detener
        self.callback_reiniciar = callback_reiniciar
        
        # Referencias a widgets para actualización
        self.status_indicator = None
        self.status_text = None
        
        self._crear_seccion()
    
    def _crear_seccion(self):
        """Crea todos los elementos de la sección"""
        # Card para el servicio
        card = ttk.Frame(self.parent, style='Card.TFrame', padding=15)
        card.grid(row=self.fila, column=0, columnspan=3, pady=(0, 20), sticky=(tk.W, tk.E))
        
        # Header con título y estado
        self._crear_header(card)
        
        # Botones de control
        self._crear_botones(card)
    
    def _crear_header(self, card):
        """Crea el encabezado con título e indicador de estado"""
        header = tk.Frame(card, bg=self.tema.CARD_BG)
        header.pack(fill=tk.X, pady=(0, 15))
        
        # Título del servicio
        titulo = ttk.Label(header, text=f"{self.icono} {self.nombre_servicio}", 
                          style='Header.TLabel')
        titulo.pack(side=tk.LEFT)
        
        # Indicador de estado
        self.status_indicator = tk.Label(header, text="●", 
                                        font=('Arial', 18),
                                        bg=self.tema.CARD_BG,
                                        fg="gray")
        self.status_indicator.pack(side=tk.RIGHT, padx=(10, 0))
        
        self.status_text = ttk.Label(header, text="Verificando...",
                                    style='Status.TLabel')
        self.status_text.pack(side=tk.RIGHT)
    
    def _crear_botones(self, card):
        """Crea los botones de control del servicio"""
        frame_botones = tk.Frame(card, bg=self.tema.CARD_BG)
        frame_botones.pack(pady=5)
        
        # Botón Iniciar
        btn_iniciar = tk.Button(
            frame_botones, text="▶ Iniciar",
            command=self.callback_iniciar,
            bg=self.tema.BTN_INICIAR_BG,
            fg=self.tema.BTN_TEXT_COLOR,
            font=ConfiguracionApp.FUENTE_BOTON,
            width=ConfiguracionApp.BOTON_ANCHO,
            height=ConfiguracionApp.BOTON_ALTO,
            border=0,
            activebackground=self.tema.BTN_INICIAR_ACTIVE,
            cursor="hand2"
        )
        btn_iniciar.grid(row=0, column=0, padx=8)
        
        # Botón Detener
        btn_detener = tk.Button(
            frame_botones, text="⏹ Detener",
            command=self.callback_detener,
            bg=self.tema.BTN_DETENER_BG,
            fg=self.tema.BTN_TEXT_COLOR,
            font=ConfiguracionApp.FUENTE_BOTON,
            width=ConfiguracionApp.BOTON_ANCHO,
            height=ConfiguracionApp.BOTON_ALTO,
            border=0,
            activebackground=self.tema.BTN_DETENER_ACTIVE,
            cursor="hand2"
        )
        btn_detener.grid(row=0, column=1, padx=8)
        
        # Botón Reiniciar
        btn_reiniciar = tk.Button(
            frame_botones, text="🔄 Reiniciar",
            command=self.callback_reiniciar,
            bg=self.tema.BTN_REINICIAR_BG,
            fg=self.tema.BTN_TEXT_COLOR,
            font=ConfiguracionApp.FUENTE_BOTON,
            width=ConfiguracionApp.BOTON_ANCHO,
            height=ConfiguracionApp.BOTON_ALTO,
            border=0,
            activebackground=self.tema.BTN_REINICIAR_ACTIVE,
            cursor="hand2"
        )
        btn_reiniciar.grid(row=0, column=2, padx=8)
    
    def actualizar_estado(self, activo):
        """
        Actualiza el indicador de estado del servicio
        
        Args:
            activo (bool): True si el servicio está activo, False si no
        """
        if activo:
            self.status_indicator.config(fg=self.tema.STATUS_ACTIVO)
            self.status_text.config(text="Activo")
        else:
            self.status_indicator.config(fg=self.tema.STATUS_INACTIVO)
            self.status_text.config(text="Inactivo")


class Footer:
    """Clase para crear el footer de la aplicación"""
    
    def __init__(self, parent, tema, logo_photo=None):
        """
        Inicializa el footer
        
        Args:
            parent: Frame padre donde se creará el footer
            tema: Instancia de TemaOscuro
            logo_photo: Imagen del logo (ImageTk.PhotoImage)
        """
        self.parent = parent
        self.tema = tema
        self.logo_photo = logo_photo
        
        self._crear_footer()
    
    def _crear_footer(self):
        """Crea el footer con separador, logo y créditos"""
        # Separador
        separator = tk.Frame(self.parent, height=1, bg=self.tema.SEPARATOR_COLOR)
        separator.grid(row=5, column=0, columnspan=3, sticky=(tk.W, tk.E), pady=(30, 20))
        
        # Frame del footer
        footer_frame = tk.Frame(self.parent, bg=self.tema.BG_COLOR)
        footer_frame.grid(row=6, column=0, columnspan=3, pady=(0, 10), sticky=tk.E)
        
        # Texto del footer
        footer_text = tk.Label(
            footer_frame,
            text="© 2025 | RAS",
            font=ConfiguracionApp.FUENTE_FOOTER,
            bg=self.tema.BG_COLOR,
            fg=self.tema.FOOTER_TEXT_COLOR
        )
        footer_text.pack(side=tk.RIGHT, padx=(0, 10))
        
        # Logo (si está disponible)
        if self.logo_photo:
            logo_label = tk.Label(footer_frame, image=self.logo_photo, bg=self.tema.BG_COLOR)
            logo_label.pack(side=tk.RIGHT)


class VisorLogs:
    """Clase para visualizar logs de error de los servicios"""
    
    def __init__(self, parent, tema, gestor_servicios):
        """
        Inicializa el visor de logs
        
        Args:
            parent: Frame padre donde se creará el visor
            tema: Instancia de TemaOscuro
            gestor_servicios: Instancia de GestorServicios para ejecutar comandos
        """
        self.parent = parent
        self.tema = tema
        self.gestor_servicios = gestor_servicios
        self.text_widget = None
        
        self._crear_visor()
    
    def _crear_visor(self):
        """Crea el visor de logs con tabs para diferentes servicios"""
        # Título
        titulo = tk.Label(
            self.parent,
            text="📋 Logs de Error de Servicios",
            font=('Arial', 14, 'bold'),
            bg=self.tema.BG_COLOR,
            fg=self.tema.FG_COLOR
        )
        titulo.pack(pady=(0, 15))
        
        # Crear notebook (tabs) para los diferentes logs
        self.notebook = ttk.Notebook(self.parent)
        self.notebook.pack(fill=tk.BOTH, expand=True)
        
        # Tab Apache
        self.tab_apache = self._crear_tab_log("Apache")
        self.notebook.add(self.tab_apache, text="Apache")
        
        # Tab MySQL/MariaDB
        self.tab_mysql = self._crear_tab_log("MySQL")
        self.notebook.add(self.tab_mysql, text="MySQL/MariaDB")
        
        # Botones de control
        botones_frame = tk.Frame(self.parent, bg=self.tema.BG_COLOR)
        botones_frame.pack(pady=(10, 0), fill=tk.X)
        
        btn_actualizar = tk.Button(
            botones_frame,
            text="🔄 Actualizar",
            command=self.actualizar_logs,
            bg=self.tema.BTN_REINICIAR_BG,
            fg=self.tema.BTN_TEXT_COLOR,
            font=('Arial', 9, 'bold'),
            border=0,
            cursor="hand2",
            padx=10,
            pady=5
        )
        btn_actualizar.pack(side=tk.LEFT, padx=(0, 5))
        
        btn_limpiar = tk.Button(
            botones_frame,
            text="🗑️ Limpiar",
            command=self.limpiar_logs,
            bg=self.tema.BTN_DETENER_BG,
            fg=self.tema.BTN_TEXT_COLOR,
            font=('Arial', 9, 'bold'),
            border=0,
            cursor="hand2",
            padx=10,
            pady=5
        )
        btn_limpiar.pack(side=tk.LEFT)
        
        btn_journal = tk.Button(
            botones_frame,
            text="📖 Ver Journal",
            command=self.ver_journal,
            bg="#f9e2af",
            fg=self.tema.BTN_TEXT_COLOR,
            font=('Arial', 9, 'bold'),
            border=0,
            cursor="hand2",
            padx=10,
            pady=5
        )
        btn_journal.pack(side=tk.LEFT, padx=(5, 0))
        
        # Cargar logs iniciales
        self.actualizar_logs()
    
    def _crear_tab_log(self, nombre):
        """Crea un tab con área de texto para mostrar logs"""
        frame = tk.Frame(self.notebook, bg=self.tema.CARD_BG)
        
        # Área de texto con scroll
        text_area = scrolledtext.ScrolledText(
            frame,
            wrap=tk.WORD,
            width=80,
            height=20,
            font=ConfiguracionApp.FUENTE_LOG,
            bg="#1a1a2e",
            fg="#e0e0e0",
            insertbackground="#e0e0e0",
            relief=tk.FLAT,
            padx=10,
            pady=10
        )
        text_area.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)
        
        # Guardar referencia
        if nombre == "Apache":
            self.text_apache = text_area
        elif nombre == "MySQL":
            self.text_mysql = text_area
        
        return frame
    
    def _leer_ultimas_lineas(self, archivo, num_lineas=50):
        """
        Lee las últimas líneas de un archivo de log
        
        Args:
            archivo: Ruta del archivo
            num_lineas: Número de líneas a leer
            
        Returns:
            str: Contenido del log o mensaje de error
        """
        # Usar el gestor de servicios para ejecutar con la contraseña guardada
        success, stdout, stderr = self.gestor_servicios.ejecutar_comando(
            f"tail -n {num_lineas} {archivo}",
            usar_sudo=True
        )
        
        if success:
            return stdout if stdout else f"El archivo {archivo} está vacío"
        else:
            return f"No se pudo leer el archivo {archivo}\n{stderr}"
    
    def actualizar_logs(self):
        """Actualiza el contenido de todos los logs"""
        # Actualizar Apache
        contenido_apache = self._leer_ultimas_lineas(RutasLogs.APACHE_ERROR)
        self.text_apache.delete(1.0, tk.END)
        self.text_apache.insert(1.0, contenido_apache)
        
        # Actualizar MySQL/MariaDB - intentar ambas rutas
        contenido_mysql = self._leer_log_mysql()
        self.text_mysql.delete(1.0, tk.END)
        self.text_mysql.insert(1.0, contenido_mysql)
    
    def _leer_log_mysql(self):
        """Lee el log de MySQL intentando diferentes rutas para MySQL y MariaDB"""
        import os
        
        # Lista de posibles ubicaciones de logs
        posibles_rutas = [
            RutasLogs.MYSQL_ERROR,
            RutasLogs.MARIADB_ERROR,
            "/var/log/mysqld.log",
            "/var/log/mysql.log",
            "/var/log/mariadb/error.log"
        ]
        
        # Intentar cada ruta
        for ruta in posibles_rutas:
            # Verificar si el archivo existe sin usar sudo
            try:
                if os.path.exists(ruta):
                    contenido = self._leer_ultimas_lineas(ruta)
                    if contenido and "No se pudo leer" not in contenido:
                        return f"=== Logs desde {ruta} ===\n\n" + contenido
            except:
                pass
        
        # Si ninguna ruta funciona, buscar en syslog
        success, stdout, stderr = self.gestor_servicios.ejecutar_comando(
            "grep -iE 'mysql|mariadb' /var/log/syslog | tail -n 50",
            usar_sudo=True
        )
        
        if success and stdout:
            return "=== Logs de MySQL/MariaDB desde syslog ===\n\n" + stdout
        
        # Último recurso: intentar obtener la configuración de logs de MySQL
        success2, stdout2, stderr2 = self.gestor_servicios.ejecutar_comando(
            "mysql -e \"SHOW VARIABLES LIKE 'log_error';\" 2>&1 || mariadb -e \"SHOW VARIABLES LIKE 'log_error';\" 2>&1",
            usar_sudo=False
        )
        
        mensaje = "No se encontraron logs de MySQL/MariaDB en las ubicaciones comunes.\n\n"
        mensaje += "Ubicaciones verificadas:\n"
        for ruta in posibles_rutas:
            mensaje += f"  - {ruta}\n"
        
        if success2 and stdout2 and "log_error" in stdout2:
            mensaje += f"\n{stdout2}\n\nPuedes verificar la configuración en:\n"
            mensaje += "  - /etc/mysql/mysql.conf.d/mysqld.cnf\n"
            mensaje += "  - /etc/my.cnf\n"
        else:
            mensaje += "\nLos logs podrían estar en syslog o journal.\n"
            mensaje += "Prueba: sudo journalctl -u mysql -n 50\n"
            mensaje += "     o: sudo journalctl -u mariadb -n 50"
        
        return mensaje
    
    def limpiar_logs(self):
        """Limpia la visualización de los logs (no el archivo real)"""
        tab_actual = self.notebook.index(self.notebook.select())
        
        if tab_actual == 0:  # Apache
            self.text_apache.delete(1.0, tk.END)
            self.text_apache.insert(1.0, "Log limpiado. Presiona 'Actualizar' para recargar.")
        elif tab_actual == 1:  # MySQL
            self.text_mysql.delete(1.0, tk.END)
            self.text_mysql.insert(1.0, "Log limpiado. Presiona 'Actualizar' para recargar.")
    
    def ver_journal(self):
        """Muestra logs desde journalctl para el servicio actual"""
        tab_actual = self.notebook.index(self.notebook.select())
        
        if tab_actual == 0:  # Apache
            servicio = "apache2"
            text_widget = self.text_apache
        elif tab_actual == 1:  # MySQL/MariaDB
            # Intentar ambos servicios
            success1, stdout1, stderr1 = self.gestor_servicios.ejecutar_comando(
                "journalctl -u mysql -n 50 --no-pager",
                usar_sudo=True
            )
            success2, stdout2, stderr2 = self.gestor_servicios.ejecutar_comando(
                "journalctl -u mariadb -n 50 --no-pager",
                usar_sudo=True
            )
            
            text_widget = self.text_mysql
            
            if success1 and stdout1 and len(stdout1) > 100:
                text_widget.delete(1.0, tk.END)
                text_widget.insert(1.0, f"=== Journal de mysql ===\n\n{stdout1}")
                return
            elif success2 and stdout2 and len(stdout2) > 100:
                text_widget.delete(1.0, tk.END)
                text_widget.insert(1.0, f"=== Journal de mariadb ===\n\n{stdout2}")
                return
            else:
                text_widget.delete(1.0, tk.END)
                text_widget.insert(1.0, "No se encontraron entradas en journal para mysql o mariadb")
                return
        else:
            return
        
        # Para Apache
        success, stdout, stderr = self.gestor_servicios.ejecutar_comando(
            f"journalctl -u {servicio} -n 50 --no-pager",
            usar_sudo=True
        )
        
        if success and stdout:
            text_widget.delete(1.0, tk.END)
            text_widget.insert(1.0, f"=== Journal de {servicio} ===\n\n{stdout}")
        else:
            text_widget.delete(1.0, tk.END)
            text_widget.insert(1.0, f"No se pudo obtener el journal de {servicio}\n{stderr}")
