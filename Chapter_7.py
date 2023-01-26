#Chapter 7 

#the reply to the input gets stored in the variable 'message' Currently this only works one line at a time. output is 
#tell me something and I will repeat itprint(message)
message = input("tell me something and I will repeat it: ")
print(message)

name = (input("What's your name: "))
print("go away," + name + "!")


# # += allows a two line string
prompt = "we would like to personalize our ads"
prompt += "\nWho are you?"

name = input(prompt)
print("\nwe want your money " + name + "!")

age = input("Tell me your age ")
age = int(age)
if age >= 40:
    print("\n)You're much too old ")
else:
    print("\nYou're not old enough ")

number = input("Tell me a number: ")
number = int(number)

if 0 == number%2:
    print("\nYup " + str(number) + " is even ")
else:
    print("\nYeah " + str(number) + " is odd ")    


# make = input("What car make are you interested in? ")
# print ("\nWe don't have " + make + "s, try again")

#Ok I wrote this if else to see what would happen if two of the conditions technically overlapped, and it does fine, order presumably matters

party = input("How many people are dining? ")
party = int(party)

if 1 == party:
    print("\nTake a seat at the bar")
elif party <= 8:
    print("\nWe can seat you now")
elif party > 8: 
    print("\nYour party of " + str(party) + " is too large. Goodbye.")


#While loops, += increments

current_number = 1
while current_number <=5:
    print(current_number)
    current_number += 1


# What in the while loop is telling it to reitterate the prompt? Feels like I should have to explain that to it

my_prompt = ("Say something, I'll echo it back:")
my_prompt += ("\n Type 'quit' to end program \n")

message = ""
while message != 'quit':
    message = input(my_prompt)
    if message != 'quit':
        print(message)


# #checking run's status is a flag?
run = True
while run: 
    message = input(my_prompt)
    if message != 'quit':
        print(message)
    else:
        run = False


# while True has no false setting and needs a break command to stop it
prompt = ("\n Name a person you have kissed")
prompt += ("\n to stop type 'quit' \n")

while True:
    person = input(prompt)

    if 'quit' == person:
        break
    else: 
        print("\nI'd love to kiss " + person + "!")

# continue means to disregard following commands within loop, step back out to the parent loop
# why increment before testing? 
current_number = 0
while current_number <=10:
    current_number += 1
    if 0 == current_number%2:
        continue
    else:
        print(current_number) 


current_number = 0
while current_number <=10:
    if 0 == current_number%2:
        current_number += 1
        continue
    else:
        print(current_number) 
        current_number += 1


#questions: after I run this why can't I query Toppings? would you have used a flag? Or is a while/break better?

order = ("Enter a topping you wish to add: ")
order += ("\n(when finished enter 'done') \n")

Toppings = []

print("Toppings is ", Toppings)

topping = ""
run = True
while run:
    topping = input(order)
    if topping != 'done':
        print(topping + " added")
        Toppings.append(topping)

    elif topping == 'done':
        print(Toppings)
        run = False