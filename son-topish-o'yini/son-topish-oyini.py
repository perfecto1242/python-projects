# -*- coding: utf-8 -*-
"""
Created on Sun Jan  7 19:42:09 2024

@author: Shohjaxon Jahonov

Python / Son topish o'yini
"""
import random

def son_top(x=10):
    tasodifiy_son = random.randint(1,x)
    print(f"Men 1 dan {x} gacha son o'yladim.Topa olasizmi?", end="")
    taxminlar = 0
    while True:
        taxminlar += 1
        taxmin = int(input(">>>"))
        if taxmin<tasodifiy_son:
            print("Xato.Men o'ylagan son bundan katta,yana urinib ko'ring: ", end="")
        elif taxmin>tasodifiy_son:
            print("Xato.Men o'ylagan son bundan kichik, yana urinib ko'ring: ", end="")
        else:
            break
        
    print(f"Tabriklayman.Men o'ylagan son {taxmin} edi.To'g'ri topdingiz.Siz bu sonni {taxminlar}ta taxmin bilan topdingiz")
    return taxminlar
            
    
def son_top_pc(x=10):
    input(f"1 dan {x} gacha son o'ylang va istalgan tugmani bosing.Men topaman.")
    quyi  = 1
    yuqori = x
    taxminlar = 0
    while True:
        taxminlar += 1
        if quyi != yuqori:
            taxmin = random.randint(quyi,yuqori)
        else:
            taxmin = quyi
        javob = input(f"\nSiz {taxmin} sonni o'yladingiz: to'gri (t),"
                      f"men o'ylagan son bundan kattaroq (+),yoki kichikroq (-)".lower())
        if javob == "-":
            yuqori = taxmin - 1 
        elif javob == "+":
            quyi = taxmin + 1
        else:
            break
    print(f"Men {taxminlar} ta taxmin bilan topdim")
    return taxminlar
        
def play(x=10):
    yana = True
    while yana:
        taxminlar_user = son_top(x)
        taxminlar_pc = son_top_pc(x)
    
        if taxminlar_user>taxminlar_pc:
            print(f"Men {taxminlar_pc} ta taxmin bilan topdim va yutdim")
        elif taxminlar_user<taxminlar_pc:
            print(f"Siz {taxminlar_user} ta taxmin bilan topdingiz va yutdingiz") 
        else:
            print("Durrang!")
        yana = int(input("Yana o'ynaysizmi: ha(1)/yo'q(0): "))
        
        
play()
        