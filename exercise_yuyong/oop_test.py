import random
from urllib import urlopen
import sys

WORD_URL = "http://learncodethehardway.org/words.txt"
WORDS = []

PHRASES = {
    "class %%%(%%%):":
      "Make a class named %%% that is-a %%%.",
    "class %%%(object):\n\tdef __init__(self, ***)" :
      "class %%% has-a __init__ that takes self and *** parameters.",
    "class %%%(object):\n\tdef ***(self, @@@)":
      "class %%% has-a function named *** that takes self and @@@ parameters.",
    "*** = %%%()":
      "Set *** to an instance of class %%%.",
    "***.***(@@@)":
      "From *** get the *** function, and call it with parameters self, @@@.",
    "***.*** = '***'":
      "From *** get the *** attribute and set it to '***'."
}

def convert(snippet, phrase):
    class_names = [w.capitalize() for w in
                   random.sample(WORDS, snippet.count("%%%"))]
    print 'class_names==>', class_names
    print 'snippet.count("%%%")==>', snippet.count("%%%")
    print 'random.sample(WORDS, snippet.count("%%%")==>', random.sample(WORDS, snippet.count("%%%"))
    for w in random.sample(WORDS, snippet.count("%%%")):
        print w.capitalize()
        print w

for word in urlopen(WORD_URL).readlines():
    WORDS.append(word.strip())

print WORDS.count('cat')
print random.sample(WORDS, 1)
print random.sample(WORDS, 2)
print random.sample(WORDS, 3)

param_names = []
param_names.append(', '.join(random.sample(WORDS, 3)))
print param_names
#
# snippets = PHRASES.keys()
# print 'before shuffle snippets:', snippets
# random.shuffle(snippets)
# print 'before shuffle snippets:', snippets
#
# for snippet in snippets:
#     phrase = PHRASES[snippet]
#     convert(snippet, phrase)