# -*- coding: utf-8 -*-
"""Untitled1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1L0w1_Vix9RkdNwkklGEKk4YOdbBjkaay
"""

#Intorduction to Pyhon Homework2 - CV dictionaries
#Created by Mutlu Senturk

CV_mutlusenturk={'name':'Mutlu','surname':'Senturk','email':'senturkmutlu@gmail.com',
          'university':'Istanbul Technical University','occupation':'Mechatronic Engineer',
          'languages':['Turkish, English'],'technical_skills':['MATLAB','Python','AutoDesk Fusion360']}

CV_denizsenturk={'name':'Deniz','surname':'Senturk','email':'denizsenturk@gmail.com',
          'university':'Mimar Sinan Fine Arts University','occupation':'Turkish Literature',
          'languages':['Turkish, English','Bulgarian'],'technical_skills':['MS Office Tools']}

CV_canerguven={'name':'Caner','surname':'Guven','email':'canerguven@gmail.com',
          'university':'Middle East Technical University','occupation':'Automotive Engineer',
          'languages':['Turkish, English','German'],'technical_skills':['MATLAB','Solidworks']}

CV_altanozgur={'name':'Altan','surname':'Ozgur','email':'altanozgur@gmail.com',
          'university':'Yildiz Technical University','occupation':'Desing Engineer',
          'languages':['Turkish, English','Bulgarian'],'technical_skills':['Catia','3DSMax']}

CV_cansungur={'name':'Can','surname':'Sungur','email':'cansungur@gmail.com',
          'university':'Istanbul Technical University','occupation':'NVH Engineer',
          'languages':['Turkish, English','German'],'technical_skills':['AVL Acoustics']}

All_CV=[CV_mutlusenturk,CV_denizsenturk,CV_canerguven,CV_altanozgur,CV_cansungur]

for CV in All_CV:

    for value,key in CV.items():
        print(value +': ',key)