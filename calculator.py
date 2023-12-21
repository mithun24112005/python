def add(a, b):
    c = a + b
    print(f"{a}+{b}={c}")
    return c


def sub(a, b):
    c = a - b
    print(f"{a}-{b}={c}")
    return c


def mul(a, b):
    c = a * b
    print(f"{a}*{b}={c}")
    return c


def div(a, b):
    if b == 0:
        print("cant divide by zero")  # return the current value if b is zero
        return a
    c = a / b
    print(f"{a}/{b}={c}")
    return c


def mod(a, b):
    if b == 0:
        print("cant divide by zero")
        return a  # Return the current value if modulus with zero
    c = a % b
    print(f"{a}%{b}={c}")
    return c


global a
a = int(input("enter the value: "))
opretions = {"=", "+", "-", "/", "%", "*"}
while True:
    op = input("Enter the operator (+, -, *, /, %, =): ")
    if op == "=":
        print(f" the ans: {a}")
        break
    if op not in opretions:
        print("invalid operator")
        continue
    b = int(input("enter the value: "))
    if op == "+":
        a = add(a, b)  # keeps the value of c is a for further calculations
    elif op == "-":
        a = sub(a, b)
    elif op == "*":
        a = mul(a, b)
    elif op == "/":
        a = div(a, b)
    elif op == "%":
        a = mod(a, b)
