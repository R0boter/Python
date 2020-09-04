import tkinter
import random
from tkinter import messagebox

i = 0
def message():
    global i
    if i == 7:
        i = 0
    loveList = ['你是最漂亮的','我只对你一个人好','什么事都听你的','永远不会变心','给你买阿尔卑斯','奶茶无限供应','你吩咐的我立马去办']
    tkinter.messagebox.showinfo(message = loveList[i])
    i +=1

def out():
    tkinter.messagebox.showinfo(message = '嘿嘿！Mua ~')
    mainWindon.destroy()

mainWindon = tkinter.Tk()
mainWindon.title('来自小垃圾的信')
mainWindon.geometry('300x300+800+300')

photo = tkinter.PhotoImage(file = '1.gif')
tkinter.Label(mainWindon,image = photo).place(x = 0,y = 0,width = 300,height = 240)

tkinter.Button(mainWindon, text = '是的',command = out).place(x = 30, y = 250, width = 80)
tkinter.Button(mainWindon, text = '不是',command = message).place(x = 190, y = 250, width = 80)

mainWindon.mainloop()