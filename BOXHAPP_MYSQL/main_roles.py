from roles import Roles
from tabulate import tabulate

# Instancia para gestionar Roles
administrar_roles = Roles()

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
            
def solicitar_texto(mensaje):
    while True:
        texto = input(mensaje).strip()
        if texto == "":
            print("Este campo no puede estar vacío.")
        else:
            return texto[:45]

def mostrar_menu():
    opcion = 0
    while opcion != 5:
        print("\n==============================")
        print("   ADMINISTRADOR DE ROLES")
        print("==============================")
        print("  1) Crea Rol")
        print("  2) Eliminar Rol")
        print("  3) Modificar Rol")
        print("  4) Consultar rol")
        print("  5) Salir")
        print("==============================")
        
        try:
            opcion = int(input("Selecciona una opción: "))
            print()

            if opcion == 1:
                print("=== Crear Rol ===")
                nombre = solicitar_texto("Nombre del Rol: ")
                descripcion = solicitar_texto("Descripción: ")
                
                resultado = administrar_roles.crear_rol(nombre, descripcion)
                if resultado > 0:
                    print("Rol creado correctamente.")
                else:
                    print("No se pudo crear el rol.")

            elif opcion == 2:
                print("=== Eliminar Rol ===")
                id_rol = solicitar_entero("ID del Rol a eliminar: ", minimo=1)
                resultado = administrar_roles.eliminar_rol_por_id(id_rol)
                if resultado > 0:
                    print("Rol eliminado correctamente.")
                else:
                    print("El Rol no existe o no se pudo eliminar.")

            elif opcion == 3:
                print("=== Modificar Rol ===")
                id_rol = solicitar_entero("ID del rol a modificar: ", minimo=1)
                rol = administrar_roles.buscar_rol_por_id(id_rol)

                if rol is None:
                    print("El Rol no existe.")
                else:
                    encabezados = ["id_rol", "Nombre_rol", "Descripción"]
                    print("Rol actual:")
                    print(tabulate([rol], headers=encabezados, tablefmt="grid"))
                    print()

                    nombre = solicitar_texto("Nuevo nombre: ")
                    descripcion = solicitar_texto("Nueva descripción: ")

                    resultado = administrar_roles.modificar_rol(id_rol, nombre, descripcion)
                    if resultado > 0:
                        print("Rol modificado correctamente.")
                    else:
                        print("No se pudo modificar el Rol.")

            elif opcion == 4:
                print("=== Lista de Roles ===")
                Roles = administrar_roles.obtener_todos_los_roles()

                if Roles:
                    encabezados = ["id_rol", "Nombre_rol", "Descripción"]
                    print(tabulate(Roles, headers=encabezados, tablefmt="grid"))
                else:
                    print("No hay Roles registrados.")

            elif opcion == 5:
                print("Saliendo del sistema...")
                
            else:
                print("Opción no válida. Intenta nuevamente.")

        except ValueError:
            print("Opción inválida. Ingresa un número entre 1 y 5.")
            
if __name__ == "__main__":
    mostrar_menu()