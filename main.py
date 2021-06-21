import tkinter.messagebox as mb
from tkinter import *
import random

fieldsize = 10
cagesize = 70
numbersofmines = 10
mines = set(random.sample(range(1, fieldsize**2+1), numbersofmines))
clicked = set()

def check_mines(neighbors):
    return len(mines.intersection(neighbors))

def generate_neighbors(square):
    if square == 1:
        data = {fieldsize + 1, 2, fieldsize + 2}
    elif square == fieldsize ** 2:
        data = {square - fieldsize, square - 1, square - fieldsize - 1}
    elif square == fieldsize:
        data = {fieldsize - 1, fieldsize * 2, fieldsize * 2 - 1}
    elif square == fieldsize ** 2 - fieldsize + 1:
        data = {square + 1, square - fieldsize, square - fieldsize + 1}
    elif square < fieldsize:
        data = {square + 1, square - 1, square + fieldsize,
                square + fieldsize - 1, square + fieldsize + 1}
    elif square > fieldsize ** 2 - fieldsize:
        data = {square + 1, square - 1, square - fieldsize,
                square - fieldsize - 1, square - fieldsize + 1}
    elif square % fieldsize == 0:
        data = {square + fieldsize, square - fieldsize, square - 1,
                square + fieldsize - 1, square - fieldsize - 1}
    elif square % fieldsize == 1:
        data = {square + fieldsize, square - fieldsize, square + 1,
                square + fieldsize + 1, square - fieldsize + 1}
    else:
        data = {square - 1, square + 1, square - fieldsize, square + fieldsize,
                square - fieldsize - 1, square - fieldsize + 1,
                square + fieldsize + 1, square + fieldsize - 1}
    return data

def clearance(ids):
    clicked.add(ids)
    ids_neigh = generate_neighbors(ids)
    around = check_mines(ids_neigh)
    c.itemconfig(ids, fill="green")

    if around == 0:
        neigh_list = list(ids_neigh)
        while len(neigh_list) > 0:
            item = neigh_list.pop()
            c.itemconfig(item, fill="green")
            item_neigh = generate_neighbors(item)
            item_around = check_mines(item_neigh)
            if item_around > 0:
                if item not in clicked:
                    x1, y1, x2, y2 = c.coords(item)
                    c.create_text(x1 + cagesize / 2,
                                  y1 + cagesize / 2,
                                  text=str(item_around),
                                  font="Arial {}".format(int(cagesize / 2)),
                                  fill='yellow')
            else:
                neigh_list.extend(set(item_neigh).difference(clicked))
                neigh_list = list(set(neigh_list))
            clicked.add(item)
    else:
        x1, y1, x2, y2 = c.coords(ids)
        c.create_text(x1 + cagesize / 2,
                      y1 + cagesize / 2,
                      text=str(around),
                      font="Arial {}".format(int(cagesize / 2)),
                      fill='yellow')

def finish():
    mb.showwarning("Вы проиграли! Игра завершена.")
    exit(0)

def click(event):
    ids = c.find_withtag(CURRENT)[0]
    if ids in mines:
        c.itemconfig(CURRENT, fill="red")
        c.after(1000, lambda: finish())
        # time.sleep(4)
    elif ids not in clicked:
        clearance(ids)
        c.itemconfig(CURRENT, fill="green")
    c.update()

def mark_mine(event):
    ids = c.find_withtag(CURRENT)[0]
    if ids not in clicked:
        clicked.add(ids)
        x1, y1, x2, y2 = c.coords(ids)
        c.itemconfig(CURRENT, fill="yellow")
    else:
        clicked.remove(ids)
        c.itemconfig(CURRENT, fill="gray")

root = Tk()
root.title("GRYN_BSBO-05-19")
c = Canvas(root, width=fieldsize * cagesize, height=fieldsize * cagesize)
c.bind("<Button-1>", click)
c.bind("<Button-3>", mark_mine)
c.pack()

for i in range(fieldsize):
    for j in range(fieldsize):
      c.create_rectangle(i * cagesize, j * cagesize,
                         i * cagesize + cagesize,
                         j * cagesize + cagesize, fill='gray')
root.mainloop()