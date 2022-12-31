Glenn_Task='Hello World'
print(Glenn_Task)


x='stringsgoinquotes'
y='spaces in string'
z='string symbols!@'
print(y)
print(z)
type(z)
print(x[3])
print(x,y,z)

#lists are a data type, listed in [], 0 indexed. Apparently lists consist of numbers or defined variables
#strings are a data type listed in '', can contain spaces/symbols, also 0 indexed
#elements queried by print(x[]). This is true for strings, lists and tuples

#TUPLES is a stupid word. Like pentuple or octuple? Ordered, immutable, uses (). Apparently cannot be called?
#[] asks for value at a position but () 'calls?'
v=(4,5,6,7)
print(v[2])
#print(v(2)) It sure hates that

#what does callable mean vs querying a position? 
#so pointers are what I used in vim but didn't have a name for, they are variables that contain the path to a file
#but a pointer can contain a command? eg x=open(filepath)
a=40
b=50
result = (a*b)
print(result)
#that's a terrible variable name

#MATH if you ask for division but want the answer in int format, it doesn't round, just drops the fraction portion
x=4/5
y=4//5
print(x,y)
a=2.85//4 #soooo // isn't int division it's floor division apparently
print(a)

#modulo is weird, put in place of the division sign entirely %
F=30%8
print(F)

string='LaraLearnsPython'
#print(string[0,8])
#ok so it doesn't recognize that

print(string[0])
print(string[4:8]) #but this isn't inclusive of the top end wtf

string2='AndyLovesMushrooms'
string3=string[:4]+string2[4:9]+string[10:]
print(string3)