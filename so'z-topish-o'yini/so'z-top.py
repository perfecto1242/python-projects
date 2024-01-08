# -*- coding: utf-8 -*-
"""
Created on Mon Jan  8 20:07:27 2024

@author: Shohjaxon Jahonov

So'z topish o'yini
"""
import random
from uzwords import words

def get_word():
    word = random.choice(words)
    while "-" in word or " " in word:
        word = random.choice(words)
    return word.upper()


def display(user_letters,word):
    display_letter=""
    for letter in word:
        if letter in user_letters:
            display_letter += letter
        else:
            display_letter += '-'
    return display_letter


def play():
    word = get_word()
    #So'zdagi harflar
    word_letters = set(word)
    ##Foydalanuvchi kiritgan harflar
    user_letters = ''
    print(f"Мен {len(word)} хонали сўз  ўйладим. Топа оласизми?")
    #print(word)
    while word_letters:
        print(display(user_letters,word))
        if user_letters:
            print(f"Шу вақтгача киритган ҳарфларингиз: {user_letters}")
            
        letter = input("Ҳарф киритинг: ").upper()
        if letter in user_letters:
            print("Bu harfni olding kiritgansiz. Boshqa harf kiriting!")
            continue
        elif letter in word:
            word_letters.remove(letter)
            print(f"{letter} ҳарфи тўғри.")
        else:
            print("Бундай ҳарф йўқ.")
        user_letters += letter
    print(f"Табриклайман! {word} сўзини {len(user_letters)} та уринишда топдингиз")
    

play()