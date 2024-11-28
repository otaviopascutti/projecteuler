not_found = True
n = 0
while not_found:
    n += 1
    for i in range(1, 11):
        if n%i != 0:
            break
        elif i == 10:
            not_found = False
print(n)