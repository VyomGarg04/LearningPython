"""The String Cleaner: Write a program that takes the messy string: `raw_data = "  Python, Java, C++, Ruby  "`. Using only built-in string methods (like `.strip()`, `.replace()`, and `.split()`), write a script to:
Remove the leading and trailing spaces.
Replace the commas with distinct pipe characters (`|`).
Split the string into a list of individual language names.
Print the final list.
"""

raw_data = "  Python, Java, C++, Ruby  "

print("Original Data ",raw_data)
new_data = raw_data.strip()#removes the headind and taling characters
print("After removing heading and tailing spaces ",new_data)
print("After replacing , with | ",new_data.replace(",","|"))#replaces a character with another
print("Final Data",new_data.split(","))#splits the string when a perticular character is encountered
