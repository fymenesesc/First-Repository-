#pip install mysql-connector-python
#pip install tabulate
import mysql.connector

class Usuarios:
    """
    CRUD Crear, modificar o eliminar Usuarios - BOXHAPP
    """

    def __init__(self):
        """
        Establece la conexión con la base de datos.
        """
        self.conexion = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="Jonathan29@",
            database="boxhapp"
        )
     
    def cerrar_conexion(self):
        """
        Cierra la conexión con la base de datos de manera segura.
        """
        if self.conexion and self.conexion.is_connected():
            self.conexion.close()
            print("Conexión a la base de datos cerrada.")

    def __str__(self):
        """
        Mostrar todos los Usuarios.
        """
        usuarios = self.obtener_todos_los_usuarios()
        texto = ""
        for usuario in usuarios:
            texto += f"{usuario}\n"
        return texto

    def obtener_todos_los_usuarios(self):
        """
        Consultar todos los usuarios.
        """
        if not self.conexion or not self.conexion.is_connected():
            return []
        
        cursor = self.conexion.cursor()
        try:
            cursor.execute("SELECT * FROM boxhapp.tb_dat_usuarios")
            resultado = cursor.fetchall()
            return resultado
        except mysql.connector.Error as err:
            print(f"Error al obtener usuarios: {err}")
            return []
        finally:
            cursor.close()

    def buscar_usuario_por_id(self, id_usuario):
        """
        Busca un usuario por su ID.
        """
        if not self.conexion or not self.conexion.is_connected():
            return None
            
        cursor = self.conexion.cursor()
        try:
            cursor.execute("SELECT * FROM boxhapp.tb_dat_usuarios WHERE id_usuario = %s", (id_usuario,))
            resultado = cursor.fetchone()
            return resultado
        except mysql.connector.Error as err:
            print(f"Error al buscar usuario: {err}")
            return None
        finally:
            cursor.close()

    def validar_id_rol(self, id_rol):
        """
        Verifica si un ID de rol existe en la base de datos.
        """
        if not self.conexion or not self.conexion.is_connected():
            return False
            
        cursor = self.conexion.cursor()
        try:
            consulta = "SELECT id_rol FROM boxhapp.tb_dat_roles WHERE id_rol = %s"
            cursor.execute(consulta, (id_rol,))
            resultado = cursor.fetchone()
            return resultado is not None
        except mysql.connector.Error as err:
            print(f"Error al verificar el ID del rol: {err}")
            return False
        finally:
            cursor.close()

    def crear_usuario(self, primer_nombre, segundo_nombre, primer_apellido, segundo_apellido, correo, celular, tipo_documento, id_identificacion, fecha_nacimiento, cargo, contrasena, id_rol, Usuario):
        """
        Agregar un nuevo usuario.
        """
        if not self.conexion or not self.conexion.is_connected():
            return 0
        """
        Validar el ID del rol antes de la inserción
        """
        if not self.validar_id_rol(id_rol):
            print(f"Error: El ID de Rol {id_rol} no existe en la tabla de roles.")
            return 0
            
        cursor = self.conexion.cursor()
        try:
            consulta = """
                INSERT INTO boxhapp.tb_dat_usuarios (
                    primer_nombre, segundo_nombre, primer_apellido, segundo_apellido,
                    correo, celular, tipo_documento, id_identificacion, fecha_nacimiento,
                    cargo, contrasena, id_rol, Usuario
                )
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
            """
            valores = (
                primer_nombre, segundo_nombre, primer_apellido, segundo_apellido,
                correo, str(celular), tipo_documento, id_identificacion, fecha_nacimiento,
                cargo, contrasena, id_rol, Usuario
            )
            cursor.execute(consulta, valores)
            filas = cursor.rowcount
            self.conexion.commit()
            return filas
        except mysql.connector.Error as err:
            print(f"Error al crear usuario: {err}")
            self.conexion.rollback()
            return 0
        finally:
            cursor.close()

    def eliminar_usuario_por_id(self, id_usuario):
        """
        Eliminar un usuario por su ID.
        """
        if not self.conexion or not self.conexion.is_connected():
            return 0
            
        cursor = self.conexion.cursor()
        try:
            cursor.execute("DELETE FROM boxhapp.tb_dat_usuarios WHERE id_usuario = %s", (id_usuario,))
            filas = cursor.rowcount
            self.conexion.commit()
            return filas
        except mysql.connector.Error as err:
            print(f"Error al eliminar usuario: {err}")
            self.conexion.rollback()
            return 0
        finally:
            cursor.close()

    def modificar_usuario(self, id_usuario, primer_nombre, segundo_nombre, primer_apellido, segundo_apellido, correo, celular, tipo_documento, id_identificacion, fecha_nacimiento, cargo, contrasena, id_rol, Usuario):
        """
        Modificar un usuario por ID.
        """
        if not self.conexion or not self.conexion.is_connected():
            return 0
        
        if not self.validar_id_rol(id_rol):
            print(f"Error: El ID de Rol {id_rol} no existe en la tabla de roles.")
            return 0
            
        cursor = self.conexion.cursor()
        try:
            consulta = """
                UPDATE boxhapp.tb_dat_usuarios
                SET
                    primer_nombre = %s,
                    segundo_nombre = %s,
                    primer_apellido = %s,
                    segundo_apellido = %s,
                    correo = %s,
                    celular = %s,
                    tipo_documento = %s,
                    id_identificacion = %s,
                    fecha_nacimiento = %s,
                    cargo = %s,
                    contrasena = %s,
                    id_rol = %s,
                    Usuario = %s
                WHERE id_usuario = %s
            """
            valores = (
                primer_nombre, segundo_nombre, primer_apellido, segundo_apellido,
                correo, str(celular), tipo_documento, id_identificacion, fecha_nacimiento,
                cargo, contrasena, id_rol, Usuario, id_usuario
            )
            cursor.execute(consulta, valores)
            filas = cursor.rowcount
            self.conexion.commit()
            return filas
        except mysql.connector.Error as err:
            print(f"Error al modificar usuario: {err}")
            self.conexion.rollback()
            return 0
        finally:
            cursor.close()
