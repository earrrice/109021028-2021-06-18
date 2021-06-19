from tkinter import *
import hashlib

s256=hashlib.sha256()

def login():
    idData=entryID.get()
    pwData=entryPw.get()
    if len(idData)>0 and len(pwData)>0:
        s256.update(pwData.encode("utf-8"))
        pwh=s256.hexdigest()
        if idData=="csie"and pwh=="5515f0912ec4ca5c9537a9c29ed62372869e0f2332c58eb312bd7ca7de850456":
            root.deiconify()
            top.destroy()
        else:
            root.deiconify(0,"end")
            top.destroy(0,"end")
    else:
        root.deiconify(0,"end")
        top.destroy(0,"end")
def ep():
    top.destroy()
    root.destroy()

flag=True

def bttxt(n):
    global flag
    if n == 0 and bt0.cget("text")=="":#讓重複按沒有效果
        if flag:
            bt0.config(text="O")
        else:
            bt0.config(text="X")
        #bt0.config(state=DISABLED)#字出現後鎖住，但是顏色會變淡
    elif n == 1 and bt1.cget("text")=="":
        if flag:
            bt1.config(text="O")
        else:
            bt1.config(text="X")
    elif n == 2 and bt2.cget("text")=="":
        if flag:
            bt2.config(text="O")
        else:
            bt2.config(text="X")
    elif n == 3 and bt3.cget("text")=="":
        if flag:
            bt3.config(text="O")
        else:
            bt3.config(text="X")
    elif n == 4 and bt4.cget("text")=="":
        if flag:
            bt4.config(text="O")
        else:
            bt4.config(text="X")
    elif n == 5 and bt5.cget("text")=="":
        if flag:
            bt5.config(text="O")
        else:
            bt5.config(text="X")
    elif n == 6 and bt6.cget("text")=="":
        if flag:
            bt6.config(text="O")
        else:
            bt6.config(text="X")
    elif n == 7 and bt7.cget("text")=="":
        if flag:
            bt7.config(text="O")
        else:
            bt7.config(text="X")
    elif n == 8 and bt8.cget("text")=="":
        if flag:
            bt8.config(text="O")
        else:
            bt8.config(text="X")
    flag=not flag

    if bt0.cget("text")==bt1.cget("text") and bt0.cget("text")==bt2.cget("text"):
        if bt0.cget("text")=="O":
            print("O win")
        elif bt0.cget("text")=="X":
            print("X win")
    elif bt3.cget("text")==bt4.cget("text") and bt3.cget("text")==bt5.cget("text"):
        if bt3.cget("text")=="O":
            print("O win")
        elif bt3.cget("text")=="X":
            print("X win")
    elif bt6.cget("text")==bt7.cget("text") and bt6.cget("text")==bt8.cget("text"):
        if bt6.cget("text")=="O":
            print("O win")
        elif bt6.cget("text")=="X":
            print("X win")
    elif bt0.cget("text")==bt3.cget("text") and bt0.cget("text")==bt6.cget("text"):
        if bt0.cget("text")=="O":
            print("O win")
        elif bt0.cget("text")=="X":
            print("X win")
    elif bt1.cget("text")==bt4.cget("text") and bt1.cget("text")==bt7.cget("text"):
        if bt1.cget("text")=="O":
            print("O win")
        elif bt1.cget("text")=="X":
            print("X win")
    elif bt2.cget("text")==bt5.cget("text") and bt2.cget("text")==bt8.cget("text"):
        if bt2.cget("text")=="O":
            print("O win")
        elif bt2.cget("text")=="X":
            print("X win")
    elif bt0.cget("text")==bt4.cget("text") and bt0.cget("text")==bt8.cget("text"):
        if bt0.cget("text")=="O":
            print("O win")
        elif bt0.cget("text")=="X":
            print("X win")
    elif bt2.cget("text")==bt4.cget("text") and bt2.cget("text")==bt6.cget("text"):
        if bt2.cget("text")=="O":
            print("O win")
        elif bt2.cget("text")=="X":
            print("X win")



root=Tk()
root.geometry("400x300+200+100")
root.rowconfigure(0,weight=1)
root.rowconfigure(1,weight=1)
root.rowconfigure(2,weight=1)
root.columnconfigure(0,weight=1)
root.columnconfigure(1,weight=1)
root.columnconfigure(2,weight=1)

bt0=Button(root,text="",command=lambda:bttxt(0))
bt0.grid(row=0,column=0,sticky=NSEW)
bt1=Button(root,text="",command=lambda:bttxt(1))
bt1.grid(row=0,column=1,sticky=NSEW)
bt2=Button(root,text="",command=lambda:bttxt(2))
bt2.grid(row=0,column=2,sticky=NSEW)
bt3=Button(root,text="",command=lambda:bttxt(3))
bt3.grid(row=1,column=0,sticky=NSEW)
bt4=Button(root,text="",command=lambda:bttxt(4))
bt4.grid(row=1,column=1,sticky=NSEW)
bt5=Button(root,text="",command=lambda:bttxt(5))
bt5.grid(row=1,column=2,sticky=NSEW)
bt6=Button(root,text="",command=lambda:bttxt(6))
bt6.grid(row=2,column=0,sticky=NSEW)
bt7=Button(root,text="",command=lambda:bttxt(7))
bt7.grid(row=2,column=1,sticky=NSEW)
bt8=Button(root,text="",command=lambda:bttxt(8))
bt8.grid(row=2,column=2,sticky=NSEW)
top=Toplevel(root)
labid=Label(top,text="id",anchor=E,justify=RIGHT,font=("Times",20))
labpw=Label(top,text="密碼",anchor=E,justify=RIGHT,font=("Times",20))
entryID=Entry(top)
entryPw=Entry(top,show="*")
btlogin=Button(top,text="Login",command=login)
btexit=Button(top,text="Exit",command=ep)
labid.grid(row=0,column=0,sticky=NSEW)
entryID.grid(row=0,column=1,sticky=NSEW)
labpw.grid(row=1,column=0,sticky=NSEW)
entryPw.grid(row=1,column=1,sticky=NSEW)
btlogin.grid(row=2,column=0,sticky=NSEW)
btexit.grid(row=2,column=1,sticky=NSEW)

root.withdraw()
root.mainloop()