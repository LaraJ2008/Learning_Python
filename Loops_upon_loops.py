#Write a python program that adds up the numbers from 1 to 100.

#While current number is less than top number add current number to Sum, then increment
#produce incremented number then add it to Partial_sum, assign Partial_sum to Full_sum?
#really this is just increment, add, increment, add...
Base_number = 0
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
        


