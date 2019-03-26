import requests

url = "https://5hyqtreww2.execute-api.eu-north-1.amazonaws.com/artists/"

r = requests.get(url)
dataArtists = r.json() # hämtar data för artister

for artist in dataArtists["artists"]:
    print(artist["name"]) # printar namnet hos varje artist

userInput = str(input("Ange en artists namn"))

for artist in dataArtists["artists"]: # tittar på artistens data
    if (userInput == artist["name"]): # om användarens artist förfrågning är samma som artistens namn
        apiString = "https://5hyqtreww2.execute-api.eu-north-1.amazonaws.com/artists/" + artist["id"]
        r = requests.get(apiString)
        dataArtist = r.json()
        returnString = ""
        returnString += "Genres: " + str(dataArtist["artist"]["genres"]) + "\nYears active: " + str(dataArtist["artist"]["years_active"]) + "\nMembers: " + str(dataArtist["artist"]["genres"]) # lägger dit all data om artisten i en string och sedan printar ut den
        print(returnString)

