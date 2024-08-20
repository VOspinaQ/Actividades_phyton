
"""Ejercicio:
Crea una calculadora básica que realice las siguientes operaciones: suma, resta, multiplicación y división.
El programa debe:

1.Mostrar un menú con las opciones de operaciones: El menú permite al usuario elegir qué operación quiere realizar.
2.Pedir al usuario que elija una operación: Se usa input para recibir la opción elegida.
3.Solicitar dos números: Los números se ingresan como float para permitir operaciones con decimales.
4.Realizar la operación elegida y mostrar el resultado: Se usan funciones para cada operación.
5.Permitir al usuario realizar otra operación o salir del programa: Un bucle while permite repetir el proceso
hasta que el usuario decida salir.


Desarrollo:"""

def menu():
    print("Selecciona una operación: (1 al 5)")
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")
    print("5. Salir")

def sumar(x, y):
    return x + y

def restar(x, y):
    return x - y

def multiplicar(x, y):
    return x * y

def dividir(x, y):
    if y != 0:
        return x / y 
    else: 
        return "Error: División por cero"

def calcu():
    while True:
        menu()
        numero = input("Ingrese su opción (1, 2, 3, 4, 5): ")

        if numero == '5':
            print("Saliendo...")
            break

        if numero in ['1', '2', '3', '4']:
            num1 = float(input("Ingresa el primer número: "))
            num2 = float(input("Ingresa el segundo número: "))

            if numero == '1':
                print(f"El resultado es: {sumar(num1, num2)}")
            elif numero == '2':
                print(f"El resultado es: {restar(num1, num2)}")
            elif numero == '3':
                print(f"El resultado es: {multiplicar(num1, num2)}")
            elif numero == '4':
                print(f"El resultado es: {dividir(num1, num2)}")
        else:
            print("Opción inválida. Inténtalo de nuevo.")

if __name__ == "__main__":
    calcu()
