#variable sor the sum
sum = 0

# it will loop through i=1 to i=999
for i in range(1, 1000):
    # if i is divisible by 3 or 5, adds i to the sum
    if (i%3 == 0) or (i%5 == 0):
        sum += i

# prints the final sum
print(f"Sum: {sum}")