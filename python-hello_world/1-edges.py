
word = "Holberton"
word_first_3 = word[:3]
word_last_2 = word[-2:]
middle_start = len(word) // 2 - 1
middle_end = middle_start + 3
middle_word = word[middle_start:middle_end]
print("First 3 letters: {}".format(word_first_3))
print("Last 2 letters: {}".format(word_last_2))
print("Middle word: {}".format(middle_word))

