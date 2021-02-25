from main.py import *
import os
from tkinter import *
from functools import partial

i = Tk()
i.geometry('400x430')
i.title("Peppanator")
i.iconbitmap("favicon.ico")



def sans():
  s = Tk()
  s.geometry('300x250')
  s.iconbitmap("sans.ico")
  s.title("Saaaanes")
  s.configure(bg='black')
  lb23 = Label(s, text="HEHEHEHEHEHEHEHEHEHEHEHE", bg="black", fg="white")
  lb23.place(x=100, y=100)


def sair():
  i.destroy()
  return
  
def creditos():
  c = Tk()
  c.geometry('300x250')
  c.iconbitmap("favicon.ico")
  c.title("Creditos")
  lb2 = Label(c, text="Thx")
  lb2.place(x=100, y=50)
  lb3 = Label(c, text="Front End: Fagundes")
  lb3.place(x=50, y=100)
  lb4 = Label(c, text="Back End: Mateus Belo Monte")
  lb4.place(x=50, y=120)

def listaper():
  l = Tk()
  l.geometry('530x250')
  l.iconbitmap("favicon.ico")
  l.title("Peppanator lista")
  listalb = Label(l, text="Estes são os persoagens disponíveis: \n\n* Peppa Pig\n* Danny Dog\n* Suzy Sheep\n* Pedro Pony\n* Freddy Fox\n* Emily Elephant\n* George Pig\n* Mommy Pig\n* Candy Cat\n* Rebecca Rabbit")
  listalb.place(x=150, y=50)

img = PhotoImage(file="img.png")
lb_img = Label(i, image=img)
lb_img.place(x=140, y=70)

lb1 = Label(i, text="Texto Principal", bg="black",fg="white")
lb1.place(x=100, y=200)

inst = Label(i, text="Seja bem-vindo ao Peppanator.\nAqui vamos adivinhar em qual personagem\n do mundo Peppa você está pensando.")
inst.place(x=80, y=20)

           
lista = Button(i, width="25",text="Lista de personagens", bg="wheat", fg="blue", command=listaper)
lista.place(x=100, y=350)

true = Button(i, width="25",text="sim", bg="silver", fg="green")
true.place(x=10, y=300) 

false = Button(i, width="25",text="não", bg="silver", fg="red")
false.place(x=195, y=300)

sair = Button(i, width="25",text="sair", bg="black", fg="red", command=sair)
sair.place(x=195, y=400)

creditos = Button(i, width="25",text="Creditos :D", bg="blue", fg="white", command=creditos)
creditos.place(x=10, y=400)

sans = Button(i, width="25",text="😐☠☜",bg="black", fg="white", command=sans)
sans.place(x=195, y=500)


i.mainloop()

