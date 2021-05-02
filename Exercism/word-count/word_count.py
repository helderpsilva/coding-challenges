from collections import Counter
import re

def count_words(sentence):

    clean_sentence = sentence.replace("_", " ").lower()
    regex_find_all_words = re.compile("(\w+(?:'\w{1})?)")
    sentence_words = re.findall(regex_find_all_words,clean_sentence)

    return Counter(sentence_words)
