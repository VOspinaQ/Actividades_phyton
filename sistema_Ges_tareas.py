"""Descripción del Ejercicio:
Desarrolla un sistema de gestión de tareas que permita al usuario añadir, ver, buscar, actualizar y eliminar tareas. Cada tarea debe tener un título, una descripción y un estado (pendiente o completada). El programa debe:

1. Permitir agregar nuevas tareas: Utiliza una clase Tarea para almacenar los detalles
2. de cada tarea y guarda los objetos en una lista.
3. Mostrar todas las tareas: Recorre la lista y muestra los detalles de cada tarea.
4. Buscar una tarea por título: Permite encontrar y mostrar información de una tarea específica.
5. Actualizar el estado de una tarea: Permite cambiar el estado de una tarea a "completada".
6. Eliminar una tarea por título: Permite remover una tarea de la lista.
7. Manejar posibles errores (como ingresar datos no válidos): Utiliza bloques try-except
para manejar errores en las entradas.
8. Permitir al usuario realizar otra operación o salir del programa: Un bucle while
permite repetir el proceso hasta que el usuario decida salir.



Desarrollo del Ejercicio:
"""
class Tarea:
    def __init__(self, titulo, descripcion, estado="pendiente"):
        self.titulo = titulo
        self.descripcion = descripcion
        self.estado = estado

    def __str__(self):
        return f"Título: {self.titulo}\nDescripción: {self.descripcion}\nEstado: {self.estado}"

tareas = []

def agregar_tarea():
    titulo = input("Introduce el título de la tarea: ")
    descripcion = input("Introduce la descripción de la tarea: ")
    nueva_tarea = Tarea(titulo, descripcion)
    tareas.append(nueva_tarea)
    print("Tarea añadida correctamente.")

def mostrar_tareas():
    if not tareas:
        print("No hay tareas para mostrar.")
    else:
        for idx, tarea in enumerate(tareas):
            print(f"\nTarea {idx + 1}")
            print(tarea)

def buscar_tarea():
    keyword = input("Introduce una palabra clave para buscar la tarea: ").strip().lower()

    print("\n--- Tareas Almacenadas ---")
    mostrar_tareas()  
    
    print(f"\nBuscando tareas que contengan la palabra clave: '{keyword}'")  
    
    resultados = []

    for tarea in tareas:
        titulo_procesado = tarea.titulo.lower().strip()
        descripcion_procesada = tarea.descripcion.lower().strip()
        
        print(f"Revisando tarea: '{titulo_procesado}' | Descripción: '{descripcion_procesada}'") 
        
        if keyword in titulo_procesado or keyword in descripcion_procesada:
            resultados.append(tarea)

    if resultados:
        print("\nTareas encontradas:")
        for tarea in resultados:
            print(tarea)
    else:
        print("No se encontraron tareas que coincidan con la búsqueda.")

def actualizar_estado():
    titulo = input("Introduce el título de la tarea que deseas actualizar: ").strip().lower()
    for tarea in tareas:
        if tarea.titulo.lower().strip() == titulo:
            tarea.estado = "completada"
            print("El estado de la tarea ha sido actualizado a 'completada'.")
            return
    print("Tarea no encontrada.")

def actualizar_descripcion():
    titulo = input("Introduce el título de la tarea que deseas actualizar: ").strip().lower()
    for tarea in tareas:
        if tarea.titulo.lower().strip() == titulo:
            nueva_descripcion = input("Introduce la nueva descripción: ").strip()
            tarea.descripcion = nueva_descripcion
            print("La descripción de la tarea ha sido actualizada.")
            return
    print("Tarea no encontrada.")

def eliminar_tarea():
    titulo = input("Introduce el título de la tarea que deseas eliminar: ").strip().lower()
    for tarea in tareas:
        if tarea.titulo.lower().strip() == titulo:
            tareas.remove(tarea)
            print("Tarea eliminada correctamente.")
            return
    print("Tarea no encontrada.")

def filtrar_tareas_por_estado():
    print("\nSelecciona el estado de las tareas que deseas ver:")
    print("1. Pendiente")
    print("2. Completada")

    opciones_estado = {
        "1": "pendiente",
        "2": "completada"
    }

    seleccion = input("Introduce el número de la opción deseada: ").strip()

    if seleccion not in opciones_estado:
        print("Opción no válida. Debe seleccionar 1 o 2.")
        return

    estado = opciones_estado[seleccion]

    tareas_filtradas = [tarea for tarea in tareas if tarea.estado == estado]

    if tareas_filtradas:
        print(f"\nTareas encontradas con el estado '{estado}':")
        for tarea in tareas_filtradas:
            print(tarea)
    else:
        print(f"No hay tareas con el estado '{estado}'.")



def mostrar_menu():
    print("\nMenú:")
    print("1. Añadir Tarea")
    print("2. Mostrar Tareas")
    print("3. Buscar Tarea por Palabra Clave")
    print("4. Actualizar Estado de Tarea")
    print("5. Actualizar Descripción de Tarea")
    print("6. Eliminar Tarea")
    print("7. Filtrar Tareas por Estado")
    print("8. Salir")

def ejecutar_operacion(opcion):
    try:
        if opcion == "1":
            agregar_tarea()
        elif opcion == "2":
            mostrar_tareas()
        elif opcion == "3":
            buscar_tarea()
        elif opcion == "4":
            actualizar_estado()
        elif opcion == "5":
            actualizar_descripcion()
        elif opcion == "6":
            eliminar_tarea()
        elif opcion == "7":
            filtrar_tareas_por_estado()
        elif opcion == "8":
            print("Saliendo del programa.")
            return False
        else:
            print("Opción no válida. Inténtalo de nuevo.")
    except Exception as e:
        print(f"Error: {e}")
    return True

def main():
    continuar = True
    while continuar:
        mostrar_menu()
        opcion = input("Selecciona una opción: ")
        continuar = ejecutar_operacion(opcion)

if __name__ == "__main__":
    main()

