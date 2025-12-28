

word = input("Input a word you want to check")
rev_word = ""

for i in range(len(word)-1,-1,-1):
    rev_word += word[i]

if(rev_word==word):
    print("Palindrome")
else:
    print("Not Palindrome")