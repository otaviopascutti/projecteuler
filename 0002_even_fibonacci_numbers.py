# initialize a(n)
an = 1
# initialize a(n-1)
an_minus_one = 1
# max value for fibonacci number
max = 4000000
# initialize the sum
sum = 0

# while the current fibonacci number do not exceed max
while an <= max:
    # if even, add it to the sum
    if (an % 2) == 0:
        sum += an
    # recalculate for next iteration
    aux = an
    an += an_minus_one
    an_minus_one = aux

# print the sum of all even fibonacci numbers below max
print(f"Sum:{sum}")