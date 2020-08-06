def no_dups(s):
    # Your code here
    seen_words = []
    word_arr = s.split(" ")

    for word in word_arr:
        if word not in seen_words:
            seen_words.append(word)

    return " ".join(seen_words)


if __name__ == "__main__":
    print(no_dups(""))
    print(no_dups("hello"))
    print(no_dups("hello hello"))
    print(no_dups("cats dogs fish cats dogs"))
    print(no_dups("spam spam spam eggs spam sausage spam spam and spam"))
