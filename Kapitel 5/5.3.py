nordic = ["danmark", "finland", "island", "norge", "sverige"]
britain = ["england", "nordirland", "skottland", "wales"]

userInput = input("Name a country!").lower() # användarens input till små bokstäver för att kunna jämföra bättre

if userInput in nordic: # om användarens input finns i arrayen nordic
    print("That is a nordic country!") 
elif userInput in britain: # om användarens input finns i arrayen britain
    print("That is a british country!")
else:
    print("That is not a nordic or a british country!")