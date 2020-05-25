import sys
import re

if len(sys.argv) != 3:
    print('ERROR')

text = sys.argv[1]
try:
    n = int(sys.argv[2])

    words_list = re.split(r' |\.|\,|\;|\:|\'|\(|\)|\!|\?', text)
    new_words_list = list(filter(lambda x: len(x) > n, words_list))
    print(new_words_list)
except ValueError:
    print('ERROR')
