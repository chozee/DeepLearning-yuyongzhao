# -*- coding:utf-8 -*-


# text = urlopen(WORD_URL).read
# print text.
fileName = "word"

def readFile(fileName):
    file = open(fileName)
    text = file.read().split()
    return text

def sortedByValueDesc(your_dict):
    return sorted(your_dict.items(), lambda x, y: cmp(x[1], y[1]), reverse=True)

def countWord(text):
    words_dict = {}
    for word in readFile(fileName):
        if len(word.strip()) == 6:
            if word in words_dict:
                words_dict[word] +=1
            else:
                words_dict[word] = 1
    return words_dict

myWordCountDict=countWord(readFile(fileName))
sortedLit = sortedByValueDesc(myWordCountDict)[:10]

for k in sortedLit:
    print "%s=%d" % (k[0], k[1])