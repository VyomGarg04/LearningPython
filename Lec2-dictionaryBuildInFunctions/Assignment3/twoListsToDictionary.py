"""List to Dictionary (Zipping): You are given two lists of equal length: 
```python 
students = ["Alice", "Bob", "Charlie"] 
grades = [85, 90, 78]```
Write a program that combines these two lists into a single dictionary, where the student names serve as keys, and the grades are the corresponding values. Print the final dictionary.
"""

students = ["Alice", "Bob", "Charlie"] 
grades = [85, 90, 78]

std_dict ={}

for i in range(len(students)):
    std_dict[students[i]] = grades[i]

# std_dict = dict(zip(students, grades))

print(std_dict)
