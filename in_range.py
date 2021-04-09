List =  [2, 3, 4, 5, 6, 7, 8, 9, 10]

def range(a):
    if a not in List:
        print(a, "is not in range")
    else:
        print(a, "is in range")

print(range(21))