import math 


# checking numbers up to and including the top prime. 
top_prime=1000

# build the list of candidate prime numbers
candidate_primes=[*range(2,top_prime+1,1)]

# build a list of the factors we'll check
#factors=[*range(2,round(math.sqrt(top_prime))+1)]

# walk through all of our candidate primes
for candidate in range(2,top_prime+1):

    print("candidate: ", candidate)

    # for that candidate number, lets check all factors up to the square root
    # of that number
    top_factor = math.floor(math.sqrt(candidate)) 
    for factor in range(2,top_factor+1):
            
            print("factor: ", factor)
            # if we had a divisible factor, it's not prime!
            if candidate%factor==0:
                print(candidate, " not prime!!!")
                candidate_primes.remove(candidate)
                break
            
# we're done!  print the primes!
print(candidate_primes)
