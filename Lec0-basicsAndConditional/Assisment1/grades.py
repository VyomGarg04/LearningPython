'''Grade Classification Write a program that asks the user for a score (integer).
If the score is between 90 and 100 (inclusive), print "A".
If the score is between 80 and 89 (inclusive), print "B".
If the score is between 70 and 79 (inclusive), print "C".
If the score is between 60 and 69 (inclusive), print "D".
If the score is between 0 and 59 (inclusive), print "F".'''




score = input("Enter your marks ")
score = int(score)

if(score>=90 and score<=100):
    print("A")
elif(score>=80 and score<=89):
    print("B")
elif(score>=70 and score<=79):
    print("C")
elif(score>=60 and score<=69):
    print("D")
else:
    print("F")