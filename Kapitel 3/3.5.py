male = [
"Erik",
"Lars",
"Karl",
"Anders",
"Johan"
]
female = [
"Maria",
"Anna",
"Margareta",
"Elisabeth",
"Eva"
]

name = input("Vilket namn ska tas bort?")

male.remove(name) #remove kan ta bort ett item från listan utan ett index, bara värdet.
female.remove(name)

print(male, female)