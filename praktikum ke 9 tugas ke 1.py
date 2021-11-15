# -*- coding: utf-8 -*-
"""
Created on Mon Nov 15 13:17:06 2021

@author: jofin
"""

def faktor(a = 0, j = 0 , p = 1):
    if (j <= 0):
        return 0
    else:
        a = int(input('Masukkan Angka ke-'+str(p)+':'))
        if(j == 1):
            return a

        else:
            p += 1
            return a + faktor (a , j-1, p)

jum = int(input('Masukan Jumlah:'))
nilai = faktor(j = jum)
print('Hasil dari Penjumlahan adalah:'+ str(nilai))
