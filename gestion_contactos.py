"""Ejercicio:
Crea un programa para gestionar una lista de contactos. Cada contacto debe tener un nombre
y un número de teléfono. El programa debe:

1. Permitir agregar nuevos contactos: Utiliza una clase Contacto y almacena objetos en una lista.
2. Mostrar todos los contactos: Recorre la lista y muestra los detalles de cada contacto.
3. Buscar un contacto por nombre: Permite encontrar y mostrar información de un contacto específico.
4. Eliminar un contacto por nombre: Permite remover un contacto de la lista.
5. Permitir al usuario realizar otra operación o salir del programa: Un bucle while permite
repetir el proceso hasta que el usuario decida salir.


Desarrollo:"""

class Contacto:
    def __init__(self, nombre, telefono):
        self.nombre = nombre
        self.telefono = telefono

    def __str__(self):
        return f"Nombre: {self.nombre}, Teléfono: {self.telefono}"


class ListaContactos:
    def __init__(self):
        self.contactos = []

    def agregar_contacto(self, nombre, telefono):
        nuevo_contacto = Contacto(nombre, telefono)
        self.contactos.append(nuevo_contacto)
        print(f"Contacto {nombre} agregado exitosamente.\n")

    def mostrar_contactos(self):
        if not self.contactos:
            print("La lista de contactos está vacía.\n")
        else:
            print("Lista de contactos:")
            for contacto in self.contactos:
                print(contacto)
            print()  # Añadir un salto de línea para separar secciones

    def buscar_contacto(self, nombre):
        for contacto in self.contactos:
            if contacto.nombre.lower() == nombre.lower():
                print(f"Contacto encontrado: {contacto}\n")
                return
        print(f"Contacto con nombre '{nombre}' no encontrado.\n")

    def eliminar_contacto(self, nombre):
        for contacto in self.contactos:
            if contacto.nombre.lower() == nombre.lower():
                self.contactos.remove(contacto)
                print(f"Contacto {nombre} eliminado exitosamente.\n")
                return
        print(f"Contacto con nombre '{nombre}' no encontrado.\n")


def menu():
    print("Seleccione una operación:")
    print("1. Agregar nuevo contacto")
    print("2. Mostrar todos los contactos")
    print("3. Buscar un contacto por nombre")
    print("4. Eliminar un contacto por nombre")
    print("5. Salir")


def main():
    lista_contactos = ListaContactos()

    while True:
        menu()
        opcion = input("Ingrese su opción (1-5): ")

        if opcion == '1':
            nombre = input("Ingrese el nombre del contacto: ")
            telefono = input("Ingrese el número de teléfono del contacto: ")
            lista_contactos.agregar_contacto(nombre, telefono)
        elif opcion == '2':
            lista_contactos.mostrar_contactos()
        elif opcion == '3':
            nombre = input("Ingrese el nombre del contacto a buscar: ")
            lista_contactos.buscar_contacto(nombre)
        elif opcion == '4':
            nombre = input("Ingrese el nombre del contacto a eliminar: ")
            lista_contactos.eliminar_contacto(nombre)
        elif opcion == '5':
            print("Saliendo del programa...")
            break
        else:
            print("Opción inválida. Inténtalo de nuevo.\n")


if __name__ == "__main__":
    main()
