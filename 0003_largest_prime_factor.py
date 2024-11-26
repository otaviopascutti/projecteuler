#the number i want to factor
n = 600851475143
#array in which i will append factors
factors = []
#i will start at 2, because i want prime factors
i = 2
#for the loop, I tried using for i in range(i, n+1), but that way i had to loop all the way up to n
#using while was better, because i can update n and then it stops at the largest factor :)
while i <= n:
    while n % i == 0:
        factors.append(i)
        n = n/i
    i += 1
print(f"Prime Factors: {factors}\nLargest Prime Factor: {factors[-1]}")