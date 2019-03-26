numbers = range(500) # skapar listan
sumOfNumbers = 0

for number in numbers:
    number += 1
    if (number % 2 == 1): # tittar om numret är udda
        sumOfNumbers += number
    
print(sumOfNumbers)
