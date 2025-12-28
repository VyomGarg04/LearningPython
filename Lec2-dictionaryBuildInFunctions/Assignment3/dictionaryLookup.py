"""Dictionary Lookup: Create a dictionary called `currency_map` with the following key-value pairs:
"USD": "Dollar"
"EUR": "Euro"
"GBP": "Pound"
Write a program that asks the user to input a currency code (e.g., "USD"). If the code exists, print the currency name. If the code does not exist, print "Currency not found." (Hint: Use the `.get()` method or the `in` keyword).
"""

currency_map = {"USD": "Dollar","EUR": "Euro","GBP": "Pound"}

currency_code = input("Enter currency code ")


if currency_code in currency_map:
    print("Currency =", currency_map[currency_code])
else:
    print("Currency not found")
