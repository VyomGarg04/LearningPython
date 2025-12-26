'''Cartesian Coordinate System Write a program that takes two numbers, X and Y, as coordinates. Determine the position of the point:
Print "Origin" if both X and Y are 0.
Print "On X-Axis" if Y is 0, but X is not.
Print "On Y-Axis" if X is 0, but Y is not.
Print "Quadrant I" if both X and Y are positive.
Print "Quadrant II" if X is negative and Y is positive.
Print "Quadrant III" if both X and Y are negative.
Print "Quadrant IV" if X is positive and Y is negative.'''


x = input("Enter the X coordinate")
x = int(x)
y = input("Enter the Y coordinate")
y = int(y)

if(x==0 and y==0):
    print("Origin")
elif(x!=0 and y==0):
    print("On X-Axis")
elif(x==0 and y!=0):
    print("On Y-Axis")
elif(x>0 and y>0):
    print("Quadrant I")
elif(x<0 and y>0):
    print("Quadrant II")
elif(x<0 and y<0):
    print("Quadrant III")
else:
    print("Quadrant IV")
