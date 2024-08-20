"""Ejercicio:
Crea un sistema de inventario para una tienda. El programa debe:

1. Permitir agregar nuevos productos (nombre, cantidad, precio): Utiliza una clase Producto
y almacena objetos en una lista.
2. Mostrar todos los productos: Recorre la lista y muestra los detalles de cada producto.
3. Buscar un producto por nombre: Permite encontrar y mostrar información de un producto específico.
4. Actualizar la cantidad de un producto: Permite modificar la cantidad de un producto existente.
5. Eliminar un producto: Permite remover un producto de la lista.
6. Manejar posibles errores (como ingresar datos no válidos): Utiliza bloques
try-except para manejar errores en las entradas.
7. Permitir al usuario realizar otra operación o salir del programa: Un bucle while
permite repetir el proceso hasta que el usuario decida salir.


Desarrollo:"""

class Producto:
    def __init__(self, nombre, cantidad, precio):
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio

    def __str__(self):
        return f"Nombre: {self.nombre}, Cantidad: {self.cantidad}, Precio: ${self.precio:.2f}"


class Inventario:
    def __init__(self):
        self.productos = []

    def agregar_producto(self):
        try:
            nombre = input("Ingrese el nombre del producto: ")
            cantidad = int(input("Ingrese la cantidad del producto: "))
            precio = float(input("Ingrese el precio del producto: "))
            nuevo_producto = Producto(nombre, cantidad, precio)
            self.productos.append(nuevo_producto)
            print(f"Producto '{nombre}' agregado exitosamente.\n")
        except ValueError:
            print("Error: Por favor ingrese una cantidad o precio válido.\n")

    def mostrar_productos(self):
        if not self.productos:
            print("El inventario está vacío.\n")
        else:
            print("Inventario de productos:")
            for producto in self.productos:
                print(producto)
            print()

    def buscar_producto(self):
        nombre = input("Ingrese el nombre del producto a buscar: ").lower()
        encontrados = [producto for producto in self.productos if nombre in producto.nombre.lower()]

        if encontrados:
            print("Productos encontrados:")
            for producto in encontrados:
                print(producto)
            print()
        else:
            print(f"No se encontraron productos que coincidan con '{nombre}'.\n")

    def actualizar_cantidad(self):
        nombre = input("Ingrese el nombre del producto a actualizar: ").lower()
        encontrados = [producto for producto in self.productos if nombre in producto.nombre.lower()]

        if encontrados:
            if len(encontrados) == 1:
                producto = encontrados[0]
                try:
                    nueva_cantidad = int(input(f"Ingrese la nueva cantidad para {producto.nombre}: "))
                    producto.cantidad = nueva_cantidad
                    print(f"Cantidad de '{producto.nombre}' actualizada a {nueva_cantidad}.\n")
                except ValueError:
                    print("Error: Por favor ingrese una cantidad válida.\n")
            else:
                print("Se encontraron varios productos:")
                for i, producto in enumerate(encontrados, start=1):
                    print(f"{i}. {producto}")
                index = int(input("Seleccione el número del producto que desea actualizar: ")) - 1
                try:
                    nueva_cantidad = int(input(f"Ingrese la nueva cantidad para {encontrados[index].nombre}: "))
                    encontrados[index].cantidad = nueva_cantidad
                    print(f"Cantidad de '{encontrados[index].nombre}' actualizada a {nueva_cantidad}.\n")
                except (ValueError, IndexError):
                    print("Error: Opción no válida o cantidad inválida.\n")
        else:
            print(f"No se encontraron productos que coincidan con '{nombre}'.\n")

    def eliminar_producto(self):
        nombre = input("Ingrese el nombre del producto a eliminar: ").lower()
        encontrados = [producto for producto in self.productos if nombre in producto.nombre.lower()]

        if encontrados:
            if len(encontrados) == 1:
                producto = encontrados[0]
                self.productos.remove(producto)
                print(f"Producto '{producto.nombre}' eliminado exitosamente.\n")
            else:
                print("Se encontraron varios productos:")
                for i, producto in enumerate(encontrados, start=1):
                    print(f"{i}. {producto}")
                index = int(input("Seleccione el número del producto que desea eliminar: ")) - 1
                try:
                    self.productos.remove(encontrados[index])
                    print(f"Producto '{encontrados[index].nombre}' eliminado exitosamente.\n")
                except (IndexError, ValueError):
                    print("Error: Opción no válida.\n")
        else:
            print(f"No se encontraron productos que coincidan con '{nombre}'.\n")

    def menu(self):
        print("Seleccione una operación:")
        print("1. Agregar nuevo producto")
        print("2. Mostrar todos los productos")
        print("3. Buscar un producto por nombre")
        print("4. Actualizar la cantidad de un producto")
        print("5. Eliminar un producto")
        print("6. Salir")

    def ejecutar(self):
        while True:
            self.menu()
            opcion = input("Ingrese su opción (1-6): ")

            if opcion == '1':
                self.agregar_producto()
            elif opcion == '2':
                self.mostrar_productos()
            elif opcion == '3':
                self.buscar_producto()
            elif opcion == '4':
                self.actualizar_cantidad()
            elif opcion == '5':
                self.eliminar_producto()
            elif opcion == '6':
                print("Saliendo del programa...")
                break
            else:
                print("Opción inválida. Inténtalo de nuevo.\n")


if __name__ == "__main__":
    inventario = Inventario()
    inventario.ejecutar()
