import praw # packetet för att kunna använda reddit via python

def cmInchConverter(input, cmOrInch): # True = cm to inch, False = inch to cm
        return str(input) + " cm is " + str(round(float(input) * 0.3937, 2)) + " inches" if cmOrInch else str(input) + " inches is " + str(round(float(input) / 0.3937, 2)) + " cm"

def kmMilesConverter(input, kmOrMiles): # True = km to miles, False = miles to km
        return str(input) + " km is " + str(round(float(input) * 0.621371, 2)) + " miles" if kmOrMiles else str(input) + " miles is " + str(round(float(input) / 0.621371, 2)) + " km"

def kgLbsConverter(input, kgOrLbs): # True = lbs to kg, False = kg to lbs
        return str(input) + " lbs is " + str(round(float(input) * 0.454, 2)) + " kg" if kgOrLbs else str(float(input)) + " kg is " + str(round(float(input) / 0.454, 2)) + " lbs"

def kphMphConverter(input, kphOrMph): # True = km/h to mph, False = mph to km/h
        return str(input) + " km/h is " + str(round(float(input) * 0.621371, 2)) + " mph" if kphOrMph else str(input) + " mph is " + str(round(float(input) / 0.621371, 2)) + " km/h"

def celsiusFahrenheitConverter(input, celsiusOrFahrenheit): # True = celsius to fahrenheit, False = fahrenheit to celsius
        return str(input) + " degrees celsius is " + str(round((float(input) * 1.8) + 32, 2)) + " degrees fahrenheit" if celsiusOrFahrenheit else str(input) + " degrees fahrenheit is " + str(round((float(input) - 32) / 1.8, 2)) + " degrees celsius"

def metersYardsConverter(input, metersOrYards): # True = yards to meters, False = meters to yards
        return str(input) + " yards is " + str(round(float(input) * 0.9144, 2)) + " meters" if metersOrYards else str(input) + " meters is " + str(round(float(input) / 0.9144, 2)) + " yards"

def isNumber(s):
    if (s != 0):
        try:
            float(s)
            return True
        except ValueError:
            return False
    else:
        return False

#kmh to mph, dollar to euro, litre to gallon, celsius to fahrenheit, yards to meters

reddit = praw.Reddit(client_id='B_JSzQBUP26DtQ',
                     client_secret='VK3Q8xTBAlcjhCPBySSEWR7SO9k',
                     username="converter-bot",
                     password="ABBspets123",
                     user_agent='converter-bot') # mitt konto

subreddit = reddit.subreddit("all") # hämtar alla subreddits

comments = subreddit.stream.comments() # hämtar alla kommentarer som läggs ut hela tiden i en så kallad stream. Om jag sätter denna i en for loop så kommer for loopen aldrig att avsluta, utan alltid få nya kommentarer hela tiden.

print("ready");

for comment in comments:
        if (comment.author.name != "converter-bot"): # så att jag inte svarar mig själv
                commentArray = comment.body.split(" ") # gör en array av comment.body stringen. Alla items kommer i arrayen kommer att vara orden i comment.body
                if ("cm" in commentArray): # om ordet cm finns i arrayen ovan.
                        indexOfNumber = commentArray.index("cm") - 1
                        if (isNumber(commentArray[indexOfNumber])): # tittar på om ordet precis bakom cm är ett nummer. Om detta är fallet så försöker den svara på reddit
                                print("comment: " + comment.body)
                                print("measurement: " + commentArray[indexOfNumber])
                                print("reply: " + cmInchConverter(commentArray[indexOfNumber], True)) # printar svaret
                                try: # försöker svara
                                     comment.reply(cmInchConverter(commentArray[indexOfNumber], True)) # svarar på reddit. Använder cmInchConverter och sätter ena parametern till numret, och den andra till True då det betyder cm till inch. False betyder inch till cm
                                except: # om ett error kommer upp, så fortsätter ändå programet köra.
                                     print("you are banned from that subreddit")
                elif ("inches" in commentArray):
                        indexOfNumber = commentArray.index("inches") - 1
                        if (isNumber(commentArray[indexOfNumber])):
                                print("comment: " + comment.body)
                                print("measurement: " + commentArray[indexOfNumber])
                                print("reply: " + cmInchConverter(commentArray[indexOfNumber], False))
                                try:
                                     comment.reply(cmInchConverter(commentArray[indexOfNumber], False))
                                except:
                                     print("you are banned from that subreddit")
                elif ("km" in commentArray):
                        indexOfNumber = commentArray.index("km") - 1
                        if (isNumber(commentArray[indexOfNumber])):
                                print("comment: " + comment.body)
                                print("measurement: " + commentArray[indexOfNumber])
                                print("reply: " + kmMilesConverter(commentArray[indexOfNumber], True))
                                try:
                                     comment.reply(kmMilesConverter(commentArray[indexOfNumber], True))
                                except:
                                     print("you are banned from that subreddit")
                elif ("miles" in commentArray):
                        indexOfNumber = commentArray.index("miles") - 1
                        if (isNumber(commentArray[indexOfNumber])):
                                print("comment: " + comment.body)
                                print("measurement: " + commentArray[indexOfNumber])
                                print("reply: " + kmMilesConverter(commentArray[indexOfNumber], False))
                                try:
                                     comment.reply(kmMilesConverter(commentArray[indexOfNumber], False))
                                except:
                                     print("you are banned from that subreddit")
                elif ("lbs" in commentArray):
                        indexOfNumber = commentArray.index("lbs") - 1
                        if (isNumber(commentArray[indexOfNumber])):
                                print("comment: " + comment.body)
                                print("measurement: " + commentArray[indexOfNumber])
                                print("reply: " + kgLbsConverter(commentArray[indexOfNumber], True))
                                try:
                                     comment.reply(kgLbsConverter(commentArray[indexOfNumber], True))
                                except:
                                     print("you are banned from that subreddit")
                elif ("kg" in commentArray):
                        indexOfNumber = commentArray.index("kg") - 1
                        if (isNumber(commentArray[indexOfNumber])):
                                print("comment: " + comment.body)
                                print("measurement: " + commentArray[indexOfNumber])
                                print("reply: " + kgLbsConverter(commentArray[indexOfNumber], False))
                                try:
                                     comment.reply(kgLbsConverter(commentArray[indexOfNumber], False))
                                except:
                                     print("you are banned from that subreddit")
                elif ("mph" in commentArray):
                        indexOfNumber = commentArray.index("mph") - 1
                        if (isNumber(commentArray[indexOfNumber])):
                                print("comment: " + comment.body)
                                print("measurement: " + commentArray[indexOfNumber])
                                print("reply: " + kphMphConverter(commentArray[indexOfNumber], False))
                                try:
                                     comment.reply(kphMphConverter(commentArray[indexOfNumber], False))
                                except:
                                     print("you are banned from that subreddit")
                elif ("km/h" in commentArray):
                        indexOfNumber = commentArray.index("km/h") - 1
                        if (isNumber(commentArray[indexOfNumber])):
                                print("comment: " + comment.body)
                                print("measurement: " + commentArray[indexOfNumber])
                                print("reply: " + kphMphConverter(commentArray[indexOfNumber], True))
                                try:
                                     comment.reply(kphMphConverter(commentArray[indexOfNumber], True))
                                except:
                                     print("you are banned from that subreddit")
                elif ("celsius" in commentArray):
                        print("celsius: " + comment.body)
                        indexOfNumber = commentArray.index("celsius") - 2
                        if (isNumber(commentArray[indexOfNumber])):
                                print("comment: " + comment.body)
                                print("measurement: " + commentArray[indexOfNumber])
                                print("reply: " + celsiusFahrenheitConverter(commentArray[indexOfNumber], True))
                                try:
                                     comment.reply(celsiusFahrenheitConverter(commentArray[indexOfNumber], True))
                                except:
                                     print("you are banned from that subreddit")
                elif ("fahrenheit" in commentArray):
                        print("fahrenheit: " + comment.body)
                        indexOfNumber = commentArray.index("fahrenheit") - 2
                        if (isNumber(commentArray[indexOfNumber])):
                                print("comment: " + comment.body)
                                print("measurement: " + commentArray[indexOfNumber])
                                print("reply: " + celsiusFahrenheitConverter(commentArray[indexOfNumber], False))
                                try:
                                     comment.reply(celsiusFahrenheitConverter(commentArray[indexOfNumber], False))
                                except:
                                     print("you are banned from that subreddit")
                elif ("meters" in commentArray):
                        indexOfNumber = commentArray.index("meters") - 1
                        if (isNumber(commentArray[indexOfNumber])):
                                print("comment: " + comment.body)
                                print("measurement: " + commentArray[indexOfNumber])
                                print("reply: " + metersYardsConverter(commentArray[indexOfNumber], False))
                                try:
                                     comment.reply(metersYardsConverter(commentArray[indexOfNumber], False))
                                except:
                                     print("you are banned from that subreddit")
                elif ("yards" in commentArray):
                        indexOfNumber = commentArray.index("yards") - 1
                        if (isNumber(commentArray[indexOfNumber])):
                                print("comment: " + comment.body)
                                print("measurement: " + commentArray[indexOfNumber])
                                print("reply: " + metersYardsConverter(commentArray[indexOfNumber], True))
                                try:
                                     comment.reply(metersYardsConverter(commentArray[indexOfNumber], True))
                                except:
                                     print("you are banned from that subreddit")
