#Write a python program that adds up the numbers from 1 to 100.

#While current number is less than top number add current number to Sum, then increment
#produce incremented number then add it to Partial_sum, assign Partial_sum to Full_sum?
#really this is just increment, add, increment, add...
#oops first one hard codes initial addend to 1 

Top_number = 100
Current_addend = 1



while Current_addend <= Top_number:
    if Current_addend == 1:
        Partial_sum = 1
        Current_addend += 1
    else:
        Partial_sum = Current_addend + Partial_sum           
        Current_addend += 1
print(Partial_sum)
        

Top_number = 100
Current_addend = 10
Partial_sum = 0

while Current_addend <= Top_number:
    Partial_sum = Current_addend + Partial_sum           
    Current_addend += 1
print(Partial_sum)
        

#Write a python program that takes a word as input, and counts the vowels in that word. Building block here
# This program shows how to extract letters from a given string.

# my_string = "hello"

# print("your string contains the following letters: ")

# for letter in my_string:
#   print(letter + " ")

Vowels = 0
Letters  = 0
my_word = "concatenate"

for letter in my_word:
    Letters +=1
    if letter in ["a", "e", "i", "o", "u", "y"]:
        Vowels +=1
print("your " + str(Letters) + " letter word contains " + str(Vowels) + " vowels")


#1.5 Write a python program that prints out the multiplication table for the numbers 1 through 9.

factor_1 = [*range(1,10,1)]
factor_2 = [*range(1,10,1)]

for first in factor_1:
    for second in factor_2:
       product = first * second 
       print(str(first) + "*" +str(second) + " = " + str(product) )
       


