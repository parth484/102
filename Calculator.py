print("Welcome to this Calculator .")
print("Press '1' to do Addition . Press '2' to do Subtraction . Press '3' to Multiply . Press '4' to Divide .")

Choice =   int(input("Choose what you want to do . "))
num1   =   int(input("Enter The First Number - "))
num2   =   int(input("Enter The Second Number - "))
#102

Add = float(num1 + num2)
Subtract =float(num1 - num2)
Multiply = float(num1 * num2)
Divide = float(num1 / num2)

if Choice == 1:
    print("The Added Number is ", Add)
elif Choice == 2:
    print("The Subtracted Number is ",Subtract)
elif Choice == 3:
    print("Your Multiplied Number is ",Multiply)
elif Choice == 4:
    print("Your Divided Number is ",Divide)
else:
    print("The Operation is invalid")    