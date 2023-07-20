# Libraries
from math import sqrt

# Lines
t1 = "--------------------------------------------------------------"
t2a = "---------------------------------------------------------------------"
t2b = "-----------------------------------------------------------------"

# Menu
m1 = "| 1. Italiano | 2. English | 3. Français (En arrive a breve) |"
m2a = "| 1. Addizione | 2. Sottrazione | 3. Moltiplicazione | 4. Divisione |"
m2b = "| 1. Addition | 2. Subtraction | 3. Multiplication | 4. Division |"

# Phrases
f1 = "Benvenuto nel programma di calcolazioni: 'Calcolatutto'. Seleziona la lingua"
f2a = "Ciao! Hai scelto Italiano come lingua dell'applicativo. Seleziona l'operazione: "
f2b = "Good Morning! You select English which language of application. Select the operation: "

# Languages
FR = "Vous avez sélectionné 'Français' mais la langue n'est pas disponible actuellement. Vous serez redirigé vers le menu principal"
EN = "You select English"
IT = "Hai selezionato Italiano"

print(t1)
print(m1)
print(t1)

while True:
    action = input("Welcome to the calculation program: 'Calcolatutto'. Select language: ")

    if action == "1":
        print(IT)
        print(t2a)
        print(m2a)
        print(t2a)
        operationi = input(f2a)

        if operationi == "1":
            print("\nHai selezionato Addizione\n")
            a = float(input("Inserisci il primo numero: "))
            b = float(input("Inserisci il secondo numero: "))
            print("Il risultato è: ", str(a + b))
            new_action1 = input("Vuoi continuare?")
            if new_action1 == "S" or new_action == "s":
                print("Sto tornando al menù principale!\n")
                continue
                print("Select the language with the previous list")
            else:
                print("A presto!\n")
                break
        elif operationi == "2":
            print("\nHai selezionato la sottrazione\n")
            a = float(input("Inserisci il primo numero: "))
            b = float(input("Inserisci il secondo numero: "))
            print("Il risultato è: ", str(a - b))
            new_action1 = input("Vuoi continuare?")
            if new_action1 == "S" or new_action == "s":
                print("Sto tornando al menù principale!\n")
                continue
                print("Select the language with the previous list")
            else:
                print("A presto!\n")
                break
        elif operationi == "3":
            print("\nHai selezionato la Moltiplicazione\n")
            a = float(input("Inserisci il primo numero: "))
            b = float(input("Inserisci il primo numero: "))
            print("Il risultato è: ", str(a * b))
            new_action1 = input("Vuoi continuare?")
            if new_action1 == "S" or new_action == "s":
                print("Sto tornando al menù principale!\n")
                continue
                print("Select the language with the previous list")
            else:
                print("A presto!\n")
                break
        elif operationi == "4":
            print("\nHai selezionato la Divisione\n")
            a = float(input("Inserisci il primo numero: "))
            b = float(input("Inserisci il primo numero: "))
            print("Il risultato è: ", str(a / b))

            new_action1 = input("Vuoi continuare?")
            if new_action1 == "S" or new_action == "s":
                print("Sto tornando al menù principale!\n")
                continue
                print("Select the language with the previous list")
            else:
                print("A presto!\n")
                break
    elif action == "2":
        print(EN)
        print(m2b)
        operation = input("Select Operation: ")

        if operation == "1":
            print("\nYou have chosen Addition\n")
            a = float(input("Enter the first number: "))
            b = float(input("Enter the second number: "))
            print("The result of addition is: ", str(a + b))
            new_action = input("\nDo you want to continue using the application? (Y/N) ")
            if new_action == "Y" or new_action == "y":
                print("Returning to the main menu!\n")
                continue
            else:
                print("Goodbye!\n")
                break
        elif operation == "2":
            print("\nYou have chosen Subtraction\n")
            a = float(input("Enter the first number: "))
            b = float(input("Enter the second number: "))
            print("The result of Subtraction is: ", str(a - b))
            new_action = input("\nDo you want to continue using the application? (Y/N) ")
            if new_action == "Y" or new_action == "y":
                print("Returning to the main menu!\n")
                continue
            else:
                print("Goodbye!\n")
                break
        elif operation == "3":
            print("\nYou have chosen Multiplication\n")
            a = float(input("Enter the first number: "))
            b = float(input("Enter the second number: "))
            print("The result of multiplication is: ", str(a * b))
            new_action = input("\nDo you want to continue using the application? (Y/N) ")
            if new_action == "Y" or new_action == "y":
                print("Returning to the main menu!\n")
                continue
            else:
                print("Goodbye!\n")
                break
        elif operation == "4":
            print("\nYou have chosen Division\n")
            a = float(input("Enter the first number: "))
            b = float(input("Enter the second number: "))
            print("The result of Division is: ", str(a / b))

            new_action = input("\nDo you want to continue using the application? (Y/N) ")
            if new_action == "Y" or new_action == "y":
                print("Returning to the main menu!\n")
                continue
            else:
                print("Goodbye!\n")
                break
    elif action == "3":
        print(FR)