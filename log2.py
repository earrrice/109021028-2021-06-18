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

def inp():
    indata=entryin.get()
    if len(indata)>0:
        if indata=="03ac674216f3e15c761ee1a5e255f067953623c8b388b4459e13f978d7c846f4":
            labut['text']="1234 sha256"
        elif indata=="6b3a55e0261b0304143f805a24924d0c1c44524821305f31d9277843b8a10f4e":
            labut['text']="password sha256"
        elif indata=="bef57ec7f53a6d40beb640a780a639c83bc29ac8a9816f1fc6c5c6dcd93c4721":
            labut['text']="abcdef sha256"
        elif indata=="65e84be33532fb784c48129675f9eff3a682b27168c0ea744b2cf58ee02337c5":
            labut['text']="qwerty sha256"
        elif indata=="81dc9bdb52d04dc20036dbd8313ed055":
            labut['text']="1234 md5"
        elif indata=="5f4dcc3b5aa765d61d8327deb882cf99":
            labut['text']="password md5"
        elif indata=="34e0c34fbafd8e282b81f8846a28065d":
            labut['text']="abcdefy md5"
        elif indata=="d8578edf8458ce06fbc5bb76a58c5ca4":
            labut['text']="qwerty md5"
        elif indata=="7110eda4d09e062aa5e4a390b0a572ac0d2c0220":
            labut['text']="1234 sha1"
        elif indata=="5baa61e4c9b93f3f0682250b6cf8331b7ee68fd8":
            labut['text']="password sha1"
        elif indata=="d105f6d706f78375a4ebeeee7d77407e996ec235":
            labut['text']="abcdefy sha1"
        elif indata=="b1b3773a05c0ed0176787a4f1574ff0075f7521e":
            labut['text']="qwerty sha1"
        else:
            labut['text']="找不到"
    else:
        labut['text']="請輸入密碼"

root=Tk()
root.geometry("400x300+200+100")
top=Toplevel(root)
labin=Label(root,text="輸入密碼",anchor=E,justify=RIGHT,font=("Times",20))
entryin=Entry(root)
btin=Button(root,text="確定",command=inp)
labut=Label(root,text="",anchor=E,justify=RIGHT,font=("Times",20))
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
labin.grid(row=0,column=0,sticky=NSEW)
entryin.grid(row=0,column=1,sticky=NSEW)
btin.grid(row=2,column=0,sticky=NSEW)
labut.grid(row=3,column=0,sticky=NSEW)

root.withdraw()
root.mainloop()