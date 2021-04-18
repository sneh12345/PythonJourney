def numsInput():
    num1 = int(input("Enter a Number 1-9 : "))
    while len(str(num1)) == 0:
        num1 = int(input("Enter a Number 1-9 : "))
        
    num2 = int(input("Enter another Number 1-9 : "))
    while len(str(num2)) == 0:
        num2 = int(input("Enter another Number 1-9 : "))
    return num1, num2

def addition(num1, num2):
    result = num1 + num2
    print("The result is : ",result)
    
def subtraction(num1, num2):
    result = num1 - num2
    print("The result is : ",result)

def multiplication(num1, num2):
    result = num1 * num2
    print("The result is : ",result)


def MakeMenu():
    print(" Calculator \n Choose a function: \n 1. Addition \n 2. Subtraction \n 3. Multiplication \n 4. Recall last result \n 5.Exit")
    menu = input("\n Enter Input : ")
    if menu == 1:
        addition(*numsInput())
    elif menu == 2:
        subtraction(*numsInput())
    elif menu == 3:
        multiplication(*numsInput())
    elif menu == 5:
        pass
    else:
        print("Please enter a valid choice.")


MakeMenu()

