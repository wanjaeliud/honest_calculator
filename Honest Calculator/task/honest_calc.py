# write your code here
messages = {
    0: "Enter an equation",
    1: "Do you even know what numbers are? Stay focused!",
    2: "Yes ... an interesting math operation. You've slept through al "
       "classes, haven't you"
}
operation = {"+", "-", "*", "/"}
memory = float(0)
while True:
    print(messages[0])
    calc = input()
    x, oper, y = calc.split()
    if x == 'M':
        x = memory
    if y == 'M':
        y = memory

    try:
        x = float(x)
        y = float(y)
    except ValueError:
        print(messages[1])
        continue

    if oper in operation:
        break
    else:
        print(messages[2])
        continue
