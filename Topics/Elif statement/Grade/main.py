score = float(input())
maximum = float(input())
percentage = (score / maximum) * 100

if 90 <= percentage <= 100:
    print("A")
elif 80 <= percentage <= 89.9:
    print("B")
elif 70 <= percentage <= 79.9:
    print("C")
elif 60 <= percentage <= 69.9:
    print("D")
else:
    print("F")
