# -*- coding: utf-8 -*-
"""
Created on Fri Sep 13 23:48:02 2019

@author: hugo_
"""
from datetime import date

def inputAge(age):
    today = date.today()
    d1 = today.strftime("%d/%m/%Y")
    d1 = d1.split("/")
    currentYear = d1[2]
    remainderYears = 99 - age
    output = int(currentYear) + remainderYears
    d1[2] =  str(output)
    #d1.reverse()
    #d1 = "/".join(d1)
    return print("At the year %s you'll be 100 years old!" % d1[2])

#inputAge(23)
name = input("Input name: ")
inputAge(int(input("Input age: " )))
