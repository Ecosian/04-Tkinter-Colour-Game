import tkinter
import tkinter as tk
from tkinter import *
import tkinter as tk 
import random 
 
colours = ['Red','Blue','Green','Pink','Black','Orange','White','Purple','Brown'] 
score = 0
timeleft = 60

def data():
    name1_info = (name1.get())
    score_info = str(score)
    
    file = open("Score.txt", "a")
    file.write(name1_info)
    file.write(", Score: ")
    file.write(str(score_info))
    file.write(".")
    file.write("\n")
    file.close()
   
    name1.delete(0, END)
    score

def startGame(event): 
	if timeleft == 60: 
		countdown() 
	nextColour() 

def nextColour(): 
	global score 
	global timeleft 
	if timeleft > 0: 
		e.focus_set() 
		if e.get().lower() == colours[1].lower(): score += 1
		e.delete(0, tkinter.END) 
		random.shuffle(colours) 
		label.config(fg = str(colours[1]), text = str(colours[0])) 
		scoreLabel.config(text = "Score: " + str(score)) 

def countdown(): 
	global timeleft 
	if timeleft > 0: 
		timeleft -= 1
		timeLabel.config(text = "Time left: "+ str(timeleft)) 
		timeLabel.after(1000, countdown) 

window = Tk()
window.title("GUI colour game")
window.geometry("350x250") 
window.resizable(0,0)
window.iconbitmap('colour.ico')
name = Label(window, text = "Name:", font = "Coral")
name.grid(row=0, column=0)

name1 = Entry(window, width=15)
name1.grid(row=2, column=0)

instructions = Label(window, text = "Type in the colour of the words!", font = ('Calibri', 20)) 
instructions.grid(row=3, column=0) 

scoreLabel = Label(window, text = "Type Name and press Enter to start", font = ('Calibri', 16)) 
scoreLabel.grid(row=4, column=0) 

timeLabel = Label(window, text = "Time left: " + str(timeleft), font = ('Calibri', 15)) 
timeLabel.grid(row=5, column=0) 

label = Label(window, font = ('Calibri', 30)) 
label.grid(row=6, column=0) 

e = Entry(window, width=20) 
window.bind('<Return>', startGame) 
e.grid(row=7, column=0) 
e.focus_set() 

btn = Button(window, text = "Submit", width=5, command = data)
btn.grid(row=15, column=0)

window.mainloop() 

