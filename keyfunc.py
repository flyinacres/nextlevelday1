'''
Use max, min, and sorted along with key functions to implement the
following functions and make the tests pass.

>>> most_spaces(["a", "a b", "a b c", "c", "abc"])
'a b c'

>>> one_line_poems = [
...      "The dogs are barking at the stillness, the stillness is still.",
...      "In the canopy of the night heaven the stars are tiptoeing.",
...      "A sunrise smiles wide into my expectant face.",
...      "The bees are awakening to the life in a yellow wonder!",
...      "The land runs astoundingly under my soles.",
...      "The dance of the flowers kissed by the butterflies.",
... ]

>>> fewest_vowels(one_line_poems)
'The land runs astoundingly under my soles.'

>>> most_consonants(one_line_poems)
'The dogs are barking at the stillness, the stillness is still.'

>>> for poem in sorted_by_word_count(one_line_poems):
...     print(poem)
The land runs astoundingly under my soles.
A sunrise smiles wide into my expectant face.
The dance of the flowers kissed by the butterflies.
The dogs are barking at the stillness, the stillness is still.
In the canopy of the night heaven the stars are tiptoeing.
The bees are awakening to the life in a yellow wonder!

EXTRA CREDIT:
Once you get this lab to pass, read about lambda expressions in the
Python docs:
https://docs.python.org/3/tutorial/controlflow.html#lambda-expressions

Modify your code to use lambda expressions instead of separately defined key functions.

'''

# Write your code here:

def most_spaces(words):
    return max(words, key=len)

def count_vowels(line):
    vc = 0
    for c in line:
        if c in ['a', 'e', 'i', 'o', 'u']:
            vc = vc + 1
    return vc

def count_consts(line):
    vc = 0
    for c in line:
        if c not in ['a', 'e', 'i', 'o', 'u']:
            vc = vc + 1
    return vc

def fewest_vowels(lines):
    return min(lines, key=count_vowels)

def most_consonants(a):
    return max(a, key=count_consts)
    return

def word_count(line):
    words = line.split(" ")
    return len(words)

def sorted_by_word_count(lines):
    return sorted(lines, key=word_count)


# Do not edit any code below this line!

if __name__ == '__main__':
    import doctest
    count, _ = doctest.testmod()
    if count == 0:
        print('*** ALL TESTS PASS ***\nGive someone a HIGH FIVE!')

# Copyright 2015-2018 Aaron Maxwell. All rights reserved.
