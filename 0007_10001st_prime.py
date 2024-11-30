#idea: i dont have to try every natural number up to prime_candidate
#but i can try to divide them only by the primes i got up to that point
#   but how? i need to keep track of the primes i find.
#   i'll use more memory, but it will make my code run faster
#and even then i wont need to try to divide by every prime, because any prime greater than n/2 wont divide n (DONE)
primes_wanted = 10001
primes = [2]
prime_candidate = 3 #first candidate. first candidate is 3 because 2 is already in the array
while len(primes)<primes_wanted:
    prime_index = 0
    while primes[prime_index]<=prime_candidate/2:
        if prime_candidate%primes[prime_index] == 0:
            break
        else:
            prime_index+=1

    # if current prime is greater than prime_candidate/2, it means there was no division
    # found in the while loop above, so the candidate is prime        
    if  primes[prime_index]>prime_candidate/2:
        primes.append(prime_candidate)
    
    prime_candidate+=1

print(f"prime number {len(primes)}: {primes[-1]}")
