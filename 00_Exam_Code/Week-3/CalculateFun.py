a = int(input("Enter a 1st number: "))
b = int(input("Enter a 2nd number: "))
op = input("Enter an operator from +, -, *, /: ")
def calculate(a, b, op):
    if op == "+":
        return a + b
    elif op == "-":
        return a - b
    elif op == "*":
        return a * b
    elif op == "/":
        return a / b
    else:
        return "Invalid operator"

ans = calculate(a, b, op)
print(ans)