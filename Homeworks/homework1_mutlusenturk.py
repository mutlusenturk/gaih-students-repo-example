# -*- coding: utf-8 -*-
"""Untitled0.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Hm-2KCMSfa7Yppw65r2pkeoBKVf2KjYA
"""

#Introduction to Pyhton Homework1 by Mutlu Senturk

#list of odd numbers
list1=list(range(1,20,2))
#list of even numbers
list2=list(range(2,21,2))
#merge list
list3=list1+list2
#multiply by 2
list4=[num*2 for num in list3] 

#print the data type
for num in list4:
    print(type(num))