print("Welcome to Sneh's calculator")

question1 = int(input('First Number:\n'))
question2 = int(input('Second Number:\n'))

operation_input = input('What operation would you like to perform? \n')

if operation_input == "Division":
    print("Answer is", question1/question2)

if operation_input == "Multiplication":
    print("Answer is", question1 * question2)

if operation_input == "Addition":
    print('Answer is', question1 + question2)

if operation_input == "Subtraction":
    print('Answer is', question1 - question2)
