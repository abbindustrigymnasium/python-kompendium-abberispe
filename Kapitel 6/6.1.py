import requests
userInput = input("Ange ett heltal:")

if userInput.isdigit(): # om användarens input är ett heltal
    apiString = "http://77.238.56.27/examples/numinfo/?integer=" + str(userInput) # hämtar data för just det heltalet
    r = requests.get(apiString)
    data = r.json()
    returnString = str(userInput) + " är ett "
    if data["even"]: # om det är ett jämnt nummer
        returnString += "jämnt nummer. "
    else:
        returnString += "udda nummer. "
    
    if data["prime"]: # om numret är ett primtal
        returnString += "Numret är ett primtal. "
    else:
        returnString += "Numret är inte ett primtal. "

    returnString += "Numrets faktorer är "

    for factor in data["factors"]: # tittar på talets faktorer
        returnString += str(factor) + ", "

    returnString = returnString[:-2] # tar bort de sista två karaktärerna i stringen för att den kommer alltid sluta på ". "
    print(returnString)
else:
    print("Fel. Ange ett giltigt heltal.")


