from googletrans import Translator
from tkinter import *
from langs import langs, lgcd  # lgcd - stands for language code
from pyperclip import copy, paste
from tkinter import ttk


r = Tk()
tr = Translator()

r.title('Translator')

r.config(bg='SpringGreen2')

# r.geometry('530x600')
# r.resizable(0,0)

global lang
lang = "English"


def translate(x):
	global lang
	output = tr.translate(x, dest=lgcd(lang)).text
	out.config(state='normal')
	out.delete(1.0, END)
	out.insert(1.0, output)
	out.config(state='disabled')


frame2 = Frame(r, bg='SpringGreen2')

Label(frame2, text=' Write Your Input ', font='Times 14 underline').grid(row=0, column=0, pady=5)

def pastec():
	inp.insert(END, paste())

def copyc():
	copy(inp.get(1.0,END))

inp = Text(frame2, width=40, height=9,font=('Helvetica',14))
inp.config()
inp.grid(column=0,row=1, padx=35, pady=5)

menu = Menu(r, tearoff=0)

menu.add_command(label='paste', command=pastec)
menu.add_command(label='copy all', command=copyc)

def menucr(event):
	menu.tk_popup(event.x_root, event.y_root)

inp.bind('<Button-3>', menucr)
inp.bind('<Control-c>', lambda x:pastec)

frame2.grid(row=0, column=0, pady=20)
options = []

for x,y in langs.items():
	options.append(x)

Label(r, text='Translate to', font=('Arial', 12)).grid(column=0, row=2)

select = ttk.Combobox(r, values=options, font=('Arial',12))
select.current(21)
select.grid(column=0, row=3,ipady=8, ipadx=4)


def selected(event):
	global lang
	lang = select.get()

select.bind('<<ComboboxSelected>>', selected)


transbtn = Button(text='Translate', command=lambda:translate(inp.get (1.0,END)))
transbtn.config(width=19, height=1, font=('Helvetica',12))
transbtn.config(relief='solid',highlightthickness=4)
transbtn.config(borderwidth=4,bg='white',fg='black')
transbtn.grid(column=0, row=4,pady=4)
frame = Frame(r, bg='SpringGreen2')
out = Text(frame, state='disabled', font=('Helvetica',16), width=40,height=7, bg='white')
Label(frame, text=' Translated Result ', font='Times 14 underline').grid(row=5, column=0, pady=4)
out.grid(column=0,row=6, pady=5)

def copyc(x):
	copy(x)

copytrans = Button(frame, text='Copy Translated', command=lambda:copyc(out.get(1.0,END)))
copytrans.config(width=19, height=1, font=('Helvetica', 10))
copytrans.config(bg='yellow', fg='black', borderwidth=2, highlightthickness=2)
copytrans.config(relief='solid')
copytrans.grid(column=0,row=7, pady=6)

frame.grid(row=5,column=0, pady=30)

r.mainloop()

