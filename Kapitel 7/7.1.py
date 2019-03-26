userInput = int(input("Ange multiplikationstabell")) # anger multiplikationstabell
iterator = 0

while True: # startar loop
    iterator += 1 # använder iterator för att bara köra loopen tre gånger åt gången
    print(iterator * userInput)
    if (iterator % 3 == 0): # tittar om loopen har körts tre gånger
        userInputContinue = input("Fortsätt? ")
        if (userInputContinue == "ja"):
            continue # fortsätter om användaren vill fortsätta
        else:
            break # annars bryter vi loopen