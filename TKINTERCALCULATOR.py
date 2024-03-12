from tkinter import *

root=Tk()
root.title('Calculator')

valueentry=Entry(root,width=40,borderwidth=5)
valueentry.grid(row=0,column=1,columnspan=3,padx=10,pady=10)

def button_click(number):
    v=valueentry.get()
    valueentry.delete(0,END)
    valueentry.insert(0,str(v)+str(number))

def button_add():
    first_number=valueentry.get()
    global f_num
    global math
    math='addition'
    f_num=float(first_number)
    valueentry.delete(0,END)

def button_subtract():
    first_number=valueentry.get()
    global f_num
    global math
    math='subtraction'
    f_num=float(first_number)
    valueentry.delete(0,END)

def button_multiply():
    first_number=valueentry.get()
    global f_num
    global math
    math='multiplication'
    f_num=float(first_number)
    valueentry.delete(0,END)

def button_divide():
    first_number=valueentry.get()
    global f_num
    global math
    math='division'
    f_num=float(first_number)
    valueentry.delete(0,END)

def button_clear():
    valueentry.delete(0,END)
    f_num==None

def button_equal():
    second_number=valueentry.get()
    second_number=int(second_number)
    valueentry.delete(0,END)
    if math=='addition':
        valueentry.insert(0,((f_num)+(second_number)))
    elif math=='subtraction':
        valueentry.insert(0,((f_num)-(second_number)))
    elif math=='division':
        valueentry.insert(0,((f_num)/(second_number)))
    elif math=='multiplication':
        valueentry.insert(0,((f_num)*(second_number)))
        

#BUTTONS

button_1=Button(root,text='1',padx=40,pady=20,bg='grey',borderwidth=2,command=lambda:button_click(1))
button_2=Button(root,text='2',padx=40,pady=20,bg='grey',borderwidth=2,command=lambda:button_click(2))
button_3=Button(root,text='3',padx=40,pady=20,bg='grey',borderwidth=2,command=lambda:button_click(3))
button_4=Button(root,text='4',padx=40,pady=20,bg='grey',borderwidth=2,command=lambda:button_click(4))
button_5=Button(root,text='5',padx=40,pady=20,bg='grey',borderwidth=2,command=lambda:button_click(5))
button_6=Button(root,text='6',padx=40,pady=20,bg='grey',borderwidth=2,command=lambda:button_click(6))
button_7=Button(root,text='7',padx=40,pady=20,bg='grey',borderwidth=2,command=lambda:button_click(7))
button_8=Button(root,text='8',padx=40,pady=20,bg='grey',borderwidth=2,command=lambda:button_click(8))
button_9=Button(root,text='9',padx=40,pady=20,bg='grey',borderwidth=2,command=lambda:button_click(9))
button_0=Button(root,text='0',padx=40,pady=20,bg='grey',borderwidth=2,command=lambda:button_click(0))

#FUNCTIONBUTTONS

button_clear=Button(root,text='CLEAR',bg='red',fg='white',padx=25,pady=53,borderwidth=3,command=button_clear)
button_equal=Button(root,text='=',padx=86,pady=20,bg='blue',fg='white',borderwidth=3,command=button_equal)
button_subtract=Button(root,text='-',padx=40,pady=20,bg='lightpink',fg='red',borderwidth=3,command=button_subtract)
button_add=Button(root,text='+',padx=39,pady=20,bg='lightblue',fg='black',borderwidth=3,command=button_add)
button_multiply=Button(root,text='x',padx=40,pady=20,bg='lightgreen',fg='blue',borderwidth=3,command=button_multiply)
button_divide=Button(root,text='/',padx=40,pady=20,bg='orange',fg='blue',borderwidth=3,command=button_divide)

#BUTTON LAYOUT

button_1.grid(row=3,column=1,columnspan=1)
button_2.grid(row=3,column=2,columnspan=1)
button_3.grid(row=3,column=3,columnspan=1)
button_4.grid(row=2,column=1,columnspan=1)
button_5.grid(row=2,column=2,columnspan=1)
button_6.grid(row=2,column=3,columnspan=1)
button_7.grid(row=1,column=1,columnspan=1)
button_8.grid(row=1,column=2,columnspan=1)
button_9.grid(row=1,column=3,columnspan=1)
button_0.grid(row=4,column=2,columnspan=1)

#FUNCTIONBUTTONLAYOUT

button_clear.grid(row=5,column=1,columnspan=1,rowspan=2)
button_subtract.grid(row=4,column=3,columnspan=1)
button_add.grid(row=4,column=1,columnspan=1)
button_equal.grid(row=6,column=2,columnspan=2)
button_multiply.grid(row=5,column=2)
button_divide.grid(row=5,column=3)

exit=Button(root,text='EXIT',command=root.quit)
exit.grid(row=7,column=2)

root=mainloop()

