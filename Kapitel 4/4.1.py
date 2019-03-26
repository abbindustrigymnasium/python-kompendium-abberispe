numbers = range(1000000) # skapar alla nummer i en lista
sumOfNumbers = 0 # definierar variabeln för summan

for number in numbers: # går igenom listan
    number += 1 # adderar 1. Detta eftersom listan börjar på 0 och slutar på 99
    sumOfNumbers += number # adderar nummret till summan

print(sumOfNumbers)