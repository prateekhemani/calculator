from calculator_function import addition
from calculator_function import subtraction
from calculator_function import multiply
from calculator_function import divide

a = input("Enter your first value: ")
a = float(a)

b = input("Enter your second value: ")
b = float(b)

c = input("Enter your choice[+, -, /, *]: ")

if c == '+':
    d = addition(a, b)
    print("your addition is: ", d)

elif c == '-':
    d = subtraction(a,b)
    print("your answer: ", d)

elif c == '*':
    d = multiply(a,b)
    print("your answer: ", d)

elif c == '/':
    d = divide(a,b)
    print("your answer: ", d)

else:
    print("Invalid operation")




