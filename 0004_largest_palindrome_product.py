#to solve the multiplication of two digits i`ll make the following analisis
#AA is a number from 10 to 99, 10xAA is all multiplications from 10x10 to 10x99
#10xAA
#11xAA - already calculated: 11X10
#12XAA - already calculated: 12X10 and 12X11
#13XAA - already calculated: 13X10 and 13X11 and 13X12
#so it looks like a starting from 10x10, 11x11, 12x12, ... , 99x99 is better than starting from 10x10, 11x10, 12x10, ...

#array in which i'll store all palindromes
palindromes = []

#here i wanted to generalize the number of digits, so instead of making the range specific to 3 digits using range(100, 1000)
#i used number_of_digits with pow so i can calculate min and max numbers
number_of_digits = 3
min_number = pow(10, number_of_digits-1)
max_number = pow(10, number_of_digits)

for i in range(min_number , max_number):
    j = i
    while j < max_number:
        number = i*j

        n = number
        reversed = 0

        #i get the last digit by taking the remainder of division by 10
        #then build the reversed number by multiplying the reverse by 10 (creating a 0 in the units place) and then adding the last digit
        #finally, i remove the last digit from n, by subtracting the last digit, and dividing the result by 10
        #this will continue while n>0 
        while n > 0:
            last_digit = n % 10
            reversed = reversed * 10 + last_digit
            n = (n - last_digit) / 10

        # print(f"{i}x{b}")
        # print(number)
        # print(reversed)
        # print(number == reversed)

        if number == reversed:
            palindromes.append(number)

        j += 1

# print(palindromes)
print(f"Largest palindrome product: {max(palindromes)}")