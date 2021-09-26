from tkinter import *

root = Tk()
root.title("Conversions")
root.geometry('944x344')
root.configure(background="white")

Label(root, text=" Conversions", font="comicsansms 25 bold").grid(row=0, column=1)

option = StringVar()
number = StringVar()

label1 = Label(root, text="Choose an option: \n 1. Decimal to binary \n 2. Binary to decimal\n Option: ")
label1.grid(row=4, column=1)

option = Entry(root, textvariable=option, font=('arial', 10, 'bold'), bd=5, width=22, justify='left')
option.grid(row=3, column=2)

num = Entry(root, textvariable=number, font=('arial', 10, 'bold'), bd=5, width=22, justify='left')
num.grid(row=5, column=2)


def conversion():
    menu = int(option.get())
    user_num = num.get()
    try:
        if menu < 1 or menu > 2:
            raise ValueError
        if menu == 1:
            # dec = int(input("Input your decimal number:\nDecimal: "))
            txt.insert(END, "Binary: " + format(bin(int(user_num))[2:]))
        elif menu == 2:
            txt.insert(END, "Decimal: " + format(int(user_num, 2)))
            # txt.insert(END,"Decimal:"+format(int(user_num)))
    except ValueError:
        print ("please choose a valid option")

        # Buttons
        Button(text="Convert", command=conversion).grid(row=15, column=2)
        Button(text="Reset", command=Reset).grid(row=17, column=2)

txt = Text(root, height=5, width=35, bd=16, font=('arial', 13, 'bold'), fg="black", bg="white")
txt.grid(row=25, column=1)

root.mainloop()
