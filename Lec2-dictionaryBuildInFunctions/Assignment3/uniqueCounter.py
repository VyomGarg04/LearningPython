"""The "Unique" Counter: Ask the user to input a sentence (e.g., "hello world hello python"). Write a script that:
Splits the sentence into a list of words.
Uses a dictionary to count how many times each word appears.
Print the dictionary.*(Example Output: `{'hello': 2, 'world': 1, 'python': 1}`)*
"""

freq = {}

def frequency(list_data):
    for i in range(len(list_data)):
        if freq[list_data[i]] == freq[i]:
            freq[i] +=1
        else:
            freq[i] = 1
    return freq


inp_str = input("Enter a string")

list_data = inp_str.split()
print("List of Words = ",list_data)

print("Frequency = ",frequency(list_data))