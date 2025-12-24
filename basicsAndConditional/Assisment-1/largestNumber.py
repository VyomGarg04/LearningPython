# Determine the Largest Number: Write a program that accepts three distinct integers from the user.
# Using only if, elif, and else statements (do not use the max() function), compare the three numbers.
# Determine and print the largest of the three numbers.

a = input("Enter 1st number")
a = int(a)
b = input("Enter 2nd number")
b = int(b)
c = input("Enter 3rd number")
c = int(c)

if(a>b):
    if(a>c):
        print("Greatest = ",a)
    else:
        print("Greatest = ",c)
else:
    if(b>c):
        print("Greatest = ",b)
    else:
        print("Greatest = ",c)
