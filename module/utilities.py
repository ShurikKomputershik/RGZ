import module.configuration

def unlockProcedure():
    print(f"Please provide program password: ")

    userInput = input()

    if userInput.strip() == module.configuration.password:
        return True
    
    return False

def userInputValidation(intext : int, lower : int, upper : int):
    if intext >= lower and intext <= upper:
        return True
    
    return False