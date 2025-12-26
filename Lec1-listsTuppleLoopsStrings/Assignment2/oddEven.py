"""The Odd-Even Separator Given a list of numbers: data = [10, 23, 35, 42, 19, 8, 4]. Write a program using a for loop that iterates through this list and sorts the numbers into two new lists:
even_nums: containing all even numbers.
odd_nums: containing all odd numbers. Print both new lists at the end.
"""

data = [10, 23, 35, 42, 19, 8, 4]
even_nums = []
odd_nums = []
for i in range(0,len(data)):
    if data[i]%2==0:
        even_nums += [data[i]]
    else:
        odd_nums += [data[i]]

print("Even numbers - ",even_nums)
print("Odd numbers - ",odd_nums)