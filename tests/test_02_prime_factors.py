#solving this will be helpful for solving problem 0003
#well, i just solved it, haha
n = 600851475143
factors = []
i = 2
#tried using for + range, but that way i had to loop all the way up to n
#using while was better, because i can update n and then it stops at the largest factor :)
while i <= n:
    while n % i == 0:
        factors.append(i)
        n = n/i
    i += 1
print(factors)