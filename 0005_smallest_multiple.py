# this has O(n^2) time complexity and is quite slow, need to revisit later
# another idea is by analyzing the factors. one update i made is to increase by the greatest factor
# but maybe i can just do the following:
# 1*2*3*4*5*6*7*8*9*10
# and then remove numbers that are factors from others on the list, because 2 is a factor of 10, 5 is a factor o 10
# so if a number needs to be divisible by 10, it is already divisibla by 2 and 5, so i can remove 10 from the list, because
# it is already there, in the form of 2*5
# so what if i manipulate the multiplication above to come up with the number
# TODO: well this is just LCM that i learned in school! I'll fix the algorithm later

not_found = True
n = 0
largest_factor = 20
while not_found:
    n += largest_factor
    for i in range(1, largest_factor + 1):
        if n%i != 0:
            break
        elif i == 20:
            not_found = False
print(n)