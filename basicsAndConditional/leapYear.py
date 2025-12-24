# Leap Year Calculator Write a program that asks for a year as input. Determine if it is a leap year based on these conditions:
# A year is a leap year if it is exactly divisible by 4.
# However, if the year is divisible by 100, it is not a leap year, unless it is also divisible by 400.
# Print "Leap Year" or "Not a Leap Year".


year = input("Enter a year ")
year = int(year)

if(year%4==0):
    if(year%100==0):
        if(year%400==0):
            print("Leap Year")
        else:
            print("Not Leap Year")
    else:
        print("Leap Year")
else:
    print("Not leap year")
        