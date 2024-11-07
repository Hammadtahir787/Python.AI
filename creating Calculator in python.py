from tkinter import *


root = Tk()
root.geometry('644x500')
root.title('Calculator By AI')
root.wm_iconbitmap('1.ico')
root.configure(background='grey')

Scvalue = StringVar()
Scvalue.set(" ")
screen = Entry(root, textvar = Scvalue,font ="Luada 40 bold")
screen.pack(fill=X, ipadx = 8, pady = 10, padx=10)

f=Frame(root,bg="grey")
b=Button(f,text=7,font="Calibri 20 bold",padx="22",pady="28")
b.pack(side=LEFT)
b=Button(f,text=8,font="Calibri 20 bold",padx="22",pady="28")
b.pack(side=LEFT)
b=Button(f,text=9,font="Calibri 20 bold",padx="22",pady="28")
b.pack(side=LEFT)
f.pack()

f=Frame(root,bg="grey")
b=Button(f,text=4,font="Calibri 20 bold",padx="22",pady="28")
b.pack(side=LEFT)
b=Button(f,text=5,font="Calibri 20 bold",padx="22",pady="28")
b.pack(side=LEFT)
b=Button(f,text=6,font="Calibri 20 bold",padx="22",pady="28")
b.pack(side=LEFT)
f.pack()

f=Frame(root,bg="grey")
b=Button(f,text=1,font="Calibri 20 bold",padx="22",pady="28")
b.pack(side=LEFT)
b=Button(f,text=2,font="Calibri 20 bold",padx="22",pady="28")
b.pack(side=LEFT)
b=Button(f,text=3,font="Calibri 20 bold",padx="22",pady="28")
b.pack(side=LEFT)
f.pack()







root.mainloop()
