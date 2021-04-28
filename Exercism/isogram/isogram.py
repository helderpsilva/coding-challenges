import string as s

def is_isogram(string):
    text = [c for c in string.lower() if c in s.ascii_lowercase]
    return len(text) == len(set(text))