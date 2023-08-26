from tkinter import *
from tkinter import messagebox


root = Tk()
root.title('Calculator App')
root.geometry("750x750")

num = IntVar()
lbbinary = StringVar()
lbdecimal = StringVar()
lbhexa = StringVar()
lboctal = StringVar()

def convert():
    if num.get()==0:
        messagebox.showerror('Error','Enter the number')
    else:
        lbbinary.set(str(bin(num.get())))
        lbdecimal.set(str(num.get()))
        lbhexa.set(str(hex(num.get())))
        lboctal.set(str(oct(num.get())))

def clear():
    num.set(0)
    lbbinary.set('')
    lbdecimal.set('')
    lbhexa.set('')
    lboctal.set('')

def exit():
    if messagebox.askyesno('Exit','Really wanted to exit'):
        root.destroy()



Label(root,text = "Conversion system",font = ('futura',60,'bold'),bg = 'sky blue',fg = 'violet',relief = RIDGE)\
    .pack(pady = 8)
n = Label(root,text = "Enter number",font = ('futura',20,'bold'),fg = 'violet')\
     .place(x=50,y=150)
b = Label(root,text = "Binary",font = ('futura',20,'bold'),fg = 'violet')\
     .place(x=50,y=220)
d = Label(root,text = "Decimal",font = ('futura',20,'bold'),fg = 'violet')\
     .place(x=50,y=290)
h = Label(root,text = "Hexa decimal",font = ('futura',20,'bold'),fg = 'violet')\
     .place(x=50,y=360)
o = Label(root,text = "Octal",font = ('futura',20,'bold'),fg = 'violet')\
     .place(x=50,y=430)


e1 = Entry(root,font = 'futura',fg = 'violet',justify = CENTER,relief = GROOVE,textvariable = num)\
    .place(x=310,y=170)
e2 = Entry(root,font = 'futura',fg = 'violet',justify = CENTER,relief = GROOVE,textvariable = lbbinary)\
    .place(x=310,y=240)
e3 = Entry(root,font = 'futura',fg = 'violet',justify = CENTER,relief = GROOVE,textvariable = lbdecimal)\
    .place(x=310,y=310)
e4 = Entry(root,font = 'futura',fg = 'violet',justify = CENTER,relief = GROOVE,textvariable = lbhexa)\
    .place(x=310,y=380)
e5 = Entry(root,font = 'futura',fg = 'violet',justify = CENTER,relief = GROOVE,textvariable = lboctal)\
    .place(x=310,y=450)


convert = Button(root,text = 'Convert',font = 'futura',fg = 'violet',bg = 'sky blue',width = 10,command = convert)\
    .place(x=70,y=550)
clear = Button(root,text = 'Clear',font = 'futura',fg = 'violet',bg = 'sky blue',width = 10,command = clear)\
    .place(x=270,y=550)
exit = Button(root,text = 'Exit',font = 'futura',fg = 'violet',bg = 'sky blue',width = 10,command = exit)\
    .place(x=470,y=550)

root.mainloop()










