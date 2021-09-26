import random
import string
from tkinter import *
 
root = Tk()
root.title("PASSWORD GENERATOR")
root.geometry('1370x720+0+0')
root.maxsize(width=1370, height=720)
root.minsize(width=1370, height=720)
root.configure(background="dark gray")



Tops = Frame(root, width=1350, height=50, bd=8, bg="dark blue")
Tops.pack(side=TOP)
 
 #buttons and input
f1 = Frame(root, width=500, height=900, bd=8, bg="gray")
f1.pack(side=LEFT)

#textbox
f2 = Frame(root, width=300, height=500, bd=8, bg="white")
f2.pack(side=TOP)

#outer frame of account name
fla = Frame(f1, width=500, height=200, bd=2, bg="cyan")
fla.pack(side =TOP)

#block of buttons
flb = Frame(f1, width=500, height=600, bd=2, bg="gold2")
flb.pack(side =TOP)

account = StringVar()
password = StringVar()

#title
lbl_information = Label(Tops, font=('arial', 45, 'bold'), text="PASSWORD GENERATOR", relief=GROOVE, bd=10, bg="cyan", fg="Black")
lbl_information.grid(row=0, column=0)



labelaccount = Label(fla, text="ACCOUNT FOR WHICH PASSWORD TO GEN", font=('arial', 16, 'bold'), bd=5, fg="black", bg="white").grid(row=0, column=0)
 
txtaccount = Entry(fla, textvariable=account, font=('arial', 16, 'bold'), bd=5, width=22,justify='left')
txtaccount.grid(row=0, column=1)


def Exit():
    root.destroy()
    return
 
def InfoEntry():
    total = string.ascii_letters + string.digits + string.punctuation
    password = "".join(random.sample(total,16))
    txt.insert(END,"\nACCOUNT\t" + account.get()+"\n")
    txt.insert(END,"PASSWORD\t" + password)
    with open('file.txt', 'a') as myfile:
        myfile.write(account.get())
        myfile.write("\t")
        myfile.write(password)
        myfile.write("\n")
    myfile.close()

def Reset():
    account.set("")

txt = Text(f2, height=22, width=34, bd=16, font=('arial', 13, 'bold'), fg="black", bg="white")
txt.grid(row=1, column=0)


ButtonView = Button(flb, text='GENERATE PASSWORD', padx=16, pady=16, bd=15, font=('arial', 16, 'bold'), relief="groove", width=20,
command=InfoEntry, fg="black", bg="dark gray").grid(row=0, column=2)

ButtonReset = Button(flb, text='RESET', padx=16, pady=16, bd=15, font=('arial', 16, 'bold'), relief="groove", width=10, command=Reset,
fg="black", bg="dark gray").grid(row=0, column=1)

ButtonExit = Button(flb, text='EXIT SYSTEM', padx=16, pady=16, bd=15, font=('arial', 16, 'bold'), relief="groove", width=14, command=Exit,
fg="black", bg="dark gray").grid(row=0, column=3)

root.mainloop()
