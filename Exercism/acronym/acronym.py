def abbreviate(words):
    clean_words = words.replace('-',' ').replace('_',' ').strip().split()

    return ''.join([word[0].upper() for word in clean_words])
