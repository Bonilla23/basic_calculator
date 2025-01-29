# Create the variables
num1 = 0
num2 = 0
salir = "Y"

# Ask the numbers
num1 = int(input("First number: "))
num2 = int(input("Second number: "))

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
    