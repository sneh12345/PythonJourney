def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
print('Limit is 996')
n=int(input("Input a number to compute the factiorial : "))
print(factorial(n))
