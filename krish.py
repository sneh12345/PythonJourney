Userinput = input("Is Degrees Fahreneith or Celcius. Write F or C Accordingly\n")
if Userinput == "C":
    print("Value Entered In Celsius")
    CelsiusInput = int(input("What is the value in Celsius\n"))
    if CelsiusInput < 0:
      print("Water is frozen")
    elif 0 < CelsiusInput < 100:
        print("Water is liquid")
    elif CelsiusInput > 100:
        print("Water is in its gaseous state")
        
if Userinput == "F":
     print("Value Entered In fahrenheit")
fahrenheitInput = int(input("What is the value in fahrenheit\n"))
if fahrenheitInput < 32:
      print("Water is frozen")
elif 32 < fahrenheitInput < 212:
        print("Water is liquid")
elif fahrenheitInput > 212:
        print("Water is in its gaseous state")