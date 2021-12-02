from tkinter import *
from random import randint
root=Tk()
root.geometry("500x300")
root.title("Number Guessing game")

random_num=randint(1,10)

def guess():
    entry_val=int(num_entry.get())
    try:
        if entry_val>random_num:
            if entry_val-1==random_num:
                msg["text"]="Really close but still High"
            else:
                msg["text"]="Too High"
        elif entry_val<random_num:
            if entry_val+1==random_num:
                msg["text"]="Really close but still low"
            else:
                msg["text"]="Too Low"
        else:
            msg["text"]="Correct"
    except:
        msg["text"]="Please enter a number"
head=Label(root,text="Number Guessing Game",font=("Helvetica",15,"bold"))
head.pack()
lbl_intro=Label(root,text="!Guess a number between 1 to 10!")
lbl_intro.pack()
lbl_number=Label(root,text="Guess Number")
lbl_number.pack()
num_entry=Entry(root,font=("Helvetica",20,"bold"),border=10,bg="lightblue",fg="Black")
num_entry.pack()
cal_btn=Button(root,text="Guess",width=10,height=1,bg="black",font=("Helvetica",13,"bold"),
    fg="white",relief=RIDGE,command=guess)
cal_btn.pack(pady=10)
msg=Label(root,text="",font=("Helvetica",13,"bold"))
msg.pack()
root.mainloop()
