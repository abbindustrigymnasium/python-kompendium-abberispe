import math
import sys


def line(bool):
    if (bool == True):
        print("*******************************") # skapar denna typ av linje vid bool = True
    else:
        print("-------------------------------")

def header(string): # skapar en header
    length = len(string) # tittar på längden på den angivna stringen
    spaces = math.ceil((30 - length) / 2) # räknar ut hur många mellanslag det ska vara på var sida av titeln. Detta för att centrera titeln
    printString = "|"
    iterator = 1 
    while iterator < spaces: # använder iterator för att kunna skapa endast så många spaces som behövs
        printString += " "
        iterator += 1
    printString += string # lägger dit stringen som användaren angav
    while len(printString) < 30: # lägger till de sista mellanslagen
        printString += " "
    printString += "|"
    print(printString)

def echo(string): # skriver ut vad som helst
    print("| " + string)

def prompt(string): # frågar efter användar input
    return input("| " + string)

    

