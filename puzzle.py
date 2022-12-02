import math
from datetime import datetime
import numpy as np
import itertools
import os.path

def save_unique_seven(words):
    print("Create array with 'unique' 7-letter words")
    words_unique = np.array([])
    for index, word in enumerate(words):
        print('\r', str(round((index / len(words)) * 100, 1)) + '%', end='')
        unique = True
        for v in itertools.permutations(word):
            check_word = ''.join(v)
            if word == check_word:
                continue
            if check_word in words:
                unique = False
                break
        if unique:
            words_unique = np.append(words_unique, word)
    np.savetxt('seven_unique.txt', words_unique, '%s')


four_letter_words = np.loadtxt('four_letter_words.txt', 'str')
seven_letter_words = np.loadtxt('seven_letter_words.txt', 'str')
print("# of 4-letter words:", len(four_letter_words))
print("# of 7-letter words:", len(seven_letter_words))

# if file with unique seven-letter words don't exist
if os.path.isfile('./seven_unique.txt') is False:
    save_unique_seven(seven_letter_words)

seven_unique = np.loadtxt('seven_unique.txt', 'str')
print("# of unique 7-letter words:", len(seven_unique))

# create alphabetically ordered 7-letter word set
# for example trucker -> cekrtu
seven_ordered = []
seven_lookup = {}
for word in seven_unique:
    seven_ordered.append(''.join(sorted(word)))
    seven_lookup[''.join(sorted(word))] = word
seven_set = set(seven_ordered)

# four_letter_words = np.loadtxt('tekst.txt', 'str')
nr_of_combs = math.comb(len(four_letter_words),7)
print(nr_of_combs, "combinations with all 4 letter words")

# randomize words as a test
four_letter_words = np.random.permutation(four_letter_words)

dt = datetime.now()
print("Start script:", dt.strftime("%Y-%m-%d %H:%M:%S") )
print("check all combinations of 4-letter words for existing seven-letter words")
ind = 0
for a in itertools.combinations(four_letter_words, 7):
    ind += 1
    # print('\r', str(round((ind / nr_of_combs) * 100, 10)) + '%', end='')
    correct = True
    for x in range(0, 4):
        check_string = a[0][x] + a[1][x] + a[2][x] + a[3][x] + a[4][x] + a[5][x] + a[6][x]
        check_sorted = ''.join(sorted(check_string))
        if check_sorted not in seven_set:
            correct = False
            break
        else:
            print('\r', str(ind), end='')
    if correct:
        f = open("options.txt", "a")
        dt = datetime.now()
        f.write(dt.strftime("%Y-%m-%d %H:%M:%S") + " " + ' '.join(a) + "\n")
        f.close()
