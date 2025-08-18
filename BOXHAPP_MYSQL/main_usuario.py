from usuarios import Usuarios
from tabulate import tabulate
import datetime

def solicitar_entero(mensaje, minimo=None):
    while True:
        try:
            valor = int(input(mensaje))
            if minimo is not None and valor < minimo:
                print(f"El valor debe ser mayor o igual a {minimo}.")
                continue
            return valor
        except ValueError:
            print("Por favor, ingresa un número entero válido.")

def solicitar_decimal(mensaje, minimo=None):
    while True:
        try:
            valor = float(input(mensaje))
            if minimo is not None and valor < minimo:
                print(f"El valor debe ser mayor o igual a {minimo}.")
                continue
            return valor
        except ValueError:
            print("Por favor, ingresa un número válido.")
            
def solicitar_texto(mensaje, max_length=None):
    """
    Solicita un texto que no puede estar vacío y valida su longitud máxima.
    """
    while True:
        texto = input(mensaje).strip()
        if texto == "":
            print("Este campo no puede estar vacío.")
        elif max_length is not None and len(texto) > max_length:
            print(f"Error: El texto no puede tener más de {max_length} caracteres.")
        else:
            return texto

def solicitar_texto_opcional(mensaje, max_length=None):
    """
    Solicita un texto que puede ser opcional (se permite dejar en blanco) y valida su longitud.
    """
    texto = input(mensaje).strip()
    if max_length is not None and len(texto) > max_length:
        print(f"Error: El texto no puede tener más de {max_length} caracteres. Por favor, ingresa un valor más corto o deja el campo vacío.")
        return solicitar_texto_opcional(mensaje, max_length)
    return texto

def solicitar_fecha(mensaje):
    while True:
        fecha_str = input(mensaje).strip()
        try:
            return datetime.date.fromisoformat(fecha_str)
        except ValueError:
            print("Formato de fecha incorrecto. Por favor, usa YYYY-MM-DD.")

def solicitar_celular(mensaje):
    """
    Solicita y valida un número de celular de hasta 10 dígitos.
    La función se repite hasta que se ingrese un valor válido.
    """
    while True:
        celular_str = input(mensaje).strip()
        if not celular_str:
            print("Este campo no puede estar vacío.")
            continue
        if not celular_str.isdigit():
            print("Error: El número de celular solo debe contener dígitos.")
            continue
        if len(celular_str) != 10:
            print("Error: El número de celular debe tener 10 dígitos.")
            continue
        return int(celular_str)

def mostrar_menu():
    administrar_usuarios = Usuarios()
    if not administrar_usuarios.conexion or not administrar_usuarios.conexion.is_connected():
        print("No se pudo iniciar la aplicación debido a un error de conexión.")
        return
        
    opcion = 0
    while opcion != 5:
        print("\n==============================")
        print("   ADMINISTRADOR DE USUARIOS")
        print("==============================")
        print("   1) Crear Usuario")
        print("   2) Eliminar Usuario")
        print("   3) Modificar Usuario")
        print("   4) Consultar Usuarios")
        print("   5) Salir")
        print("==============================")
        
        try:
            opcion = int(input("Selecciona una opción: "))
            print()

            if opcion == 1:
                print("=== Crear Usuario ===")
                primer_nombre = solicitar_texto("Primer Nombre: ", max_length=50)
                segundo_nombre = solicitar_texto_opcional("Segundo Nombre (opcional): ", max_length=50)
                primer_apellido = solicitar_texto("Primer Apellido: ", max_length=50)
                segundo_apellido = solicitar_texto_opcional("Segundo Apellido (opcional): ", max_length=50)
                correo = solicitar_texto("Correo: ", max_length=100)
                celular = solicitar_celular("Celular: ")
                tipo_documento = solicitar_texto("Tipo de Documento: ", max_length=10)
                id_identificacion = solicitar_entero("ID de Identificación: ")
                fecha_nacimiento = solicitar_fecha("Fecha de Nacimiento (YYYY-MM-DD): ")
                cargo = solicitar_texto("Cargo: ", max_length=50)
                contrasena = solicitar_texto("Contraseña: ", max_length=255)
                id_rol = solicitar_entero("ID del Rol: ")
                Usuario = solicitar_texto("Nombre de Usuario: ", max_length=50)
                
                resultado = administrar_usuarios.crear_usuario(
                    primer_nombre, segundo_nombre, primer_apellido, segundo_apellido,
                    correo, celular, tipo_documento, id_identificacion, fecha_nacimiento,
                    cargo, contrasena, id_rol, Usuario
                )
                if resultado > 0:
                    print("Usuario creado correctamente.")
                else:
                    print("No se pudo crear el usuario.")

            elif opcion == 2:
                print("=== Eliminar Usuario ===")
                id_usuario = solicitar_entero("ID del Usuario a eliminar: ", minimo=1)
                resultado = administrar_usuarios.eliminar_usuario_por_id(id_usuario)
                if resultado > 0:
                    print("Usuario eliminado correctamente.")
                else:
                    print("El Usuario no existe o no se pudo eliminar.")

            elif opcion == 3:
                print("=== Modificar Usuario ===")
                id_usuario = solicitar_entero("ID del usuario a modificar: ", minimo=1)
                usuario_actual = administrar_usuarios.buscar_usuario_por_id(id_usuario)

                if usuario_actual is None:
                    print("El Usuario no existe.")
                else:
                    encabezados = [
                        "id_usuario", "primer_nombre", "segundo_nombre", "primer_apellido", 
                        "segundo_apellido", "correo", "celular", "tipo_documento", 
                        "id_identificacion", "fecha_nacimiento", "cargo", "contrasena", 
                        "id_rol", "Usuario"
                    ]
                    print("Usuario actual:")
                    print(tabulate([usuario_actual], headers=encabezados, tablefmt="grid"))
                    print()
                    
                    primer_nombre = solicitar_texto(f"Nuevo Primer Nombre ({usuario_actual[1]}): ", max_length=50)
                    segundo_nombre = solicitar_texto_opcional(f"Nuevo Segundo Nombre (opcional) ({usuario_actual[2]}): ", max_length=50)
                    primer_apellido = solicitar_texto(f"Nuevo Primer Apellido ({usuario_actual[3]}): ", max_length=50)
                    segundo_apellido = solicitar_texto_opcional(f"Nuevo Segundo Apellido (opcional) ({usuario_actual[4]}): ", max_length=50)
                    correo = solicitar_texto(f"Nuevo Correo ({usuario_actual[5]}): ", max_length=100)
                    celular = solicitar_celular(f"Nuevo Celular ({usuario_actual[6]}): ")
                    tipo_documento = solicitar_texto(f"Nuevo Tipo de Documento ({usuario_actual[7]}): ", max_length=10)
                    id_identificacion = solicitar_entero(f"Nueva ID de Identificación ({usuario_actual[8]}): ")
                    fecha_nacimiento = solicitar_fecha(f"Nueva Fecha de Nacimiento ({usuario_actual[9]}): ")
                    cargo = solicitar_texto(f"Nuevo Cargo ({usuario_actual[10]}): ", max_length=50)
                    contrasena = solicitar_texto(f"Nueva Contraseña ({usuario_actual[11]}): ", max_length=255)
                    id_rol = solicitar_entero(f"Nuevo ID del Rol ({usuario_actual[12]}): ")
                    Usuario = solicitar_texto(f"Nuevo Nombre de Usuario ({usuario_actual[13]}): ", max_length=50)

                    resultado = administrar_usuarios.modificar_usuario(
                        id_usuario, primer_nombre, segundo_nombre, primer_apellido, segundo_apellido,
                        correo, celular, tipo_documento, id_identificacion, fecha_nacimiento,
                        cargo, contrasena, id_rol, Usuario
                    )
                    if resultado > 0:
                        print("Usuario modificado correctamente.")
                    else:
                        print("No se pudo modificar el Usuario.")

            elif opcion == 4:
                print("=== Lista de Usuarios ===")
                usuarios = administrar_usuarios.obtener_todos_los_usuarios()
                encabezados = [
                    "id_usuario", "primer_nombre", "segundo_nombre", "primer_apellido",
                    "segundo_apellido", "correo", "celular", "tipo_documento",
                    "id_identificacion", "fecha_nacimiento", "cargo", "contrasena",
                    "id_rol", "Usuario"
                ]

                if usuarios:
                    for i, usuario in enumerate(usuarios):
                        print(f"\n--- Usuario {i+1} ---")
                        datos_usuario = list(zip(encabezados, usuario))
                        print(tabulate(datos_usuario, headers=["Campo", "Valor"], tablefmt="plain"))
                else:
                    print("No hay Usuarios registrados.")

            elif opcion == 5:
                print("Saliendo del sistema...")
                
            else:
                print("Opción no válida. Intenta nuevamente.")

        except ValueError:
            print("Opción inválida. Ingresa un número entre 1 y 5.")
        finally:
            if opcion == 5:
                administrar_usuarios.cerrar_conexion()

if __name__ == "__main__":
    mostrar_menu()
