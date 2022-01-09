# write your code here
messages = [
    "Enter an equation",
    "Do you even know what numbers are? Stay focused!",
    "Yes ... an interesting math operation. You've slept through all "
    "classes, haven't you?",
    "Yeah... division by zero. Smart move..."
]
operation = {"+", "-", "*", "/"}
while True:
    print(messages[0])
    calc = input()
    x, oper, y = calc.split()

    try:
        x = float(x)
        y = float(y)
    except ValueError:
        print(messages[1])
        continue

    if oper not in operation:
        print(messages[2])
        continue

    if oper == '+':
        result = x + y
    elif oper == '-':
        result = x - y
    elif oper == '*':
        result = x * y
    elif oper == '/':
        try:
            result = x / y
        except ZeroDivisionError:
            print(messages[3])
            continue

    print(float(result))
    break
