"# Learning_Python" 
#The problem of primes, I guess I would just go through the numbers in my head, checking each one for extraneous factors. I'd need to check 2/3/5/7 as factors 
to get to 100. 

So what I'm doing is sort of a loop, and in my head once I find one factor that number doesn't even need to be checked against the rest. 
I guess I could ask for a list (2:100) and loop the numbers through division, looking for anything where x%factor = 0. If a 0 isn't found for any primes, 
that number gets written to a primes list? 
I'll have to think about how to handle 2/3/5/7 themselves...oh I guess I can set a clause of if x<9 do something else, tbd
Seems like checking each prime factor one after another for each number in 9:100 would work, and if # makes it though all the hoops, that lands it in [primes]


NESTED IF which I gather is a messy way to go... 
SET = 1-100
for i in SET
  if i>10:
    if i%2==0:
      delete i from SET
    else:
      if i%3==0:
        delete i from SET
      else:
        if i%5==0:
          delete i from SET
        else:
          if i%7==0:
            delete i from SET
          else: END
 else:
  if i is an element of [1,4,6,8,9]
    delete i from SET
    
    END
    
Will delete or remove understand the use of i as a variable
Don't know how to say is an element of, guessing i can't use the curvy E
Also making a list 1-100 looks like it has some hoops? Set bottom number, set top number, set step size? Or some bullshit?
      
