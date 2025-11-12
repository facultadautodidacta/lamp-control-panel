#!/usr/bin/env python3
"""
Panel de Control LAMP
Interfaz gráfica para gestionar servicios de Apache, MySQL y PHP

Desarrollado por RAS - 2025
"""

import tkinter as tk
from tkinter import ttk, messagebox, simpledialog
import os
from PIL import Image, ImageTk

# Importar módulos personalizados
from config import TemaOscuro, ConfiguracionApp, Servicios
from servicios import GestorServicios
from componentes import SeccionServicio, Footer, VisorLogs


class PanelControlLAMP:
    """Clase principal del Panel de Control LAMP"""
    
    def __init__(self, root):
        """Inicializa la aplicación"""
        self.root = root
        self.root.title("Panel de Control LAMP")
        self.root.geometry(f"{ConfiguracionApp.VENTANA_ANCHO}x{ConfiguracionApp.VENTANA_ALTO}")
        self.root.resizable(False, False)
        
        # Configurar clase de ventana (importante para la barra de tareas en Linux)
        try:
            self.root.wm_class("lamp-control-panel", "LAMP-Control-Panel")
        except:
            pass
        
        # Configurar icono de la ventana para la barra de tareas
        self._configurar_icono_ventana()
        
        # Configurar tema
        self.tema = TemaOscuro()
        self.root.configure(bg=self.tema.BG_COLOR)
        
        # Inicializar gestor de servicios
        self.gestor_servicios = GestorServicios()
        
        # Verificar servicios LAMP instalados
        self._verificar_servicios_lamp()
        
        # Solicitar contraseña al inicio
        self._solicitar_password()
        
        # Referencias a secciones de servicios
        self.seccion_apache = None
        self.seccion_mysql = None
        self.status_label = None
        self.visor_logs = None
        self.notebook = None
        
        # Logo
        self.logo_photo = None
        
        # Configurar estilos y crear interfaz
        self.setup_styles()
        self.crear_interfaz()
        
        # Limpiar contraseña al cerrar
        self.root.protocol("WM_DELETE_WINDOW", self._on_closing)
    
    def _configurar_icono_ventana(self):
        """Configura el icono de la ventana para la barra de tareas"""
        try:
            # Obtener ruta del script
            directorio_script = os.path.dirname(os.path.abspath(__file__))
            ruta_png = os.path.join(directorio_script, "logo.png")
            
            if os.path.exists(ruta_png):
                # Cargar imagen
                icono_img = Image.open(ruta_png)
                
                # Convertir a RGBA si no lo está
                if icono_img.mode != 'RGBA':
                    icono_img = icono_img.convert('RGBA')
                
                # Crear múltiples tamaños para mejor compatibilidad
                tamaños = [16, 24, 32, 48, 64]
                iconos = []
                
                for tamaño in tamaños:
                    img_redimensionada = icono_img.resize((tamaño, tamaño), Image.LANCZOS)
                    icono_photo = ImageTk.PhotoImage(img_redimensionada)
                    iconos.append(icono_photo)
                
                # Establecer iconos (el True hace que se aplique a todas las ventanas hijas)
                self.root.iconphoto(True, *iconos)
                
                # Intentar también con wm_iconbitmap como fallback para X11
                try:
                    # Crear un XBM temporal para sistemas que lo requieren
                    import tempfile
                    # Esto es específico para algunos gestores de ventanas en Linux
                    self.root.wm_iconname("LAMP Panel")
                except:
                    pass
                
                # Mantener referencias para evitar garbage collection
                self.root._iconos_photos = iconos
        except Exception as e:
            print(f"No se pudo cargar el icono: {e}")
    
    def _verificar_servicios_lamp(self):
        """Verifica si los servicios LAMP están instalados"""
        import subprocess
        
        servicios_faltantes = []
        
        # Verificar Apache
        try:
            resultado = subprocess.run(
                ['systemctl', 'list-unit-files', 'apache2.service'],
                capture_output=True,
                text=True
            )
            if 'apache2.service' not in resultado.stdout:
                servicios_faltantes.append('Apache2')
        except:
            servicios_faltantes.append('Apache2')
        
        # Verificar MySQL/MariaDB
        mysql_encontrado = False
        for servicio in ['mysql.service', 'mariadb.service']:
            try:
                resultado = subprocess.run(
                    ['systemctl', 'list-unit-files', servicio],
                    capture_output=True,
                    text=True
                )
                if servicio in resultado.stdout:
                    mysql_encontrado = True
                    break
            except:
                pass
        
        if not mysql_encontrado:
            servicios_faltantes.append('MySQL/MariaDB')
        
        # Mostrar advertencia si faltan servicios
        if servicios_faltantes:
            mensaje = "⚠️ SERVICIOS NO DETECTADOS\n\n"
            mensaje += "Los siguientes servicios no están instalados:\n"
            mensaje += "\n".join(f"  • {s}" for s in servicios_faltantes)
            mensaje += "\n\nEl panel se abrirá, pero no podrás gestionar "
            mensaje += "los servicios que no estén instalados.\n\n"
            mensaje += "Para instalar los servicios faltantes:\n"
            
            if 'Apache2' in servicios_faltantes:
                mensaje += "\n  Apache: sudo apt-get install apache2"
            if 'MySQL/MariaDB' in servicios_faltantes:
                mensaje += "\n  MySQL: sudo apt-get install mysql-server"
                mensaje += "\n  MariaDB: sudo apt-get install mariadb-server"
            
            messagebox.showwarning("Servicios LAMP no instalados", mensaje)
    
    def _solicitar_password(self):
        """Solicita la contraseña de root al usuario"""
        password = simpledialog.askstring(
            "Autenticación requerida",
            "Ingresa tu contraseña de sudo:",
            show='*'
        )
        
        if password:
            self.gestor_servicios.configurar_password(password)
        else:
            messagebox.showwarning(
                "Advertencia",
                "No se ingresó contraseña. Se solicitará permisos para cada operación."
            )
    
    def _on_closing(self):
        """Ejecuta limpieza al cerrar la aplicación"""
        self.gestor_servicios.limpiar_password()
        self.root.destroy()
    
    def setup_styles(self):
        """Configura los estilos de la interfaz"""
        style = ttk.Style()
        style.theme_use('clam')
        
        # Estilos personalizados
        style.configure('Title.TLabel', 
                       background=self.tema.BG_COLOR,
                       foreground=self.tema.ACCENT_COLOR,
                       font=ConfiguracionApp.FUENTE_TITULO)
        
        style.configure('Card.TFrame',
                       background=self.tema.CARD_BG,
                       relief='flat')
        
        style.configure('Header.TLabel',
                       background=self.tema.CARD_BG,
                       foreground=self.tema.FG_COLOR,
                       font=ConfiguracionApp.FUENTE_HEADER)
        
        style.configure('Status.TLabel',
                       background=self.tema.CARD_BG,
                       foreground=self.tema.FG_COLOR,
                       font=ConfiguracionApp.FUENTE_STATUS)
        
        # Estilo para el Notebook (pestañas)
        style.configure('TNotebook', 
                       background=self.tema.BG_COLOR,
                       borderwidth=0)
        style.configure('TNotebook.Tab',
                       background=self.tema.CARD_BG,
                       foreground=self.tema.FG_COLOR,
                       padding=[20, 10],
                       font=ConfiguracionApp.FUENTE_TAB)
        style.map('TNotebook.Tab',
                 background=[('selected', self.tema.ACCENT_COLOR)],
                 foreground=[('selected', self.tema.BG_COLOR)])
    
    def crear_interfaz(self):
        """Crea todos los elementos de la interfaz"""
        # Frame principal
        main_frame = tk.Frame(self.root, bg=self.tema.BG_COLOR, padx=25, pady=25)
        main_frame.pack(fill=tk.BOTH, expand=True)
        
        # Título
        titulo = ttk.Label(main_frame, text="🖥️  Panel de Control LAMP", 
                          style='Title.TLabel')
        titulo.pack(pady=(0, 20))
        
        # Crear Notebook (pestañas)
        self.notebook = ttk.Notebook(main_frame)
        self.notebook.pack(fill=tk.BOTH, expand=True)
        
        # Pestaña de Servicios
        self._crear_tab_servicios()
        
        # Pestaña de Logs
        self._crear_tab_logs()
        
        # Cargar logo
        self._cargar_logo()
        
        # Footer (fuera del notebook)
        self._crear_footer(main_frame)
    
    def _crear_footer(self, parent):
        """Crea el footer con separador, logo y créditos"""
        # Separador
        separator = tk.Frame(parent, height=1, bg=self.tema.SEPARATOR_COLOR)
        separator.pack(fill=tk.X, pady=(15, 10))
        
        # Frame del footer
        footer_frame = tk.Frame(parent, bg=self.tema.BG_COLOR)
        footer_frame.pack(fill=tk.X)
        
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
    
    def _crear_tab_servicios(self):
        """Crea la pestaña de control de servicios"""
        tab_servicios = tk.Frame(self.notebook, bg=self.tema.BG_COLOR, padx=20, pady=20)
        self.notebook.add(tab_servicios, text="⚙️  Servicios")
        
        # Sección Apache
        self.seccion_apache = SeccionServicio(
            parent=tab_servicios,
            nombre_servicio="Apache Web Server",
            icono="🌐",
            tema=self.tema,
            fila=0,
            callback_iniciar=self.iniciar_apache,
            callback_detener=self.detener_apache,
            callback_reiniciar=self.reiniciar_apache
        )
        
        # Label de estado general
        self.status_label = tk.Label(tab_servicios, text="", 
                                    font=ConfiguracionApp.FUENTE_STATUS,
                                    bg=self.tema.BG_COLOR,
                                    fg=self.tema.FG_COLOR)
        self.status_label.grid(row=2, column=0, columnspan=3, pady=20)
        
        # Sección MySQL
        self.seccion_mysql = SeccionServicio(
            parent=tab_servicios,
            nombre_servicio="MySQL Database",
            icono="🗄️",
            tema=self.tema,
            fila=3,
            callback_iniciar=self.iniciar_mysql,
            callback_detener=self.detener_mysql,
            callback_reiniciar=self.reiniciar_mysql
        )
        
        # Actualizar estados iniciales
        self.actualizar_estados()
        
        # Actualizar estados cada 3 segundos
        self.actualizar_estados_periodicamente()
    
    def _crear_tab_logs(self):
        """Crea la pestaña del visor de logs"""
        tab_logs = tk.Frame(self.notebook, bg=self.tema.BG_COLOR, padx=20, pady=20)
        self.notebook.add(tab_logs, text="📋  Logs de Error")
        
        # Visor de Logs
        self.visor_logs = VisorLogs(
            parent=tab_logs,
            tema=self.tema,
            gestor_servicios=self.gestor_servicios
        )
    
    def _cargar_logo(self):
        """Carga el logo de la aplicación"""
        try:
            logo_path = os.path.join(os.path.dirname(__file__), 'logo.png')
            logo_image = Image.open(logo_path)
            logo_image = logo_image.resize(ConfiguracionApp.LOGO_TAMANO, Image.Resampling.LANCZOS)
            self.logo_photo = ImageTk.PhotoImage(logo_image)
        except Exception as e:
            print(f"No se pudo cargar el logo: {e}")
    
    # ====================
    # MÉTODOS DE APACHE
    # ====================
    
    def iniciar_apache(self):
        """Inicia el servicio de Apache"""
        if self.gestor_servicios.verificar_servicio_activo(Servicios.APACHE):
            self._mostrar_mensaje_info("Apache ya está iniciado")
        else:
            self._ejecutar_accion_servicio(
                Servicios.APACHE,
                self.gestor_servicios.iniciar_servicio,
                "Iniciar Apache"
            )
    
    def detener_apache(self):
        """Detiene el servicio de Apache"""
        if not self.gestor_servicios.verificar_servicio_activo(Servicios.APACHE):
            self._mostrar_mensaje_info("Apache ya está detenido")
        else:
            self._ejecutar_accion_servicio(
                Servicios.APACHE,
                self.gestor_servicios.detener_servicio,
                "Detener Apache"
            )
    
    def reiniciar_apache(self):
        """Reinicia el servicio de Apache"""
        self._ejecutar_accion_servicio(
            Servicios.APACHE,
            self.gestor_servicios.reiniciar_servicio,
            "Reiniciar Apache"
        )
    
    # ====================
    # MÉTODOS DE MYSQL
    # ====================
    
    def iniciar_mysql(self):
        """Inicia el servicio de MySQL"""
        if self.gestor_servicios.verificar_servicio_activo(Servicios.MYSQL):
            self._mostrar_mensaje_info("MySQL ya está iniciado")
        else:
            self._ejecutar_accion_servicio(
                Servicios.MYSQL,
                self.gestor_servicios.iniciar_servicio,
                "Iniciar MySQL"
            )
    
    def detener_mysql(self):
        """Detiene el servicio de MySQL"""
        if not self.gestor_servicios.verificar_servicio_activo(Servicios.MYSQL):
            self._mostrar_mensaje_info("MySQL ya está detenido")
        else:
            self._ejecutar_accion_servicio(
                Servicios.MYSQL,
                self.gestor_servicios.detener_servicio,
                "Detener MySQL"
            )
    
    def reiniciar_mysql(self):
        """Reinicia el servicio de MySQL"""
        self._ejecutar_accion_servicio(
            Servicios.MYSQL,
            self.gestor_servicios.reiniciar_servicio,
            "Reiniciar MySQL"
        )
    
    # ====================
    # MÉTODOS AUXILIARES
    # ====================
    
    def _ejecutar_accion_servicio(self, nombre_servicio, accion, descripcion):
        """
        Ejecuta una acción sobre un servicio y muestra el resultado
        
        Args:
            nombre_servicio: Nombre del servicio
            accion: Función a ejecutar (del GestorServicios)
            descripcion: Descripción de la acción para mensajes
        """
        success, stdout, stderr = accion(nombre_servicio)
        
        if success:
            self.status_label.config(
                text=f"✓ {descripcion}: {stdout if stdout else 'Completado'}",
                foreground=self.tema.STATUS_ACTIVO
            )
            messagebox.showinfo("Éxito", f"{descripcion}\nSalida: {stdout if stdout else 'Completado'}")
        else:
            self.status_label.config(
                text=f"✗ Error al {descripcion.lower()}",
                foreground=self.tema.STATUS_INACTIVO
            )
            messagebox.showerror("Error", f"Error al {descripcion.lower()}\n{stderr}")
        
        # Actualizar estado después de 1 segundo
        self.root.after(ConfiguracionApp.DELAY_ACTUALIZACION_COMANDO, self.actualizar_estados)
    
    def _mostrar_mensaje_info(self, mensaje):
        """Muestra un mensaje informativo"""
        self.status_label.config(
            text=f"ℹ {mensaje}",
            foreground=self.tema.STATUS_INFO
        )
        messagebox.showinfo("Información", mensaje)
    
    def actualizar_estados(self):
        """Actualiza los indicadores de estado de todos los servicios"""
        # Actualizar Apache
        apache_activo = self.gestor_servicios.verificar_servicio_activo(Servicios.APACHE)
        self.seccion_apache.actualizar_estado(apache_activo)
        
        # Actualizar MySQL
        mysql_activo = self.gestor_servicios.verificar_servicio_activo(Servicios.MYSQL)
        self.seccion_mysql.actualizar_estado(mysql_activo)
    
    def actualizar_estados_periodicamente(self):
        """Actualiza los estados cada intervalo configurado"""
        self.actualizar_estados()
        self.root.after(ConfiguracionApp.INTERVALO_ACTUALIZACION, self.actualizar_estados_periodicamente)


def main():
    """Función principal"""
    root = tk.Tk()
    app = PanelControlLAMP(root)
    root.mainloop()


if __name__ == "__main__":
    main()
