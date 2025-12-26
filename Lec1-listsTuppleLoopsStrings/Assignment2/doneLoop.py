"""The "Done" Loop Write a program using a while loop that continuously asks the user to enter a number.
The loop should continue running until the user types the word "done."
Once they type "done," the loop stops, and the program prints the sum of all the numbers entered.
"""

user_input = input("Enter a number or done to stop ")
sum=0
while(user_input!="done"):
    sum += int(user_input)
    user_input = input("Enter a number or done to stop ")

print("Sum of values = ",sum)