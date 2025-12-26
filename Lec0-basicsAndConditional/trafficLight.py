

def trafficLight(color):
    if(color == "red"):
        print("Stop")
    elif(color== "yellow"):
        print("Wait")
    elif(color=="green"):
        print("Go")
    else:
        print("Invalid Color")


color = input("Enter a color")
trafficLight(color)
        
