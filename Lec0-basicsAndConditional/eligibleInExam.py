

attendanceEst = input("Enter your attendance percentage ")
attendanceEst = int(attendanceEst)
marks = input("Enter your marks ")
marks = int(marks)
fees = input("Have you paid the fees ")

if(attendanceEst>=80):
    if(marks>=50):
        if(fees == "yes"):
            print("Eligible to give exam ")
        else:
            print("Not eligible ")
    else:
        print("Not eligible ")   
else:
    print("Not eligible ")

