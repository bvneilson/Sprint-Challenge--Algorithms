'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):
    th_count = 0

    #removes (num) characters from beginning of string
    def remove_chars(word, num):
        new_word = word[num:]
        return new_word

    # TBC
    if len(word) < 2:
        return th_count
    else:
        if word[0] == 't' and word[1] == 'h':
            return 1 + count_th(remove_chars(word, 2))
        else:
            return count_th(remove_chars(word, 1))
