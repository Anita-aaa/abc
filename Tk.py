# from tkinter import *
# win= Tk()
# win.mainloop()

# from tkinter import *
# win=Tk()
# win.title("System")
# win.mainloop()

# from tkinter import *
# win=Tk()
# win.geometry("200x300")
# win.mainloop()

# from tkinter import *
# win=Tk()
# win.maxsize(width=300,height=200)
# win.minsize(width=300,height=200)
# win.mainloop()


# from tkinter import *
# win=Tk()
# win.iconbitmap("a.ico")
# win.mainloop()

# from tkinter import *
# root=Tk()
# redbutton= Button(root,text="LEFT",fg="green") #remaining
# redbutton.pack(side=LEFT)
# greenbutton=Button(root,text="RIGHT", fg="black")
# greenbutton.pack(side=RIGHT)
# bluebutton=Button(root,text="TOP",fg="Blue")
# bluebutton.pack(side=TOP)
# root.mainloop()

#row column
# from tkinter import*
# root=Tk()
# name=Label(root,text="Name").grid(row=0,column=0)
# e1=Entry(root).grid(row=0,column=1)
# password= Label(root,text="password").grid(row=1,column=0)
# e2=Entry(root).grid(row=1,column=1)
# email=Label(root,text="email").grid(row=2,column=0)
# e3=Entry(root).grid(row=2,column=1)
# root.mainloop()



# homework
#loginform

# from tkinter import*
# root=Tk()
# root.title("Login form")
# name=Label(root,text="Name").grid(row=0,column=0)
# e1=Entry(root).grid(row=0,column=1)
# email= Label(root,text="email").grid(row=1,column=0)
# e2=Entry(root).grid(row=1,column=1)
# password=Label(root,text="password").grid(row=2,column=0)
# e3=Entry(root).grid(row=2,column=1)
# root.mainloop()

# registration form
# from tkinter import*
# root=Tk()
# root.title("Registration")
# firstname=Label(root,text="firstname").grid(row=0,column=0)
# e1=Entry(root).grid(row=0,column=1)
# lastname=Label(root,text="lastname").grid(row=1,column=0)
# e2=Entry(root).grid(row=1,column=1)
# email= Label(root,text="email").grid(row=2,column=0)
# e2=Entry(root).grid(row=2,column=1)
# password=Label(root,text="password").grid(row=3,column=0)
# e3=Entry(root).grid(row=3,column=1)
# login=Button(root,text="login",fg="blue").grid(row=4,column=1)  
# forgetpassword=Button(root,text="forget password",fg="blue").grid(row=5,column=1)
# root.mainloop()

# from tkinter import*
# root=Tk()
# root.geometry("400x250")
# name=Label(root,text="Name").place(x=10,y=30)
# password=Label(root,text="address").place(x=10,y=90)
# contact=Label(root,text="Contact").place(x=10,y=130)
# e1=Entry(root).place(x=50,y=30)
# e2=Entry(root).place(x=60,y=90)
# e3=Entry(root).place(x=60,y=130)
# root.mainloop()
# from tkinter import*
# lol=Tk()
# lol.title("GUI")
# name=Label(lol,text="tkinter",font=("itt",80))
# name.pack()
# lol.mainloop()

# from tkinter import*
# window=Tk()
# def func():
#     print("Button is clicked")
# btn=Button(window,text="login",command=func)
# btn.pack(side="top")
# window.mainloop()

'''
from tkinter import*
window=Tk()
def func():
    if btn=Button(window,text=login )

'''


# from tkinter import *
# window=Tk()
# def myclick():
#     myLabel=Label(window,text="Look! i clicked the button",fg="red",bg="purple",font=40)
#     myLabel.pack()
# my_button=Button(window,text="click me",padx=10,pady=10,command=myclick,fg="red",bg="blue")
# my_button.pack()
# window.mainloop()

'''
from tkinter import*
window=Tk()
e=Entry(window,bg="blue",fg="white")
e.pack()
def myclick():
    myLabel=Label(window,text="hello"+e.get())
    myLabel.pack()#e.delete(0:END)
btn=Button(window,text="click me")
btn.pack()
window.mainloop()
'''


# from tkinter import*
# root=Tk()
# root.title("GUI")
# root.maxsize(width=600,height=300)
# root.minsize(width=600,height=300)
# def add():
#     x=var.get()
#     print(x)
#     mylabell.config(text=x,bg="green")
# #label1
# mylabel=Label(root,text="User Name",fg="red",bg="yellow")
# mylabel.place(x=10,y=10)
# mylabell=Label(root,text="Nothing",fg="red",bg="yellow")
# mylabell.place(x=40,y=120)
# var=StringVar()
# ent=Entry(root,bg="black",fg="white",textvariable=var)
# ent.place(x=80,y=10)
# btn=Button(root,text="Submit",bg="green",fg="white",command=add)
# btn.place(x=20,y=80)
# root.mainloop()

'''
from tkinter import*
root=Tk()
def click()
'''
# from tkinter import *
# window= Tk()
# window.geometry('300x300')
# def func():
#  print("hello python")

# btn = Button(window, text="Login", command=func)
# btn.pack(side="top")
# def add():
#  print("hello softwarica")

# btn = Button(window, text="Registration", command=add)
# btn.pack(side="left")
# window.mainloop()

'''
from tkinter import *
from tkinter import messagebox
root=Tk()
'''
#Creates new window (Pil install garera image download garnuparxa)
'''
from tkinter import *
from PIL import Image, ImageTk
root=Tk()
def open():
    global my_img
    top=Toplevel()
    my_img=ImageTk.PhotoImage(Image.open("eaglee.png"))
    my_label=Label(top,image=my_img)
    my_label.pack(pady=10)
    btn=Button(top,text="close window",command=top.destroy)
    btn.pack()
btnn=Button(root,text="open",command=open)
btnn.pack()
root.mainloop()
'''
# from tkinter import*
# root=Tk()
# root.geometry("200x200")
# def show():
#     label.config(text=clicked.get())
# #dropdown menu options
# options=[
#     "Monday"
#     "Tuesday"
#     "Wednesday"
#     "Thursday"
#     "Friday"
#     "Saturday"
#     "Sunday"

# ]
# clicked=StringVar()
# clicked.set("Monday")
# drop=OptionMenu(root, clicked, *options)
# drop.pack()
# button=Button(root,text="click Me", command=show).pack()
# label=Label(root,text=" ")
# label.pack()
# root.mainloop()






#+++++++++++++

# from _ast import Lambda
# from tkinter import*
# root=Tk()
# root.title("Simple Calculator")
# e=Entry(root,width=35,borderwidth=5)
# e.grid(row=0,column=0,columnspan=3,padx=10,pady=10)

# def button_click(number):
#     current=e.get()
#     e.delete(0, END)
#     e.insert(0,str(current)+ str(number))
# def button_clear():
#     e.delete=(0,END)
# def button_add():
#     first_number=e.get()
#     global f_num 
#     f_num=int(first_number) 
#     e.delete(0,END)
# def button_equal():
#     second_number=e.get()
#     e.delete(0 , END)
#     e.insert(0,f_num+int(second_number))
# button_1=Button(root,text="1",padx=40,pady=20,command=lambda : button_click(1))
# button_2=Button(root,text="2",padx=40,pady=20,command=lambda : button_click(2))
# button_3=Button(root,text="3",padx=40,pady=20,command=lambda : button_click(3))
# button_4=Button(root,text="4",padx=40,pady=20,command=lambda : button_click(4))
# button_5=Button(root,text="5",padx=40,pady=20,command=lambda : button_click(5))
# button_6=Button(root,text="6",padx=40,pady=20,command=lambda : button_click(6))
# button_7=Button(root,text="7",padx=40,pady=20,command=lambda : button_click(7))
# button_8=Button(root,text="8",padx=40,pady=20,command=lambda : button_click(8))
# button_9=Button(root,text="9",padx=40,pady=20,command=lambda : button_click(9))
# button_0=Button(root,text="0",padx=40,pady=20,command=lambda : button_click(0))
# button_add=Button(root,text="+",padx=39,pady=20,command=button_add)
# button_equal=Button(root,text="=",padx=91,pady=20,command=button_equal)
# button_clear=Button(root,text="clear",padx=79,pady=20,command=button_clear)
# button_1.grid(row=3,column=0)
# button_2.grid(row=3,column=1)
# button_3.grid(row=3,column=2)

# button_4.grid(row=2,column=0)
# button_5.grid(row=2,column=1)
# button_6.grid(row=2,column=2)

# button_7.grid(row=1,column=0)
# button_8.grid(row=1,column=1)
# button_9.grid(row=1,column=2)

# button_0.grid(row=4,column=0)
# button_clear.grid(row=4,column=1,columnspan=2)
# button_add.grid(row=5,column=0)
# button_equal.grid(row=5,column=1,columnspan=2)
# root.mainloop()







# #######
# # Calculator
# import tkinter
# from tkinter import *
# root=Tk()
# root.title("Simple Calculator")
# root.geometry("400x400")
# root.resizable(False,False)

# equation=""

# def show(value):
#     global equation
#     equation+=value
#     label_result.config(text=equation)

# def clear():
#     global equation
#     equation=""
#     label_result.config(text=equation)

# def calculate():
#     global equation
#     result=""
#     if equation !="":
#         try:
#             result=eval(equation)
#         except:
#             result="error"
#             equation=""
#     label_result.config(text=result)

# root.configure(bg="black")
# label_result=Label(root,width=25,height=2,text="",font=30)
# label_result.pack()
# e=Button(root,text="C",width=5,height=1,font=30,bd=1,command=lambda:clear())
# e.place(x=10,y=70)
# e=Button(root,text="/",width=5,height=1,font=30,bd=1,command=lambda:show("/"))
# e.place(x=100,y=70)
# Button(root,text="%",width=5,height=1,font=30,bd=1,command=lambda:show("%")).place(x=200,y=70)
# Button(root,text="*",width=5,height=1,font=30,bd=1,command=lambda:show("*")).place(x=300,y=70)

# Button(root,text="7",width=5,height=1,font=30,bd=1,bg="pink",command=lambda:show("7")).place(x=10,y=140)
# Button(root,text="8",width=5,height=1,font=30,bd=1,bg="pink",command=lambda:show("8")).place(x=100,y=140)
# Button(root,text="9",width=5,height=1,font=30,bd=1,bg="pink",command=lambda:show("9")).place(x=200,y=140)
# Button(root,text="-",width=5,height=1,font=30,bd=1,bg="pink",command=lambda:show("-")).place(x=300,y=140)


# Button(root,text="4",width=5,height=1,font=30,bd=1,bg="pink",command=lambda:show("4")).place(x=10,y=210)
# Button(root,text="5",width=5,height=1,font=30,bd=1,bg="pink",command=lambda:show("5")).place(x=100,y=210)
# Button(root,text="6",width=5,height=1,font=30,bd=1,bg="pink",command=lambda:show("6")).place(x=200,y=210)
# Button(root,text="+",width=5,height=1,font=30,bd=1,bg="pink",command=lambda:show("+")).place(x=300,y=210)

# Button(root,text="1",width=5,height=1,font=30,bd=1,bg="pink",command=lambda:show("1")).place(x=10,y=280)
# Button(root,text="2",width=5,height=1,font=30,bd=1,bg="pink",command=lambda:show("2")).place(x=100,y=280)
# Button(root,text="3",width=5,height=1,font=30,bd=1,bg="pink",command=lambda:show("3")).place(x=200,y=280)

# Button(root,text="0",width=12,height=3,font=30,bd=1,bg="pink",command=lambda:show("0")).place(x=10,y=350)
# Button(root,text=".",width=12,height=3,font=30,bd=1,bg="pink",command=lambda:show(".")).place(x=130,y=350)

# Button(root,text="=",width=8,height=4,font=30,bd=1,bg="orange",command=lambda:calculate()).place(x=300,y=300)

# root.mainloop()



