from random import *
from tkinter import *
from tkinter import ttk
from tkinter import messagebox

root=Tk()
root.title("Rock-Paper-Scissors Game")
root.geometry("1540x800")
#root.resizable('false','false')
root.config(background="#EAE0C8")
# root.config(background="#D2B48C")

Rock=0
Paper=0
Scissors=0
score={"computer":0,"you":0}
def ifnewround():
    result= messagebox.askyesno(title="New round?",message="Are you sure you want new round?")
    if result:
        global score
        score = {"computer": 0, "you": 0}
        messagebox.showinfo("New score",f"The score is:\n computer:0 \n you:0")

    else: exit()


def ifrock():
    global Rock
    Rock=1
    global Paper
    Paper = 0
    global Scissors
    Scissors = 0
def ifpaper():
    global Paper
    Paper=1
    global Scissors
    Scissors = 0
    global Rock
    Rock = 0
def ifscissors():
    global Scissors
    Scissors=1
    global Paper
    Paper = 0
    global Rock
    Rock = 0

def play():
    global score

    programe_choice = ["Rock", "Paper", "Scissors"]

    other_choice =choice(programe_choice)

    if (other_choice=="Rock" and Rock) or (other_choice=="Paper" and Paper) or (other_choice=="Scissors" and Scissors):
        line_1=f"Comuter chooses {other_choice}\nSO,it's a TIE"
        if Rock:
            your_choice="Rock"
        elif Paper:
            your_choice="Paper"
        else:
            your_choice="Scissors"
        line_1 = f"Comuter chose {other_choice} and you chose {your_choice}\nSO,it's a TIE"
        line2 = f"Still \n computer:{score['computer']}\nyou:{score['you']}"
        alllines=[line_1,line2]
        messagebox.showinfo("The score", "\n".join(alllines))

    elif (other_choice=="Rock" and Scissors) or (other_choice == "Scissors" and Paper) or (other_choice=="Paper" and Rock):
        score["computer"]+=1

        if Rock:
            your_choice="Rock"
        elif Paper:
            your_choice="Paper"
        else:
            your_choice="Scissors"
        line1=f"Comuter chose {other_choice} and you chose {your_choice}  \nComputer Wins!"
        line2=f"computer:{score['computer']}\nyou:{score['you']}"
        alllines_1=[line1,line2]
        messagebox.showinfo("The score","\n".join(alllines_1))
    else:
        if Rock:
            your_choice="Rock"
        elif Paper:
            your_choice="Paper"
        else:
            your_choice="Scissors"
        score["you"] += 1
        line_3=f"Comuter chose {other_choice} and you chose {your_choice}\nYOU WIN!"
        line_4=f"computer:{score['computer']}\nyou:{score['you']}"
        alllines_2=[line_3,line_4]
        messagebox.showinfo("The score", "\n".join(alllines_2))



fram1=Frame(root,bd=0,background="#CCCCFF")##D2B48C
fram1.pack()
#label_1=Label(root,text="Rock-Paper-Scissors Game",font=("cooper black",20),background="#65000B",fg="white")
#label_1.pack(side=TOP)
rock_img=PhotoImage(file=r"C:\Users\dms66\Downloads\R.png")
paper_img=PhotoImage(file=r"C:\Users\dms66\Downloads\p.png")
scissors_img=PhotoImage(file=r"C:\Users\dms66\Downloads\s.png")
rock=Button(fram1,bd=0,image=rock_img,command=ifrock,background="#EAE0C8")#font=("cooper black",16),

rock.grid(row=0,column=0)
paper=Button(fram1,bd=0,image=paper_img,command=ifpaper,background="#EAE0C8")
paper.grid(row=0,column=1)
scissors=Button(fram1,bd=0,image=scissors_img,command=ifscissors,background="#EAE0C8")
scissors.grid(row=0,column=2)
play_btn=Button(root,bd=10,width=30,height=2,background="#008000",fg="white",text="PLAY Now!",font=("cooper black",16),command=play)
play_btn.pack(pady=(20,0))
newround_btn=Button(root,bd=10,width=20,height=2,background="#660000",fg="white",text="New Round!",font=("cooper black",16),command=ifnewround)
newround_btn.pack(pady=(20,1))
















root.mainloop()