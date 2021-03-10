import tkinter
import time


def move_up():
	canv.move(left,0,-5)
	get_other_move()

def move_down():
	canv.move(left,0,5)
	get_other_move()

def get_other_move():
	




print("Welcome to SuperCrappyPong")


window = tkinter.Tk()
window.geometry("1200x600")
window.title("SuperCrappyPong")


canv = tkinter.Canvas(window)
#canv.geometry("600x600")
#canv.configure(scrollregion = (-300,-300,300,300))
canv.configure(width=1200, height=600)

left = canv.create_rectangle(5,5,10,100, fill ="black", outline = "black")
right = canv.create_rectangle(1190,5,1195,100, fill ="black", outline = "black")
ball = canv.create_rectangle(595,295,605,305, fill = "black", outline = "black")

canv.pack()

window.bind("<KeyPress-Up>", lambda e: move_up())
window.bind("<KeyPress-Down>", lambda e: move_down())

#rectangle.pack()

window.mainloop()


