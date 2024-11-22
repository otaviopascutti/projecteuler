my_values = []
my_derivatives = []
x = -4
while x <= 4:
    my_values.append(x*x)
    my_derivatives.append(2*x)
    x = x+1
print(my_values)
print(my_derivatives)