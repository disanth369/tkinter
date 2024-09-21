from tkinter import *
root=Tk()
root.title("my app")
root.geometry("300x300")
root.config(background='blue')

l1=Label(root,text="welocome",bg="red",fg="green",padx=5)
l1.pack()
l2=Label(root,text="enter your name",bg="white",fg="orange",padx=5)
l2.pack()
e1=Entry(root)
e1.pack()
def msg():
    name=e1.get()
    m1="welcome"+name
    l3=Label(root,text=m1)
    l3.pack()
b1=Button(root,text='submit',command=msg)
b1.pack()
root.mainloop()       