"""
Módulo para gestión de servicios del sistema
Maneja operaciones de inicio, detención y verificación de estado de servicios
"""

import subprocess
import os
import tempfile


class GestorServicios:
    """Clase para gestionar servicios del sistema usando systemctl"""
    
    def __init__(self):
        self.timeout = 30
        self._password_file = None
    
    def configurar_password(self, password):
        """
        Guarda la contraseña en un archivo temporal para reutilizarla
        
        Args:
            password (str): Contraseña del usuario
        """
        # Crear archivo temporal seguro
        fd, self._password_file = tempfile.mkstemp(text=True)
        os.write(fd, (password + '\n').encode())
        os.close(fd)
        # Dar permisos solo al usuario
        os.chmod(self._password_file, 0o600)
    
    def limpiar_password(self):
        """Elimina el archivo temporal de contraseña"""
        if self._password_file and os.path.exists(self._password_file):
            os.remove(self._password_file)
            self._password_file = None
    
    def verificar_servicio_activo(self, nombre_servicio):
        """
        Verifica si un servicio está activo
        
        Args:
            nombre_servicio (str): Nombre del servicio a verificar
            
        Returns:
            bool: True si el servicio está activo, False en caso contrario
        """
        try:
            resultado = subprocess.run(
                ['systemctl', 'is-active', nombre_servicio],
                capture_output=True,
                text=True,
                timeout=5
            )
            return resultado.stdout.strip() == "active"
        except Exception:
            return False
    
    def ejecutar_comando(self, comando, usar_sudo=True):
        """
        Ejecuta un comando del sistema
        
        Args:
            comando (str): Comando a ejecutar
            usar_sudo (bool): Si se debe usar privilegios sudo
            
        Returns:
            tuple: (success: bool, stdout: str, stderr: str)
        """
        try:
            if usar_sudo:
                # Si tenemos contraseña guardada, usar sudo con -S
                if self._password_file:
                    with open(self._password_file, 'r') as f:
                        password = f.read()
                    
                    cmd = ['sudo', '-S'] + comando.split()
                    resultado = subprocess.run(
                        cmd,
                        input=password,
                        capture_output=True,
                        text=True,
                        timeout=self.timeout
                    )
                else:
                    # Usar pkexec si no hay contraseña guardada
                    cmd = ['pkexec'] + comando.split()
                    resultado = subprocess.run(
                        cmd,
                        capture_output=True,
                        text=True,
                        timeout=self.timeout
                    )
            else:
                cmd = comando.split()
                resultado = subprocess.run(
                    cmd,
                    capture_output=True,
                    text=True,
                    timeout=self.timeout
                )
            
            success = resultado.returncode == 0
            return success, resultado.stdout.strip(), resultado.stderr.strip()
            
        except subprocess.TimeoutExpired:
            return False, "", "El comando tardó demasiado tiempo"
        except Exception as e:
            return False, "", str(e)
    
    def iniciar_servicio(self, nombre_servicio):
        """Inicia un servicio del sistema"""
        return self.ejecutar_comando(f"systemctl start {nombre_servicio}", usar_sudo=True)
    
    def detener_servicio(self, nombre_servicio):
        """Detiene un servicio del sistema"""
        return self.ejecutar_comando(f"systemctl stop {nombre_servicio}", usar_sudo=True)
    
    def reiniciar_servicio(self, nombre_servicio):
        """Reinicia un servicio del sistema"""
        return self.ejecutar_comando(f"systemctl restart {nombre_servicio}", usar_sudo=True)
