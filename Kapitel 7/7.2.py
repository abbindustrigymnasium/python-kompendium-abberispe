import random

print("Guess the random number!")
randomNum = random.randint(0, 99) # skapar random nummer

while True:
    userGuess = int(input("Your guess: ")) # användaren anger gissning
    if (userGuess > randomNum): # tittar om gissningen är större än numret
        print("LOWER")
        continue # fortsätter med loopen
    elif (userGuess < randomNum):
        print("HIGHER")
        continue
    elif (userGuess == randomNum): # tittar om gissningen är samma som numret
        print("You guessed right! The random number was " + str(randomNum))
        break # bryter loopen