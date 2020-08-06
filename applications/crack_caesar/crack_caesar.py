# Use frequency analysis to find the key to ciphertext.txt, and then
# decode it.

# Your code here
standard_frequencies = ["E", "T", "A", "O", "H", "N", "R", "I", "S", "D", "L",
                        "W", "U", "G", "F", "B", "M", "Y", "C", "P", "K", "V", "Q", "J", "X", "Z"]

with open("ciphertext.txt") as f:
    words = f.read()

letter_count = {}
for char in words:
    if char.isalpha():
        if char in letter_count:
            letter_count[char] += 1
        else:
            letter_count[char] = 1

sorted_count = {k: v for k, v in sorted(
    letter_count.items(), key=lambda item: item[1], reverse=True)}

cypher_map = {}
for i, key in enumerate(sorted_count.keys()):
    cypher_map[key] = standard_frequencies[i]

for char in words:
    if char.isalpha():
        print(cypher_map[char], end="")
    else:
        print(char, end="")
