#pip install mysql-connector-python
#pip install tabulate
import mysql.connector

class Roles:
    """
    CRUD Crear, modificar o eliminar roles - BOXHAPP
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
     
    def __str__(self):
        """
        Mostrar todos los Roles.
        """
        roles = self.obtener_todos_los_roles()
        texto = ""
        for rol in roles:
            texto += f"{rol}\n"
        return texto

    def obtener_todos_los_roles(self):
        """
        Consultar todos los roles.
        """
        cursor = self.conexion.cursor()
        cursor.execute("SELECT * FROM boxhapp.tb_dat_roles")
        resultado = cursor.fetchall()
        cursor.close()
        return resultado

    def buscar_rol_por_id(self, id_rol):
        """
        Busca un rol por su ID.
        """
        cursor = self.conexion.cursor()
        cursor.execute("SELECT * FROM boxhapp.tb_dat_roles WHERE id_rol = %s", (id_rol,))
        resultado = cursor.fetchone()
        cursor.close()
        return resultado

    def crear_rol(self, nombre_rol, Descripcion):
        """
        Agregar un nuevo Rol.
        """
        cursor = self.conexion.cursor()
        consulta = """
            INSERT INTO boxhapp.tb_dat_roles (nombre_rol, Descripcion)
            VALUES (%s, %s)
        """
        valores = (nombre_rol, Descripcion)
        cursor.execute(consulta, valores)
        filas = cursor.rowcount
        self.conexion.commit()
        cursor.close()
        return filas

    def eliminar_rol_por_id(self, id_rol):
        """
        Eliminar un rol por su ID.
        """
        cursor = self.conexion.cursor()
        cursor.execute("DELETE FROM boxhapp.tb_dat_roles WHERE id_rol = %s", (id_rol,))
        filas = cursor.rowcount
        self.conexion.commit()
        cursor.close()
        return filas

    def modificar_rol(self, id_rol, nombre_rol, Descripcion):
        """
        Modificar un rol por id.
        """
        cursor = self.conexion.cursor()
        consulta = """
            UPDATE boxhapp.tb_dat_roles
            SET nombre_rol = %s, Descripcion = %s
            WHERE id_rol = %s
        """
        valores = (nombre_rol, Descripcion, id_rol)
        cursor.execute(consulta, valores)
        filas = cursor.rowcount
        self.conexion.commit()
        cursor.close()
        return filas
        
        
       