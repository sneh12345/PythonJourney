# This program will find out the greater number in the arguments

def larger_number(x, y, z):
    if x > y:
        print(x, "is greater")
    elif z > y & x:
        print(z, 'is greater')
    else:
        print(y, 'is greater')

larger_number(12, 31, 98)
