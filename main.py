from tkinter import *
root=Tk()
root.title("event handlind")
root.geometry("300x300")
root.config(background='blue')
def Key_pressed(event):
   print(event.char,'key is preesed')
def Mouse_click(event):
   print('mouse is clicked')

root.bind('<Key>',Key_pressed)
b1=Button(root,text='submit')
b1.pack()

b1.bind('<Button-1>',Mouse_click)

root.mainloop()       