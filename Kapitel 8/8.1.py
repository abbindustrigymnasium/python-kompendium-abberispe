userInput = str(input("Ange distans: ")) # frågor om en distans

def determineMileOrKilometer(str):
    index = len(str) - 1 
    if (str[index] == "s"): # tittar på om sista bokstaven är s. då betyder det att användaren vill konvertera från miles till km
        number = ""
        iterator = 0
        while True:
            if (str[iterator] == " "):
                break
            else:
                number += str[iterator]
            iterator += 1
        return [number, "miles"]
    else: # km till miles
        number = ""
        iterator = 0
        while True:
            if (str[iterator] == " "):
                break
            else:
                number += str[iterator]
            iterator += 1
        return [number, "km"]


def convertToKilometers(miles): 
    conv = 0.621371
    return int(miles) / conv

def convertToMiles(km):
    conv = 0.621371
    return conv * int(km)

distanceArray = determineMileOrKilometer(userInput)

if (distanceArray[1] == "km"): # om userinput är km
    miles = convertToMiles(distanceArray[0])
    print(userInput + " motsvarar " + str(miles) + " miles") # printar miles
elif (distanceArray[1] == "miles"):
    km = convertToKilometers(distanceArray[0]) # om userinput är miles
    print(userInput + " motsvarar " + str(km) + " km") # printar km

