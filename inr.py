
# Python3 program to convert
# the number from International
# system to Indian system
 
# Function to convert a number
# represented in International
# numeric system to Indian numeric
# system.
def convert(input):
 
    # Find the length of the
    # input string
    Len = len(input)
 
    # Removing all the separators(, )
    # from the input string
    i = 0
    while(i < Len):
        if(input[i] == ","):
            input = input[:i] + input[i + 1:]
            Len -= 1
            i -= 1
        elif(input[i] == " "):
            input=input[:i] + input[i + 1:]
            Len -= 1
            i -= 1
        else:
            i += 1
    # Reverse the input string
    input=input[::-1]
 
    # Declaring the output string
    output = ""
 
    # Process the input string
    for i in range(Len):
 
        # Add a separator(, ) after the
        # third number
        if(i == 2):
            output += input[i]
            output += " ,"
         
        # Then add a separator(, ) after
        # every second number
        elif(i > 2 and i % 2 == 0 and
             i + 1 < Len):
            output += input[i]
            output += " ,"
        else:
            output += input[i]
     
    # Reverse the output string
    output=output[::-1]
 
    # Return the output string back
    # to the main function
    return output
 
# Driver code
input1 = "123, 456, 789"
input2 = "90, 050, 000, 000"
print(convert(input1))
print(convert(input2))