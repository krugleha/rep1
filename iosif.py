# -*- coding: utf-8 -*-
"""
Created on Wed Nov  6 03:21:30 2019

@author: User
"""

n = int(input())  # кол-во людей в круге
m = int(input())  # какого по счету убивают(если 3, то убивают 3, 6, 1 и тд)

a = [1] * n

s = 0
while sum(a) > 0:
    for i in range(len(a)):
        if a[i] == 1:
            s += 1
        if s == m:
            a[i] = 0
            s = 0

        # проверка
#        if sum(a)==3:
#            print(a)
#        if sum(a)==2:
#            print(a)
#        if sum(a)==1:
#            print(a)
        
        # вывод индексов трех победителей
        if sum(a) == 3:
            b3 = set()
            for j3 in range(len(a)):
                if a[j3] == 1:
                    b3.add(j3+1)
        if sum(a) == 2:
            b2 = set()
            for j2 in range(len(a)):
                if a[j2] == 1:
                    b2.add(j2+1)
        if sum(a) == 1:
            b1 = set()
            for j1 in range(len(a)):
                if a[j1] == 1:
                    b1.add(j1+1)


print(b1)  # win
print(b2-b1)
print(b3-b2)