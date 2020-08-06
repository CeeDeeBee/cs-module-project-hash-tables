import re


def word_count(s):
    # Your code here
    str_dict = {}

    s = re.sub(r'[\r|\n|\t]', r' ', s)
    str_arr = s.split(" ")
    for word in str_arr:
        word = word.lower()
        word = re.sub(
            r'["|:|;|,|\.|\-|\+|=|\/|\\|\||\[|\]|{|}|\(|\)|\*|\^|&]', r'', word)

        if word is not '':
            if word in str_dict:
                str_dict[word] += 1
            else:
                str_dict[word] = 1

    return str_dict


if __name__ == "__main__":
    print(word_count(""))
    print(word_count("Hello"))
    print(word_count('Hello, my cat. And my cat doesn\'t say "hello" back.'))
    print(word_count(
        'This is a test of the emergency broadcast network. This is only a test.'))
    print(word_count('":;,.-+=/\\|[]{}()*^&'))
    print(word_count('a a\ra\na\ta \t\r\n'))
