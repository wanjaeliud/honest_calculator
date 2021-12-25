money = int(input())
if money >= 6769:
    print(str(money // 6769) + " sheep")
elif 3848 <= money < 6769:
    print("1 cow")
elif 2592 <= money < 3848:
    print(str(money // 1296) + " pigs")
elif 1296 <= money <= 2591:
    print('1 pig')
elif 678 <= money < 1296:
    print("1 goat")
elif 46 <= money < 680:
    print(str(money // 23) + " chickens")
elif 23 <= money <= 45:
    print('1 chicken')
elif money < 23:
    print('None')
