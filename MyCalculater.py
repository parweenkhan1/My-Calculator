from tkinter import *
from tkinter import messagebox
import math
screen = Tk()
screen.title("Calculator")
screen.iconbitmap('Guillendesign-Variations-1-Calculator-2.ico')
screen.configure(bg="light blue")
screen.maxsize(width=453,height=500)
screen.minsize(width=360,height=500)

def click(number):
    global operator
    operator+=str(number)
    tex.set(operator)

def clear():
    global operator
    operator = ''
    tex.set(operator)
def equal():
    global operator
    try:
        result = eval(operator)
        operator = str(result)
        tex.set(result)
    except:
        messagebox.showinfo("Notification","Try again ,Somthing is wrong.")
######################################Binding Function
def on_enter7(e):
    btn7.configure(bg="red")
def on_leave7(e):
    btn7.configure(bg="white")

def on_enter8(e):
    btn8.configure(bg="red")
def on_leave8(e):
    btn8.configure(bg="white")

def on_enter9(e):
    btn9.configure(bg="red")
def on_leave9(e):
    btn9.configure(bg="white")

def on_enterPlus(e):
    btnPlus.configure(bg="red")
def on_leavePlus(e):
    btnPlus.configure(bg="white")

def on_enter4(e):
    btn4.configure(bg="red")
def on_leave4(e):
    btn4.configure(bg="white")

def on_enter5(e):
    btn5.configure(bg="red")
def on_leave5(e):
    btn5.configure(bg="white")

def on_enter6(e):
    btn6.configure(bg="red")
def on_leave6(e):
    btn6.configure(bg="white")

def on_enterMultiply(e):
    btnMultiply.configure(bg="red")
def on_leaveMultiply(e):
    btnMultiply.configure(bg="white")

def on_enter1(e):
    btn1.configure(bg="red")
def on_leave1(e):
    btn1.configure(bg="white")

def on_enter2(e):
    btn2.configure(bg="red")
def on_leave2(e):
    btn2.configure(bg="white")

def on_enter3(e):
    btn3.configure(bg="red")
def on_leave3(e):
    btn3.configure(bg="white")

def on_enterMinus(e):
    btnMinus.configure(bg="red")
def on_leaveMinus(e):
    btnMinus.configure(bg="white")

def on_enter0(e):
    btn0.configure(bg="red")
def on_leave0(e):
    btn0.configure(bg="white")

def on_enterClear(e):
    btnClear.configure(bg="red")
def on_leaveClear(e):
    btnClear.configure(bg="white")

def on_enterEqual(e):
    btnEqual.configure(bg="red")
def on_leaveEqual(e):
    btnEqual.configure(bg="white")

def on_enterDivision(e):
    btnDivision.configure(bg="red")
def on_leaveDivision(e):
    btnDivision.configure(bg="white")

def on_enterEqual(e):
    btnEqual.configure(bg="red")
def on_leaveEqual(e):
    btnEqual.configure(bg="white")

def on_entersin(e):
    btnsin.configure(bg="red")
def on_leavesin(e):
    btnsin.configure(bg="white")

def on_entercos(e):
    btncos.configure(bg="red")
def on_leavecos(e):
    btncos.configure(bg="white")

def on_entertan(e):
    btntan.configure(bg="red")
def on_leavetan(e):
    btntan.configure(bg="white")

def on_enterlog(e):
    btnlog.configure(bg="red")
def on_leavelog(e):
    btnlog.configure(bg="white")

def on_entersqrt(e):
    btnsqrt.configure(bg="red")
def on_leavesqrt(e):
    btnsqrt.configure(bg="white")
####################Binding function Scintific calculation
def cmsin():
    global operator
    try:
        result = math.sin(eval(tex.get()))
        operator = str(result)
        tex.set(operator)
    except:
        messagebox.showinfo("Notification", "Try again ,Somthing is wrong.")

def cmcos():
    global operator
    try:
        result = math.cos(eval(tex.get()))
        operator = str(result)
        tex.set(operator)
    except:
        messagebox.showinfo("Notification", "Try again ,Somthing is wrong.")


def cmtan():
    global operator
    try:
        result = math.tan(eval(tex.get()))
        operator = str(result)
        tex.set(operator)
    except:
        messagebox.showinfo("Notification", "Try again ,Somthing is wrong.")


def cmlog():
    global operator
    try:
        result = math.log(eval(tex.get()))
        operator = str(result)
        tex.set(operator)
    except:
        messagebox.showinfo("Notification", "Try again ,Somthing is wrong.")


def cmsqrt():
    global operator
    try:
        result = math.sqrt(eval(tex.get()))
        operator = str(result)
        tex.set(operator)
    except:
        messagebox.showinfo("Notification", "Try again ,Somthing is wrong.")


tex = StringVar()
operator = ""
entry1 = Entry(screen,bg="gray",font=("arial",20,"italic bold"),bd="25",justify="right",textvariable=tex)
entry1.grid(row=0,columnspan=4)

btn7 = Button(screen,text="7",font=("arial",20,"italic bold"),bd="8",padx="16",pady="16",command=lambda:click(7)
              ,activebackground="gray",activeforeground="white")
btn7.grid(row=1,column=0)

btn8 = Button(screen,text="8",font=("arial",20,"italic bold"),bd='8',padx="16",pady="16",command=lambda:click(8)
              ,activebackground="gray",activeforeground="white")
btn8.grid(row=1,column=1)

btn9 = Button(screen,text="9",font=("arial",20,"italic bold"),bd="8",padx="16",pady="16",command=lambda:click(9)
              ,activebackground="gray",activeforeground="white")
btn9.grid(row=1,column=2)

btnPlus = Button(screen,text="+",font=("arial",20,"italic bold"),bd="8",padx="16",pady="16",command=lambda:click('+')
                 ,activebackground="gray",activeforeground="white")
btnPlus.grid(row=1,column=3)

btn4 = Button(screen,text="4",font=("arial",20,"italic bold"),bd="8",padx="16",pady="16",command=lambda:click(4)
              ,activebackground="gray",activeforeground="white")
btn4.grid(row=2,column=0)

btn5 = Button(screen,text="5",font=("arial",20,"italic bold"),bd="8",padx="16",pady="16",command=lambda:click(5)
              ,activebackground="gray",activeforeground="white")
btn5.grid(row=2,column=1)

btn6 = Button(screen,text="6",font=("arial",20,"italic bold"),bd="8",padx="16",pady="16",command=lambda:click(6)
              ,activebackground="gray",activeforeground="white")
btn6.grid(row=2,column=2)

btnMultiply = Button(screen,text="*",font=("arial",20,"italic bold"),bd="8",padx="18",pady="16",command=lambda:click('*')
                     ,activebackground="gray",activeforeground="white")
btnMultiply.grid(row=2,column=3)

btn1 = Button(screen,text="1",font=("arial",20,"italic bold"),bd="8",padx="16",pady="16",command=lambda:click(1)
              ,activebackground="gray",activeforeground="white")
btn1.grid(row=3,column=0)

btn2 = Button(screen,text="2",font=("arial",20,"italic bold"),bd="8",padx="16",pady="16",command=lambda:click(2)
              ,activebackground="gray",activeforeground="white")
btn2.grid(row=3,column=1)

btn3 = Button(screen,text="3",font=("arial",20,"italic bold"),bd="8",padx="16",pady="16",command=lambda:click(3)
              ,activebackground="gray",activeforeground="white")
btn3.grid(row=3,column=2)

btnMinus = Button(screen,text="-",font=("arial",20,"italic bold"),bd="8",padx="18",pady="16",command=lambda:click('-')
                  ,activebackground="gray",activeforeground="white")
btnMinus.grid(row=3,column=3)

btn0 = Button(screen,text="0",font=("arial",20,"italic bold"),bd="8",padx="16",pady="16",command=lambda:click(0)
              ,activebackground="gray",activeforeground="white")
btn0.grid(row=4,column=0)

btnClear = Button(screen,text="C",font=("arial",20,"italic bold"),bd="8",padx="16",pady="16",command=clear
                  ,activebackground="gray",activeforeground="white")
btnClear.grid(row=4,column=1)

btnEqual = Button(screen,text="=",font=("arial",20,"italic bold"),bd="8",padx="16",pady="16",command=equal
                  ,activebackground="gray",activeforeground="white")
btnEqual.grid(row=4,column=2)

btnDivision = Button(screen,text="/",font=("arial",20,"italic bold"),bd="8",padx="18",pady="16",command=lambda:click("/")
                     ,activebackground="gray",activeforeground="white")
btnDivision.grid(row=4,column=3)
###############################################Scintific Calculetor
btnsin = Button(screen,text="sin",font=("arial",20,"italic bold"),bd="8",padx="14",pady="19",command=cmsin,
              activebackground="gray",activeforeground="white")
btnsin.grid(row=0,column=4)

btncos = Button(screen,text="cos",font=("arial",20,"italic bold"),bd="8",padx="14",pady="19",command=cmcos
              ,activebackground="gray",activeforeground="white")
btncos.grid(row=1,column=4)

btntan = Button(screen,text="tan",font=("arial",20,"italic bold"),bd="8",padx="16",pady="19",command=cmtan
              ,activebackground="gray",activeforeground="white")
btntan.grid(row=2,column=4)

btnlog = Button(screen,text="log",font=("arial",20,"italic bold"),bd="8",padx="17",pady="19",command=cmlog
              ,activebackground="gray",activeforeground="white")
btnlog.grid(row=3,column=4)

btnsqrt = Button(screen,text="sqrt",font=("arial",20,"italic bold"),bd="8",padx="12",pady="19",command=cmsqrt
              ,activebackground="gray",activeforeground="white")
btnsqrt.grid(row=4,column=4)
################################Binding
btnsin.bind("<Enter>",on_entersin)
btnsin.bind("<Leave>",on_leavesin)

btncos.bind("<Enter>",on_entercos)
btncos.bind("<Leave>",on_leavecos)

btntan.bind("<Enter>",on_entertan)
btntan.bind("<Leave>",on_leavetan)

btnlog.bind("<Enter>",on_enterlog)
btnlog.bind("<Leave>",on_leavelog)

btnsqrt.bind("<Enter>",on_entersqrt)
btnsqrt.bind("<Leave>",on_leavesqrt)






######################################Binding
btn7.bind("<Enter>",on_enter7)
btn7.bind("<Leave>",on_leave7)

btn8.bind("<Enter>",on_enter8)
btn8.bind("<Leave>",on_leave8)

btn9.bind("<Enter>",on_enter9)
btn9.bind("<Leave>",on_leave9)

btnPlus.bind("<Enter>",on_enterPlus)
btnPlus.bind("<Leave>",on_leavePlus)

btn4.bind("<Enter>",on_enter4)
btn4.bind("<Leave>",on_leave4)

btn5.bind("<Enter>",on_enter5)
btn5.bind("<Leave>",on_leave5)

btn6.bind("<Enter>",on_enter6)
btn6.bind("<Leave>",on_leave6)

btnMultiply.bind("<Enter>",on_enterMultiply)
btnMultiply.bind("<Leave>",on_leaveMultiply)

btn1.bind("<Enter>",on_enter1)
btn1.bind("<Leave>",on_leave1)

btn2.bind("<Enter>",on_enter2)
btn2.bind("<Leave>",on_leave2)

btn3.bind("<Enter>",on_enter3)
btn3.bind("<Leave>",on_leave3)

btnMinus.bind("<Enter>",on_enterMinus)
btnMinus.bind("<Leave>",on_leaveMinus)

btn0.bind("<Enter>",on_enter0)
btn0.bind("<Leave>",on_leave0)

btnClear.bind("<Enter>",on_enterClear)
btnClear.bind("<Leave>",on_leaveClear)

btnEqual.bind("<Enter>",on_enterEqual)
btnEqual.bind("<Leave>",on_leaveEqual)

btnDivision.bind("<Enter>",on_enterDivision)
btnDivision.bind("<Leave>",on_leaveDivision)

screen.mainloop()