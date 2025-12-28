

word = input("Input a word you want to check ")

left =0
right = len(word)-1

pal = True
while(left<right):
    if(word[left]!=word[right]):
        print("Not Palindrome")
        pal = False
        break
    left +=1
    right -=1

if pal:
    print("Palindrome")

    