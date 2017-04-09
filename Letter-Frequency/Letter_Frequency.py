# counts the frequency of letters in a word doc

import string

file_name = open(raw_input("What is the file name? "), 'r')

letters = []

for line in file_name:
    for char in line:
        letters.append(char.lower())
file_name.close()

letter_counts = []

for char in string.ascii_lowercase:
    letter_counts.append(letters.count(char))

for n in range(26):
    s = string.ascii_lowercase[n] + ' : '
    for j in range(letter_counts[n]):
        s += 'x'
    print (s)
