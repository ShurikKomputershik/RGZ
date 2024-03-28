def unlockProcedure():
    print("Please provide program password: ")

    userInput = int(input())  

    if userInput == 1234:  
        return True
    
    return False

def userInputValidation(intext, lower, upper):
    if intext >= lower and intext <= upper:
        return True
    
    return False