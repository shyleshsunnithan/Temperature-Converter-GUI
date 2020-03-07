from tkinter import *
from tkinter.messagebox import showinfo

win = Tk()
win.title("Temperature Converter")

def celsius_to_farhenheit():
    value = int(entry.get())
    answer = (value * 9/5)+32
    showinfo("Answer",f"{value} C = {answer} F") 

def farhenheit_to_celsius():
    value = int(entry.get())
    answer = (value - 32)*5/9
    showinfo("Answer",f"{value} F = {answer} C") 

label = Label(win,text="Enter Temperature Here:",font=('arial',15,'bold'))
label.grid(row=0,column=0)

entry = Entry(win,font=('arial',20,'bold'))
entry.grid(row=1,column=0)

button1 = Button(win,text="Celsius to Fahrenheit",font=('arial',10,'bold'),command=celsius_to_farhenheit)
button1.grid(row=3,column=0)

button2 = Button(win,text="Convert Fahrenheit to Celsius",font=('arial',10,'bold'),command=farhenheit_to_celsius)
button2.grid(row=4,column=0)


win.mainloop()
