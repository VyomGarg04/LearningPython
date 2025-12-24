

def eligible(age):
    if(age>=18):
        print("Eligible")
    else:
        print("Not eligible")


age = input("Enter the age of the voter : ")
age = int(age)
eligible(age)