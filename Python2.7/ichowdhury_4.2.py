#!/usr/bin/env python
word_filename = 'C:\Users\Iftekhar Chowdhury\Desktop\Python\words.txt'
sawyer_filename ='C:\Users\Iftekhar Chowdhury\Desktop\Python\sawyer.txt'

wordset = set([])

def prepare_word(word):
    word = word.rstrip(';,.?!')
    word = word.lower()
    return word

def get_spelling_word(word_filename):   
   
    fh = open(word_filename)
    words = fh.read().split()
    for word in words:
        
        word = prepare_word(word)
        wordset.add(word)
    fh.close()
   
    return word

def report_misspellings(wordset,sawyer_filename):
    
    fh = open(sawyer_filename)
    test_words = fh.read().split()
    for word in test_words:
        word = prepare_word(word)
        wrdset = get_spelling_word(word_filename)
        if word not in wordset:
            print word
    return word

val = report_misspellings(wordset,sawyer_filename)
print val 

    
    
    
