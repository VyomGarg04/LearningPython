"""The Tuple Editor (Type Conversion): We have a tuple: `coordinates = (10, 20, 30)`. Tuples are immutable (cannot be changed). However, we need to change the last value from `30` to `50`. Write a script to:
Convert the tuple into a list.
Change the value in the list.
Convert the list back into a tuple.
Print the final tuple.
"""

coordinates = (10, 20, 30)

coor_list = list(coordinates)#conver

coor_list[2] = 50

coordinates = tuple(coor_list)

print(coordinates)
