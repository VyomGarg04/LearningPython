# 0 1 1 2 3 5 8 13 ....

n = input("Enter a number")
n = int(n)

a=0
b=1
print(a)
print(b)
i=0
for i in range(2, n): 
    b=a+b
    print(b)
    a=b-a