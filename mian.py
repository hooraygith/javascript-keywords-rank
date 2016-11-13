import re
import os
import nltk
from nltk import word_tokenize

def main():
    list = []
    for file in os.listdir("./articles"):
        print(file)
        with open('./articles/' + file , 'r', encoding='utf-8') as f:
            raw = f.read()
            raw = raw.lower()
            text = word_tokenize(raw)
            list = list + text

    text2 = nltk.FreqDist(list)


    for i in text2.most_common(100):
        print(i)


main()