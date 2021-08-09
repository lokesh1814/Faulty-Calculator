#Faulty Calculator
"""Design a calculator which will correctly solve all the problems except
the following ones:
       45 * 3 = 555, 56 + 9 = 77, 56 / 6 = 4"""
""" Your program should take operator and the two numbers as input from the 
user and then return the result"""

value1 = int(input("Enter the first value: "))

op = input("Choose The operator(+, -, *, /): ") #operator
1
value2 = int(input("Enter the second value: "))

#Addition
if op == "+":
    if value1 == 56 and value2 == 9 or value1 == 9 and value2 == 56:
        print(value1, "+", value2, "=", "77")

    else:
        print("Result: ", value1 + value2)

#Subtraction
if op == "-":
    print("Result: ", value1 - value2)

#Multiplication
if op == "*":
    if value1 == 45 and value2 == 3 or value1 == 3 and value2 ==45:
        print(value1, "*", value2, "=", "555")

    else:
        print("Result: ", value1 * value2)

#Division
if op == "/":
    if value1 == 56 and value2 == 6 or value1 == 6 and value2 == 56:
        print(value1, "/", value2, "=", "4")
    else:
        print("Result: ", value1 / value2)

else:
    print("Please, try again later.")