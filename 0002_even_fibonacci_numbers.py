#variable for current term
an = 1
#variable for a(n-1) term, i'm also starting it with 1 because you'll see it will work out just fine
an_minus_one = 1
#max is the greatest number i'll allow for the sequence
max = 4000000
#sum variable
sum = 0

# while the current fibonacci number do not exceed max
while an <= max:
    # if current term is even, add it to the sum
    if (an % 2) == 0:
        sum += an
    # recalculate current term for next iteration
    # I chose to do it in three lines like this because it feels more readable to me
    aux = an
    an += an_minus_one
    an_minus_one = aux

# print the sum of all even fibonacci numbers below max
print(f"Sum:{sum}")