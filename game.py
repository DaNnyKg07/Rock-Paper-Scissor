from random import randint
from tkinter import *
from PIL import Image, ImageTk


# main window
root = Tk()
root.title("Rock Paper Scissor")
root.configure(background="turquoise")

# picture
rock_img_user = ImageTk.PhotoImage(Image.open("images/rock_user.png"))
paper_img_user = ImageTk.PhotoImage(Image.open("images/paper_user.png"))
scissor_img_user = ImageTk.PhotoImage(Image.open("images/scissors_user.png"))
rock_img_comp = ImageTk.PhotoImage(Image.open("images/rock_comp.png"))
paper_img_comp = ImageTk.PhotoImage(Image.open("images/paper_comp.png"))
scissor_img_comp = ImageTk.PhotoImage(Image.open("images/scissors_comp.png"))

# insert picture
user_label = Label(root, image=scissor_img_user, bg="turquoise")
comp_label = Label(root, image=scissor_img_comp, bg="turquoise")
user_label.grid(row=1, column=0)
comp_label.grid(row=1, column=4)


# scores
playerScore = Label(root, text=0, font=("Arial Bold",15), bg="turquoise", fg="black")
computerScore = Label(root, text=0, font=("Arial Bold",15), bg="turquoise", fg="black")
playerScore.grid(row=1, column=1)
computerScore.grid(row=1, column=3)

# indicators
user = Label(root, font=("Arial Bold",15), text="USER", bg="turquoise", fg="black")
computer = Label(root, font=("Arial Bold",15), text="COMPUTER",
                       bg="turquoise", fg="black")
computer.grid(row=0, column=3)
user.grid(row=0, column=1)

# messages
msg = Label(root, font=("Arial Bold",15), bg="turquoise", fg="black")
msg.grid(row=3, column=2)

# update message


def updateMessage(x):
    msg['text'] = x

# update user score


def updateUserScore():
    score = int(playerScore["text"])
    score += 1
    playerScore["text"] = str(score)

# update computer score


def updateCompScore():
    score = int(computerScore["text"])
    score += 1
    computerScore["text"] = str(score)

# check winner


def checkWin(player, computer):
    if player == computer:
        updateMessage("Its a tie!!!")
    elif player == "rock":
        if computer == "paper":
            updateMessage("You lost")
            updateCompScore()
        else:
            updateMessage("You Won")
            updateUserScore()
    elif player == "paper":
        if computer == "scissor":
            updateMessage("You lost")
            updateCompScore()
        else:
            updateMessage("You Won")
            updateUserScore()
    elif player == "scissor":
        if computer == "rock":
            updateMessage("You lost")
            updateCompScore()
        else:
            updateMessage("You Won")
            updateUserScore()

    else:
        pass


# update choices

choices = ["rock", "paper", "scissor"]


def updateChoice(x):

    # for computer
    compChoice = choices[randint(0, 2)]
    if compChoice == "rock":
        comp_label.configure(image=rock_img_comp)
    elif compChoice == "paper":
        comp_label.configure(image=paper_img_comp)
    else:
        comp_label.configure(image=scissor_img_comp)


# for user
    if x == "rock":
        user_label.configure(image=rock_img_user)
    elif x == "paper":
        user_label.configure(image=paper_img_user)
    else:
        user_label.configure(image=scissor_img_user)

    checkWin(x, compChoice)


# buttons
rock = Button(root, width=20, height=2, text="ROCK", 
              bg="#FF3E4D", fg="black", command=lambda: updateChoice("rock")).grid(row=2, column=1)
paper = Button(root, width=20, height=2, text="PAPER",
               bg="#FAD02E", fg="black", command=lambda: updateChoice("paper")).grid(row=2, column=2)
scissor = Button(root, width=20, height=2, text="SCISSOR",
                 bg="#0ABDE3", fg="black", command=lambda: updateChoice("scissor")).grid(row=2, column=3)

root.mainloop()