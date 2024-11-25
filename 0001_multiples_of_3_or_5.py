# initialize sum variable
sum = 0

# for every i, 0 <= i <= 999
for i in range(1000):
    # if i is divisible by 3 or 5, adds i to the sum
    if (i%3 == 0) or (i%5 == 0):
        sum += i

# prints the final sum
print(f"Sum: {sum}")

# please note that i can be 0, but in this case, this is not a problem