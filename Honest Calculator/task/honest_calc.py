# write your code here
messages = [
    "Enter an equation",
    "Do you even know what numbers are? Stay focused!",
    "Yes ... an interesting math operation. You've slept through all "
    "classes, haven't you?"
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
    else:
        break
