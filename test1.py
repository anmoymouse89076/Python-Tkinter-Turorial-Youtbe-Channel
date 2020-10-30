#Python Tkinter Tutorial Setting Up Window And Buttons For Begginers
#source code link in description
#python 3.8
#Now We Are Going To Add Some Color
# Ctrl + s to save

from tkinter import *
window=Tk()
btn=Button(window, text="This is Button widget", fg='blue')
btn.place(x=80, y=100)
lbl=Label(window, text="This is Label widget", fg='red', font=("Helvetica", 16))
lbl.place(x=60, y=50)
txtfld=Entry(window, text="This is Entry Widget", bd=5)
txtfld.place(x=80, y=150)
window.title('Hello Python')
window.geometry("300x200+10+10")
window.mainloop()

#sorry guys it looks like the hashtags were not letting my code run
#i dont know why
#because hashtags arent ment to do anything any way
#but here is the final ressult