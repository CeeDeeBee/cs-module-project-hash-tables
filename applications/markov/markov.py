import random
import re

# Read in all the words in one go
with open("input.txt") as f:
    words = f.read()

# TODO: analyze which words can follow other words
# Your code here
word_dict = {}
words = re.sub(r'[\r|\n|\t]', r' ', words)
words_arr = words.split(" ")
for i, word in enumerate(words_arr):
    # skip last val
    if i + 1 < len(words_arr):
        next_word = words_arr[i+1]
        if word in word_dict:
            word_dict[word].append(next_word)
        else:
            word_dict[word] = [next_word]


def construct_sentence():
    start_word = ""
    while True:
        rand_start = random.choice(list(word_dict.values()))[0]
        if rand_start.replace('"', '').isupper():
            start_word = rand_start
            break

    sentence = start_word
    latest_word = start_word
    while True:
        next_word = random.choice(word_dict[latest_word])
        sentence += " " + next_word
        latest_word = next_word
        # check if word is an end word
        check_word = latest_word.replace('"', '')
        if re.match('[^?!.]*[?.!]$', check_word) is not None:
            break

    return sentence


# TODO: construct 5 random sentences
# Your code here
print(construct_sentence() + "\n")
print(construct_sentence() + "\n")
print(construct_sentence() + "\n")
print(construct_sentence() + "\n")
print(construct_sentence() + "\n")
