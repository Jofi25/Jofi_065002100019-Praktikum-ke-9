# -*- coding: utf-8 -*-
"""
Created on Sun Nov 21 21:18:35 2021

@author: jofin
"""

print('Ini Merupakan Program Pemangkatan Negatif Dan Positif')

def positif(x) :
       y = int(input('Masukkan Pangkatnya :'))
       pangkat = x ** y
       print('Hasilnya Adalah', pangkat) 

def negatif(x) : 
       y = int(input('Masukkan Pangkatnya :')) 
       pangkat = x ** y
       print('Hasilnya Adalah', pangkat) 
x = int(input('Masukkan Angka :')) 
if x >= 0 :
    positif(x) 
elif x <= 0 :
    negatif(x) 
else :
    print('Tolong Masukkan Angka')