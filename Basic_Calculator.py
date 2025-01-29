#Import time
import time

# Create the variables
num1 = 0
num2 = 0
salir = "N"

# Create the Def 
def suma(num1,num2):
    total = num1 + num2
    print(f"La suma entre {num1} + {num2} = {total}")

def resta(num1,num2):
    total = num1 - num2
    print(f"La resta entre {num1} - {num2} = {total}")

def mult(num1,num2):
    total = num1 * num2
    print(f"La multiplicacion entre {num1} * {num2} = {total}")

def div(num1,num2):
    if num2 == 0:
        print("No se puede dividir entre 0")
    else:
        total = num1 / num2
        print(f"La division entre {num1} / {num2} = {total}")

# Create the bucle
while salir == "N":
    while True:
        try:
            num1 = float(input("First number: "))
            num2 = float(input("Second number: "))
            break
        except ValueError:
            print("Introduce numeros validos")
    #---Men----#
    while True:
        print("----Menu----")
        print("1: Sumar (" ,num1, "+ " ,num2, ")")
        print("2: Restar (" ,num1, "- " ,num2, ")")
        print("3: Multiplicar (" ,num1, "* " ,num2, ")")
        print("4: Dividir (" ,num1, "/ " ,num2, ")")
        print("5: Cambiar numeros")
        print("6: Salir")
        # Variable option
        option = str(input("Introduce una opcion: ")).lower()
        if option == "sumar" or option == "1":
            suma(num1,num2)
        elif option == "restar" or option == "2":
            resta(num1,num2)
        elif option == "multiplicar" or option == "3":
            mult(num1,num2)
        elif option == "dividir" or option == "4":
            div(num1,num2)
        elif option == "Cambiar numeros" or option == "5":
            break
        elif option == "salir" or option == "6":
            salir = "Y"
        else:
            print("Opcion Incorrecta...")    
        time.sleep(2)
    
    