import math 

# An algebraic equation has a missing number. We have to find that missing number 
# Only addition
# This program can ONLY solve 1 constant, one variable, and only addition. With one answer. 

constant = int(input('Please enter the constant, the known number in the algebra question\n'))
variable = str(input('Please enter the variable, a place holder fotr the missing number. (a-z)\n'))
output = int(input('Please enter the output of the expression\n'))
what = input('What do you wanna do? Minus the variable? Add?\n')

def compute_alga(a, c):
    return a - c

def compute_algm(a, c):
    return a + c
    

if constant > output:
    print(abs(variable))


if what == 'Minus':
    print(variable,"is",compute_algm(constant, output))
elif what == 'Add':
    print(variable,"is",compute_alga(constant, output))
else: 
    print("Sorry, can't help with you there.") 