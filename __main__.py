

import tkinter as tk
lst = []

def enterItems():
    items = entry1.get()
    lst = [int(item) for item in items.split()]
    entry1.destroy()
    button.destroy()
    sum_num = 0
    for t in lst:
        sum_num = sum_num + t
    avg = sum_num / len(lst)
    displayText = tk.Text(root)
    displayText.grid()
    displayText.insert('1.0', 'List 1:\n' + str(lst) + '\nAverage: ' + str(avg))


if __name__== "__main__":
    root = tk.Tk()
    entry1 = tk.Entry(root, text = 'enter array here')
    entry1.grid()
    button = tk.Button(root, text = 'submit', command = enterItems)
    button.grid()
    root.mainloop()
