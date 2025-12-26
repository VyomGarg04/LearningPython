"""Tuple Statistics: Create a list of tuples where each tuple represents a product and its price: cart = [("Apple", 0.50), ("Banana", 0.25), ("Milk", 2.00), ("Bread", 1.50)]. Write a program that loops through the cart to calculate and print:
The program should calculate and print the total cost of all items.
The program should output the name of the item that is the most expensive.
"""


cart = [("Apple", 0.50), ("Banana", 0.25), ("Milk", 2.00), ("Bread", 1.50)]
total =0

max_price = cart[0][1]
for i in range(0,len(cart)):
    total += cart[i][1]
    if(float(cart[i][1])>max_price):
        max_price = cart[i][1]
        max_item = cart[i][0]
        


print("Max Price = ",max_price)
print("Item having the max_price price ",max_item)
print("Sum of all the item's price ",total)
