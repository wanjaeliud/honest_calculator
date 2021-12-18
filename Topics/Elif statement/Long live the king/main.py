three = [(1, 1), (1, 8), (8, 1), (8, 8)]
five = []


def append_to_five(j):
    for i in range(2, 8):
        five.append((i, j))
        five.append((j, i))


append_to_five(1)
append_to_five(8)

print(five)

vector = (int(input()), int(input()))

print(vector)

if vector in three:
    print('3')
elif vector in five:
    print('5')
else:
    print('8')
