# Create the variables
num1 = 0
num2 = 0
salir = "Y"

# Ask the numbers
num1 = int(input("First number: "))
num2 = int(input("Second number: "))

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
    total = num1 / num2
    print(f"La division entre {num1} / {num2} = {total}")

# Create the bucle
while salir == "Y":
    #---Menu----#
    print("----Menu----")
    print("Sumar (" ,num1, "+ " ,num2, ")")
    print("Restar (" ,num1, "- " ,num2, ")")
    print("Multiplicar (" ,num1, "* " ,num2, ")")
    print("Dividir (" ,num1, "/ " ,num2, ")")
    # Variable option
    option = str(input("Introduce una opcion: "))
    if option.lower() == "sumar":
        print(suma(num1,num2))
    elif option.lower() == "restar":
        print(resta(num1,num2))
    elif option.lower() == "multiplicar":
        print(mult(num1,num2))
    elif option.lower() == "dividir":
        print(div(num1,num2))