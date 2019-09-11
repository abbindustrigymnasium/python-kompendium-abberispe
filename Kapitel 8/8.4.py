import ui
import web

ui.line(False)
ui.header("ARTISTS DATABASE")
ui.line(False)
ui.echo("Welcome to a world of")
ui.echo("Music!")
ui.line(False)
ui.echo("L | List of artists")
ui.echo("V | View artist profile")
ui.echo("E | Exit application")
ui.line(False)
userInput = ui.prompt("Selection > ") # printar ut hela hem-menyn


def main(input): #main funktionen så att man kan köra programmet flera gånger utan att restarta. Input parametern används när man vill att programmet inte ska startas om helt, utan kanske börja igen i 'View artist profile'
    global userInput  #gör variabeln userinput till global för att kunna jämföra den med V, L eller E
    if (userInput == "L" or input == "L"):
        data = web.get("https://5hyqtreww2.execute-api.eu-north-1.amazonaws.com/artists/") # hämtar data för alla artister
        ui.line(False)
        ui.header("ARTIST DATABASE")
        ui.line(False) 
        for artist in data["artists"]: 
            ui.echo(artist["name"]) # går igenom alla namn i databasen och printar ut dem
        ui.line(True)
        ui.echo("L | List of artists")
        ui.echo("V | View artist profile")
        ui.echo("E | Exit application")
        ui.line(False)
        userInput = ui.prompt("Selection > ")
        main(None) # restartar programmet så att vi kan köra programmet flera gånger
    if (userInput == "V"):
        data = web.get("https://5hyqtreww2.execute-api.eu-north-1.amazonaws.com/artists/") # hämtar data
        ui.line(False)
        ui.header("ARTIST DATABASE")
        ui.line(False)
        inputArtist = ui.prompt("Artist name > ").lower() # frågar om artistnamn, gör om det till lowercase för att lättare jämföra
        ui.line(True)
        found = False
        for artist in data["artists"]: # går igenom alla artister
            if (artist["name"].lower() == inputArtist): # tittar om namnet är lika med user input för artisten
                found = True
                ui.header(inputArtist.capitalize()) # skriver ut titel för namnet
                apiString = "https://5hyqtreww2.execute-api.eu-north-1.amazonaws.com/artists/" + artist["id"] # hämtar data för artisten såsom members och years active
                data = web.get(apiString)
                genreString = ""
                membersString = ""
                yearsActiveString = ""
                for genre in data["artist"]["genres"]: # eftersom all data kommer via en array så går jag igenom arraysen och lägger datan som en lång string
                    genreString += genre.capitalize() + ", "
                for member in data["artist"]["members"]:
                    membersString += member.capitalize() + ", "
                for yearsActive in data["artist"]["years_active"]:
                    yearsActiveString += yearsActive.capitalize() + ", "
                genreString = genreString[:-2]
                membersString = membersString[:-2] # tar bort två karaktärer från varje string eftersom de alltid kommer sluta med ', '
                yearsActiveString = yearsActiveString[:-2]
    
                ui.echo("Members: " + membersString)
                ui.echo("Genre: " + genreString) # printar all data
                ui.echo("Years Active: " + yearsActiveString)
                ui.line(True)
                ui.echo("L | List of artists")
                ui.echo("V | View artist profile")
                ui.echo("E | Exit application")
                ui.line(False)
                userInput = ui.prompt("Selection > ")
                main(None) # restartar programmet
        if (found == False):
            ui.echo("Unknown artist: " + inputArtist)
            userInput = ui.prompt("Selection > ")
            main("L")
    else:
        ui.line(True)
        ui.echo("Unknown command: " + userInput)
        ui.line(True)
        ui.echo("L | List of artists")
        ui.echo("V | View artist profile")
        ui.echo("E | Exit application")
        ui.line(False)
        userInput = ui.prompt("Selection > ")
        main(None)

main(None) # startar programmet
