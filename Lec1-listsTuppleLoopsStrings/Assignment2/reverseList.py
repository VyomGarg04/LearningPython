"""Reverse it manually. Ask the user to enter five distinct numbers and store them in a list. Write a script to reverse the order of the list without using the built-in reverse() method or [::-1] slicing. You must use a loop and logic to create the reversed result."""


list = [5,7,0,4,8,2,4,8,1,3,5]
rev_list = []
n = len(list)
for i in range(0,int(n/2)):
    temp = list[i]
    list[i] = list[n-i-1]
    list[n-i-1] = temp

print(list)