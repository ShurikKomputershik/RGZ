from module.utilities import userInputValidation
from module.atbash import atbash_decode, atbash_encode
from module.gronsfeld import gronsfeld_encode, gronsfeld_decode, is_valid_gronsfeld_key
from module.viginere import vigenere_encode, vigenere_decode, is_valid_vigenere_key

currentText = ""

def helloMessage():
    print("---------------------------------------------")
    print("Welcome to Origo!")

    programMainLoop()


def changeInputMenu():
    global currentText

    while True:
        print("| Change input | Menu:")
        print("| 1. From file")
        print("| 2. From console")

        try:
            userInput = int(input())
        except ValueError:
            print("No such variant")
            continue

        if userInputValidation(userInput, 1, 2):
            if userInput == 1:
                print("Provide filename:")
                filename = input().strip()

                try:
                    with open(filename, 'r') as fileHandler:
                        currentText = fileHandler.read()
                except FileNotFoundError:
                    print("File not found!")
                    continue
                except OSError as e:
                    print(f"Error opening the file: {e}")
                    continue

            elif userInput == 2:
                print("Enter text:")
                currentText = input()

            return  # Выход из функции changeInputMenu()
        else:
            print("No such variant")

        

def cypherMenu():
    global currentText

    while True:
        print("---------------------------------------------")
        print("Cypher Menu:")

        print("Select a cipher algorithm:")
        print("1. Atbash Cipher")
        print("2. Gronsfeld Cipher")
        print("3. Vigenere Cipher")
        print("4. Back to main menu")

        try:
            userChoice = int(input())
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

        if userChoice == 1:
            # Atbash Cipher
            currentText = atbash_encode(currentText)
            print("Text encrypted using Atbash Cipher:")
            print(currentText[:30] + '...' if len(currentText) > 30 else currentText)

        elif userChoice == 2:
            # Gronsfeld Cipher
            print("Enter Gronsfeld key:")
            key = input()
            if is_valid_gronsfeld_key(key):
                currentText = gronsfeld_encode(currentText, key)
                print("Text encrypted using Gronsfeld Cipher:")
                print(currentText[:30] + '...' if len(currentText) > 30 else currentText)
            else:
                print("Invalid Gronsfeld key.")

        elif userChoice == 3:
            # Vigenere Cipher
            print("Enter Vigenere key:")
            key = input()
            if is_valid_vigenere_key(key):
                currentText = vigenere_encode(currentText, key)
                print("Text encrypted using Vigenere Cipher:")
                print(currentText[:30] + '...' if len(currentText) > 30 else currentText)
            else:
                print("Invalid Vigenere key.")

        elif userChoice == 4:
            return

        else:
            print("Invalid input. Please select a valid option.")

        # Возвращение в цикл меню шифрования
def decypherMenu():
    global currentText

    while True:
        print("---------------------------------------------")
        print("Decypher Menu:")

        print("Select a cipher algorithm for decryption:")
        print("1. Atbash Cipher")
        print("2. Gronsfeld Cipher")
        print("3. Vigenere Cipher")
        print("4. Back to main menu")

        try:
            userChoice = int(input())
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

        if userChoice == 1:
            # Atbash Cipher
            currentText = atbash_decode(currentText)
            print("Text decrypted using Atbash Cipher:")
            print(currentText[:30] + '...' if len(currentText) > 30 else currentText)

        elif userChoice == 2:
            # Gronsfeld Cipher
            print("Enter Gronsfeld key:")
            key = input()
            if is_valid_gronsfeld_key(key):
                currentText = gronsfeld_decode(currentText, key)
                print("Text decrypted using Gronsfeld Cipher:")
                print(currentText[:30] + '...' if len(currentText) > 30 else currentText)
            else:
                print("Invalid Gronsfeld key.")

        elif userChoice == 3:
            # Vigenere Cipher
            print("Enter Vigenere key:")
            key = input()
            if is_valid_vigenere_key(key):
                currentText = vigenere_decode(currentText, key)
                print("Text decrypted using Vigenere Cipher:")
                print(currentText[:30] + '...' if len(currentText) > 30 else currentText)
            else:
                print("Invalid Vigenere key.")

        elif userChoice == 4:
            return

        else:
            print("Invalid input. Please select a valid option.")

        # Возвращение в цикл меню дешифрования

def saveCurrentText():
    global currentText

    print("---------------------------------------------")
    print("Save Current Text:")
    print("1. Print to console")
    print("2. Save to a file")

    try:
        userChoice = int(input())
    except ValueError:
        print("Invalid input. Please enter a number.")
        return

    if userChoice == 1:
        print("Current text:")
        print(currentText)
    elif userChoice == 2:
        filename = input("Enter filename to save: ")
        try:
            with open(filename, 'w') as file:
                file.write(currentText)
                print("Text saved to", filename)
        except OSError as e:
            print("Error saving the file:", e)
    else:
        print("Invalid input. Please select a valid option.")

def programMainLoop():
    global currentText
    while True:
        print("---------------------------------------------")
        current_display = currentText[:30] + ('...' if len(currentText) > 30 else '') if currentText else '      (nothing!)'
        print(f"Current input buffer: {current_display}\n")

        print("Menu:")
        print("1. Change input")
        print("2. Cypher")
        print("3. Decypher")
        print("4. Save input buffer")
        print("5. Exit")

        try:
            userInput = int(input())
        except:
            print("No such variant")
            continue

        if userInput > 0 and userInput < 6:
            if userInput == 1:
                changeInputMenu()
            elif userInput == 2:
                cypherMenu()
            elif userInput == 3:
                decypherMenu()
            elif userInput == 4:
                saveCurrentText()
            elif userInput == 5:
                return SystemExit
        else:
            print("No such variant")
