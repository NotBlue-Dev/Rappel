# -*- coding: utf-8 -*-
"""
Created on Mon Nov  2 18:40:53 2020

@author: NotBlue
"""
import pandas as pd 
import calendar
from datetime import datetime
import pyttsx3 
now = datetime.now()

dt_string = now.strftime("%H %M")

day = []         
hour = []
days = input('Entrée les jours qui necessite un rappel comme cela : "Monday, Tuesday" \n')    
hours = input("Entrée l'heure et les minutes comme ceci : 18 30 \n")
hour.append(hours)
splited = days.split(',')
day.append(splited)
  

check = calendar.day_name[1]

y = len(splited)

statu = False   

for x in range(y):
    check == day[0][x]
    if True:
        statu = True

if statu == True:
    if dt_string == hours:
        converter = pyttsx3.init() 
  
        converter.setProperty('rate', 150) 

        converter.setProperty('volume', 1) 

        converter.say("Fais tes résponsabilités gros con") 
  
        converter.runAndWait() 
        

    
