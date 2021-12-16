# take box size
a_length = int(input())
b_width = int(input())
c_height = int(input())

# take doorway size
x_width = int(input())
y_height = int(input())
size_of_doorway = int(x_width) * int(y_height)

# box fits in door
if size_of_doorway >= a_length * b_width or size_of_doorway >= a_length \
        * c_height or size_of_doorway >= b_width * c_height:
    print('The box can be carried')
else:
    print('The box cannot be carried')
