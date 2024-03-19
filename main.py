from module.utilities import unlockProcedure
from module.programLoop import helloMessage

def main():
    unlockState = unlockProcedure()

    if unlockState == True:
        print("Success!")
        helloMessage()
    else:
        print("Unlock procedure went wrong! Invalid password")
        return SystemExit

if __name__ == "__main__":
    main()