#!/usr/bin/env python3
# encoding: UTF-8

import sys
from tkinter import *
from functools import reduce
import operator
root=Tk()
root.geometry("600x300")
digital=Label(root,text="Введите цифры",font="times 24 bold")
digital.grid(row=0,column=2)

def clicked():
    res = "Цифорки {}".format(number.get())
    nota.configure(text=res)
    nums = int(number.get())
    print (nums)

def Midline():
    mid = "Цифроки {}".format(number.get())
    mid.len = len(number.get().lst)
    mid.avg = reduce(operator.add, number.lst) / mid.len
    nota.configure(text=mid)


nota=Label(root, text='Цифорки', font="times 15 bold")
nota.grid(row=3,column=2)

number = Entry(width=10)
number.grid(row=4,column=2)

btn = Button(text="Вписать!", command=clicked)
btn.grid(row=5,column=2)

btn = Button(text="Среднее!", command=Midline)
btn.grid(row=5,column=3)

root.mainloop()
