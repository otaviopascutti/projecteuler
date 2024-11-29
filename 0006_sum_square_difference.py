#for each natual number x | 1<=x<=n, I square it and add it to sum_of_square, and also add it to sum_of_numbers
#then I get square of the sum by squaring the sum of number
#finally i print the difference
n = 100
sum_of_numbers = 0
sum_of_squares = 0
square_of_the_sum = 0
for i in range(n):
    sum_of_squares += pow((i+1),2)
    sum_of_numbers += (i+1)
square_of_the_sum = pow(sum_of_numbers, 2)
print(square_of_the_sum - sum_of_squares)