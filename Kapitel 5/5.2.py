ages = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17]
# alla åldrar och respektive sömntimmar ligger på samma index i arraysen
sleep = [14, 13, 12, 11.5, 11, 11, 10.5, 10, 10, 10, 9.5, 9, 9, 9, 9, 8.5, 8]

userName = input("What is your name?")
userAge = int(input("What is your age?")) # frågar användaren

iterator = 0 # använder iterator i loopen för att kunna utnyttja index i arraysen

for age in ages:
    if (age == userAge):
        print("Hallå " + userName + "! Enligt Vårdguidens rekommendationer behöver individer i din ålder (" + str(userAge) + " år) sova minst " + str(sleep[iterator]) + " timmar per natt")
    iterator += 1