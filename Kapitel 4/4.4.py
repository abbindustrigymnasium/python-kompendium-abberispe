förnamn =[" Maria ", " Erik ", " Karl "]
efternamn =[" Svensson ", " Karlsson ", " Andersson "]

for namn in förnamn: #lägger in två for loopar i varandra. Går igenom alla namn i förnamn för att sedan para ihop dem med alla namn i efternamn
    for namn2 in efternamn:
        print(namn, namn2)