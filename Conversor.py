from tkinter import *

def converter():
    C= float (lb2.get())
    F=float (lb3.grid)
    lb4.grid(C* 1.8+32)

medi=Tk()
medi.grid_rowconfigure(0,weight=1)
medi.grid_rowconfigure(0,weight=1)
medi.grid_columnconfigure(0,weight=1)
medi.grid_columnconfigure(1,weight=1)

lb1 = Entry(medi)
lb2 = Button(medi, text="converter ", command=converter)
lb3 = Label(medi)
lb4 = Label(medi, text="")

lb1.grid(row=0,column=0, sticky=NSEW)
lb2.grid(row=0,column=0, sticky=NSEW)
lb3.grid(row=0,column=1, sticky=NSEW)
lb4.grid(row=0,column=1, sticky=NSEW)

medi.mainloop()