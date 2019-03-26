class person: # skapar en klass för ett personobject med namn, kön, hårfärg och ögonfärg som argument
  def __init__(self, name, gender, haircolor, eyecolor):
    self.name = name
    self.gender = gender
    self.haircolor = haircolor
    self.eyecolor = eyecolor                                                                                                                                                                                                                                                                                                       

genderInput = input("Gender?")
hairColorInput = input("Haircolor?")
eyeColorInput = input("Eyecolor?") # promptar användaren

danielradcliffe = person("Daniel Radcliffe", "man", "brown", "brown")
rupertgrint = person("Rupert Grint", "man", "red", "blue")
emmawatson = person("Emma Watson", "woman", "brown", "brown")
selenagomez = person("Selena Gomez", "woman", "brown", "brown") # använder klassen för att skapa personer med egenskaper

listOfPersons = [danielradcliffe, rupertgrint, emmawatson, selenagomez] # lägger in alla nya personer i en lista

found = False

for person in listOfPersons: # för varje person-objekt i listan
    if person.gender == genderInput and person.haircolor == hairColorInput and person.eyecolor == eyeColorInput: # om en person matchar användarens input
        print(person.name)
        found = True

if found == False:
    print("Could not find any match.")