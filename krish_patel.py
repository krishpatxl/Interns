import math


def calculator():
    while True:
    
        print(" 1. Add\n 2. Subtract\n 3. Multiply\n 4. Divide\n 5. Square Root\n 6. Power")
        i = eval(input("Select from the following: "))
        
        match i:
    
            case 1:
                num1 = eval(input("Enter first number: "))
                num2 = eval(input("Enter second number: "))
                solution = num1 + num2
                print (solution)
        
            case 2:
                num1 = eval(input("Enter first number: "))
                num2 = eval(input("Enter second number: "))
                solution = num1 - num2
                print (solution)
        
            case 3:
                num1 = eval(input("Enter first number: "))
                num2 = eval(input("Enter second number: "))
                solution = num1 * num2
                print (solution)
        
            case 4:
                num1 = eval(input("Enter first number: "))
                num2 = eval(input("Enter second number: "))
                solution = num1 / num2
                print (solution)
        
            case 5:
                num1 = eval(input("Enter a number: "))
                solution = math.sqrt(num1)
                print (solution)
        
            case 6:
                num1 = eval(input("Enter first number: "))
                num2 = eval(input("Enter second number: "))
                solution = math.pow(num1, num2)
                print (solution)
            
        next_solution = (input("Next Calculation?) (Yes/No):"))
        if (next_solution == "Yes"):
            calculator()
        else:
            quit()
        
calculator()