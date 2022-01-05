# user_input_time = int(input())

# if user_input_time in [-11, -12]:
#     print('Monday')
# elif user_input_time in [14]:
#     print('Wednesday')
# elif user_input_time in [-10, -9, -8, -7, -6, -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]:
#     print("Tuesday")


offset = int(input())

if offset > 13:
    print('Wednesday')
elif offset < -10:
    print('Monday')
else:
    print('Tuesday')
