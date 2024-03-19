import module.configuration

def unlockProcedure():
    print(f"Please provide program password: ")

    userInput = input()

    if userInput.strip() == module.configuration.password:
        return True
    
    return False
            
def isTextValid(text : str) -> bool:
    try:
        for i in text:
            if i.lower() in "йцукенгшщзхъфывапролджэячсмитьбю":
                return False
    except Exception as e:
        return False
    
    return True

def userInputValidation(intext : int, lower : int, upper : int):
    if intext >= lower and intext <= upper:
        return True
    
    return False