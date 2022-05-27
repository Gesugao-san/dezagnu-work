#!/usr/bin/env python3
# encoding: UTF-8

import tkinter as tk
from tinydb import TinyDB
db = TinyDB('database.json')
table = TinyDB.table(db, 'users')
lst = []

def cal_average(num):
    sum_num = 0
    for t in num:
        sum_num = sum_num + t
    _avg = sum_num / len(num)
    return _avg

def enterItems():
    items = entry.get()
    lst = [int(item) for item in items.split()]
    entry.destroy()
    button.destroy()
    db.insert({'input': lst})
    stored = db.all()
    db.truncate()
    #print(stored)
    avg = cal_average(stored[0]['input'])
    displayText = tk.Text(root)
    displayText.grid()
    displayText.insert('1.0', 'List: ' + str(lst) + '\nAverage: ' + str(avg))


if __name__== "__main__":
    root = tk.Tk()
    entry = tk.Entry(root, text = 'enter array here')
    entry.grid()
    button = tk.Button(root, text = 'submit', command = enterItems)
    button.grid()
    root.mainloop()
