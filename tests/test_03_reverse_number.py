#this will be useful for the solution of problem 0004
#this script reverts number and then checks if its a palindrome

#number to be reversed
number = 99099

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
print(number)
print(reversed)
print(number == reversed)