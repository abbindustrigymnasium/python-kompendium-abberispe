import requests

userInput = str(input("Ange en stad."))

apiString = "https://54qhf521ze.execute-api.eu-north-1.amazonaws.com/weather/" + userInput

r = requests.get(apiString)
data = r.json()  # hämtar data för användarens stad

returnString = ""

for forecast in data["forecasts"]: # tittar på datan vid varje dag
    returnString += forecast["date"] + "      " + forecast["forecast"] + "\n" # lägger till datumet och prognosen i en string 

print(returnString)