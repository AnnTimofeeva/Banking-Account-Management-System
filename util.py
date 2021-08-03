import os

class Util:

    @staticmethod
    def clear_screen():
        os.system('cls')

    @staticmethod
    def  press_return(message):
        print (message)
        input()        