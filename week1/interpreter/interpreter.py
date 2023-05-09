#დავალება #9 - Math Interpreter
expression = input("Expression: ")

x = float(expression.split(" ")[0])
y = expression.split(" ")[1]
z = float(expression.split(" ")[2])

if y == "+":
    print(x + z)
elif y == "-":
    print(x - z)
elif y == "*":
    print(x * z)
elif y == "/":
    print(x/z)