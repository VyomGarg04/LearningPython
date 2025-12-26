'''Triangle Type Checker Write a program that takes three integers as input representing the sides of a triangle.
First, determine if the sides can form a valid triangle (the sum of any two sides must be greater than the third). If they cannot, print "Not a valid triangle".
If the triangle is valid, verify the following:
Print "Equilateral" if all three sides are the same.
Print "Isosceles" if exactly two sides are the same.
Print "Scalene" if all three sides are different.'''


side1 = input("Enter the first side ")
side1 = int(side1)
side2 = input("Enter the second side ")
side2 = int(side2)
side3 = input("Enter the third side ")
side3 = int(side3)


if(side1+side2<side3 and side2+side3<side1 and side1+side3<side2):
    print("Triangle not valid")
else:
    if(side1==side2 and side2==side3):
        print("Equilateral")
    elif((side1==side2 and side2!=side3)or(side1==side3 and side2!=side3)or(side3==side2 and side1!=side3)):
        print("Isosceles")
    else:
        print("Scalene")