# Your code here
import re

with open("robin.txt") as f:
    words = f.read()

# sanitize input
words = words.lower()
words = re.sub(
    r'["|:|;|,|\.|\-|\+|=|\/|\\|\||\[|\]|{|}|\(|\)|\*|\^|&]', r'', words)
words = re.sub(r'[\r|\n|\t]', r' ', words)

# count words
word_count = {}
words_arr = words.split(" ")
longest_word = 0
for word in words_arr:
    if word in word_count:
        word_count[word] += "#"
    else:
        if len(word) > longest_word:
            longest_word = len(word)
        word_count[word] = "#"

# sort dict


def sorter(item):
    return (-len(item[1]), item[0])


sorted_word_count = {k: v for k, v in sorted(
    word_count.items(), key=sorter)}

for item in sorted_word_count.items():
    print(f"{item[0]:{longest_word + 2}} {item[1]}")
