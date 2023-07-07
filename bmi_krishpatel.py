import math

output = ["Your BMI is ", "You are underweight", "You are at normal weight", "You are overweight", "You are obese", "Welcome to the BMI Calculator, Please enter the following to calculate your body mass index: ", "Enter your weight in lbs (pounds): ", "Enter your height in in. (inches): "]

def bmi():
    while True:
        print(output[5])
    
        weight = eval(input(output[6]))
        
        height = eval(input(output[7]))
        
        
        (solution) = (weight / math.pow(height, 2)) * 703
        rsolution = round(solution, 1)
        print (output[0] + str(rsolution))
        
        if solution < 18.5:
            print(output[1])
        
        elif 18.5 < solution < 24.9:
            print(output[2])
        
        elif 24.9 < solution < 29.9:
            print(output[3])
        
        elif 30 < solution:
            print (output[4])
            
        next_rsolution = (input("Next Calculation?) (Yes/No):"))
        if (next_rsolution == "Yes" or "yes"):
            bmi()
        else:
            quit()

bmi()