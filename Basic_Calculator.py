#Import time
import time

# Create the variables
num1 = 0
num2 = 0
salir = "N"

# Ask the numbers
while True:
    try:
        num1 = float(input("First number: "))
        num2 = float(input("Second number: "))
        break
    except ValueError:
        print("Introduce numeros validos")

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
    #---Menu----#
    print("----Menu----")
    print("Sumar (" ,num1, "+ " ,num2, ")")
    print("Restar (" ,num1, "- " ,num2, ")")
    print("Multiplicar (" ,num1, "* " ,num2, ")")
    print("Dividir (" ,num1, "/ " ,num2, ")")
    print("Salir")
    # Variable option
    option = str(input("Introduce una opcion: "))
    if option.lower() == "sumar":
        suma(num1,num2)
        time.sleep(1)
    elif option.lower() == "restar":
        resta(num1,num2)
        time.sleep(1)
    elif option.lower() == "multiplicar":
        mult(num1,num2)
        time.sleep(1)
    elif option.lower() == "dividir":
        div(num1,num2)
        time.sleep(1)
    elif option.lower() == "salir":
        salir = "Y"
        
        