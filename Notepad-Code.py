from tkinter import *
from tkinter.messagebox import showinfo
from tkinter.filedialog import askopenfilename ,asksaveasfilename
import os
root=Tk()
root.title("*Untitled-Notepad")
#root.wm_iconbitmap("notepad photo.png")
root.geometry("300x300")
root.wm_iconbitmap()
#this is for our text area  x and y axis both
textarea=Text(root,font="arial",undo=True)
file=None
textarea.pack(fill=BOTH,expand=True)

def newfile():
    global file
    root.title("Untitled-Notepad")
    file=None
    textarea.delete("1.0",END)

def openfile():
    global file
    file=askopenfilename(defaultextension=".txt",filetypes=[("All file","*.*"),("Text Document","*.txt")])
    if file == "":
        file= None
    else:
        root.title(os.path.basename(file)+ "- Notepad")
        textarea.delete("1.0",END)
        f= open(file,'r')
        textarea.insert("1.0",f.read())
        f.close()
def savefile():
    global file
    if file == None:
        file = asksaveasfilename(initialfile="Untitled.txt",filetypes=[("All file","*.*"),("Text Document","*.txt")])
    if file == "":
        file =None
        # to save file
    else :
        f= open(file,"w")
        f.write(textarea.get(1.0,END))
        f.close()

    root.title(os.path.basename(file)+"-Notepad")

  #eventgenerate use to acces command autmatically
def cut():
    textarea.event_generate("<<cut>>")
def copy():
    textarea.event_generate("<<copy>>")

def paste():
    textarea.event_generate("<<paste>>")

def about():
    showinfo("notepad","Notepad by himanshu")


menubar=Menu(root)

filemenu=Menu(menubar,tearoff=0)
menubar.add_cascade(label="file",menu=filemenu)

filemenu.add_command(label='New',accelerator="ctrl N",command=newfile)
filemenu.add_command(label='Open',accelerator="ctrl O",command=openfile)
filemenu.add_command(label='Save',accelerator="ctrl S",command=savefile)
filemenu.add_command(label='save as',accelerator="ctrl shift S",command=savefile)
filemenu.add_command(label='Close',accelerator="ctrl f4",command=root.quit)
filemenu.add_separator()
filemenu.add_command(label='Exit',command=root.quit)

editmenu=Menu(menubar,tearoff=0)
menubar.add_cascade(label="Edit",menu=editmenu)

# editmenu.add_command(label='Undo',accelerator="ctrl Z",command=undo)
# editmenu.add_command(label='Redo',accelerator="ctrl y",command=redo)
# editmenu.add_separator()
editmenu.add_command(label='Cut',accelerator="ctrl x",command=cut)
editmenu.add_command(label='Copy',accelerator="ctrl C",command=copy)
editmenu.add_command(label='Paste',accelerator="ctrl v",command=paste)

helpmenu=Menu(menubar,tearoff=0)
menubar.add_cascade(label="Help",menu=helpmenu)

helpmenu.add_cascade(label="Help Index",command=about)
helpmenu.add_cascade(label="About....",command=about)

root.config(menu=menubar)

root.mainloop()