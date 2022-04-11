from tkinter import *
window=Tk()

def FullName():
    name['text'] = 'myname'

label = Label(text='Enter your FullName:', fg='red')
label.place(x=70, y=50)

button = Button(text='Click to display your FullName', fg='red', command=FullName)
button.place(x=50, y=100)

entername = Entry(textvariable='myname', bd='5')
entername.place(x=250, y=50)

name = Entry(text='This is my name', bd='5')
name.place(x=250, y=100)

window.title('Midterm in OOP')
window.geometry("500x200+10+10")
window.mainloop()