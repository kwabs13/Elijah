#!/usr/bin/python
from random import shuffle

def main():
    sentence = raw_input('Please enter a word or a sentence: ')
    words = sentence.split(' ')
    # print(words)
    scramblesentence = ''
    for word in words:
        scramblesentence = scramblesentence + ' ' + scrambleWord(list(word))
    print(scramblesentence)

def scrambleWord(letters_list):    
    if len(letters_list) < 2:
        return ''.join(letters_list)
    elif letters_list[-1] == ".":
        sub_list = letters_list[1:-2]    
        shuffle(sub_list)
        scrambledWord_str = ''.join(sub_list) 
        return letters_list[0] + scrambledWord_str + letters_list[-2] + "."
    elif letters_list[-1] == ",":
        sub_list = letters_list[1:-2]    
        shuffle(sub_list)
        scrambledWord_str = ''.join(sub_list) 
        return letters_list[0] + scrambledWord_str + letters_list[-2] + ","
    else:
        sub_list = letters_list[1:-1]    
        shuffle(sub_list)
        scrambledWord_str = ''.join(sub_list) 
        return letters_list[0] + scrambledWord_str + letters_list[-1]
main()
