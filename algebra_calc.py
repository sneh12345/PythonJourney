# An algebraic equation has a missing number. We have tp find that missing number 
# Only addition
# This program can ONLY solve 1 constant, one variable, and only addition. With one answer. 

constant = int(input('Please enter the constant, the known number in the algebra question'))
variable = str(input('Please enter the variable, a place holder fotr the missing number. (a-z)'))
output = input('Please enter the output of the expression')
print("This is your equation, ", constant, "+", variable, "=", output)

'''
def algebra(constant, output):
     return output - constant

print(algebra(constant, output))
'''