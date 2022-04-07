from tkinter import *
window = Tk()

window.geometry("400x230+10+20")
window.title("Label")

label = Label(window, text="Laboratory Activity 5")
label.place(x=130, y=100)
label = Label(window, text="Submitted to: Mam Sayo")
label.place(x=120, y=120)

window.mainloop()