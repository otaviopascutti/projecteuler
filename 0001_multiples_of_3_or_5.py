sum = 0
for i in range(10):
    if (i%3 == 0) or (i%5 == 0):
        print(f"{i} <--")
        sum += i
    else:
        print(i)
print(f"Sum: {sum}")