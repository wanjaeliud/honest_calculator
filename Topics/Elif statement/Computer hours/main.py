# Make sure your output matches the assignment *exactly*
hour_spent = int(input())
if hour_spent < 2:
    print("That's rare nowadays!")
elif 2 <= hour_spent < 4:
    print("This seems reasonable")
else:
    print("Don't forget to take breaks!")
