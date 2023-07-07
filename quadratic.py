import math 

def main():
    print("This program finds the real solutions to a quadratic.")
    print()

    a = eval(input("Please enter the coefficients a: "))
    b = eval(input("Please enter the coefficients b: "))
    c = eval(input("Please enter the coefficients c: "))

    discRoot = math.sqrt(b * b - 4 * a * c)
    root1 = (-b + discRoot) / (2 * a)
    root2 = (-b - discRoot) / (2 * a)

    print()
    print("The solutions are: ", root1, root2)

main()