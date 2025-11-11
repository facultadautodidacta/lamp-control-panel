"""
Módulo de configuración y estilos visuales
Define colores, fuentes y estilos del tema de la aplicación
"""


class TemaOscuro:
    """Configuración de colores para el tema oscuro"""
    
    # Colores base
    BG_COLOR = "#1e1e2e"
    FG_COLOR = "#cdd6f4"
    ACCENT_COLOR = "#89b4fa"
    CARD_BG = "#313244"
    
    # Colores de separadores
    SEPARATOR_COLOR = "#45475a"
    
    # Colores de botones
    BTN_INICIAR_BG = "#a6e3a1"
    BTN_INICIAR_ACTIVE = "#94d293"
    BTN_DETENER_BG = "#f38ba8"
    BTN_DETENER_ACTIVE = "#e17896"
    BTN_REINICIAR_BG = "#89b4fa"
    BTN_REINICIAR_ACTIVE = "#77a2e8"
    BTN_TEXT_COLOR = "#1e1e2e"
    
    # Colores de estado
    STATUS_ACTIVO = "#28a745"
    STATUS_INACTIVO = "#dc3545"
    STATUS_INFO = "orange"
    
    # Colores del footer
    FOOTER_TEXT_COLOR = "#6c7086"
    SEPARATOR_COLOR = "#45475a"


class ConfiguracionApp:
    """Configuración general de la aplicación"""
    
    # Dimensiones de la ventana
    VENTANA_ANCHO = 800
    VENTANA_ALTO = 650
    
    # Intervalos de actualización (milisegundos)
    INTERVALO_ACTUALIZACION = 3000  # 3 segundos
    DELAY_ACTUALIZACION_COMANDO = 1000  # 1 segundo
    
    # Tamaño del logo
    LOGO_TAMANO = (30, 30)
    
    # Fuentes
    FUENTE_TITULO = ('Arial', 20, 'bold')
    FUENTE_HEADER = ('Arial', 14, 'bold')
    FUENTE_STATUS = ('Arial', 10)
    FUENTE_BOTON = ('Arial', 11, 'bold')
    FUENTE_FOOTER = ('Arial', 9)
    FUENTE_LOG = ('Courier', 9)
    FUENTE_TAB = ('Arial', 11)
    
    # Dimensiones de botones
    BOTON_ANCHO = 18
    BOTON_ALTO = 2
    
    # Logs
    LINEAS_LOG = 10  # Número de líneas a mostrar


class Servicios:
    """Nombres de los servicios del sistema"""
    
    APACHE = "apache2"
    MYSQL = "mysql"


class RutasLogs:
    """Rutas de archivos de logs del sistema"""
    
    APACHE_ERROR = "/var/log/apache2/error.log"
    # MariaDB y MySQL pueden usar diferentes rutas
    MYSQL_ERROR = "/var/log/mysql/error.log"
    MARIADB_ERROR = "/var/log/mariadb/mariadb.log"
    SYSLOG = "/var/log/syslog"
