king_column = int(input())
king_row = int(input())

if king_column in [1, 8] and king_row in [1, 8]:
    print("3")
elif king_column in [1, 8] and king_row not in [1, 8] or king_column not in [1, 8] and king_row in [1, 8]:
    print("5")
else:
    print("8")
