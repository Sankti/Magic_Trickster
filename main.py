from tkinter import *

window = Tk()
window.geometry("360x430")
window.title("Magic Trickster")
root = Frame(window, borderwidth=2, relief="solid", background="midnightblue")

message_box = Text(root, width=42, height=3, wrap=WORD, fg="black", font=("Courier New", 10))
message_box.config(state=DISABLED)

def write(string):
    message_box.config(state=NORMAL)
    message_box.insert("end", string)
    message_box.see("end")
    message_box.config(state=DISABLED)

# PROGRAM MECHANICS

write("Ha haaa! I am the  mighty Amon Zandalar! \nPlease think of a number from 0 to 99.")

low = 0
high = 100
guess = int((low + high) / 2)
count = 1

write("\nIs your number " + str(guess) + "?")

def too_low():
    global high, guess, count
    high = int(guess)
    guess = int((low + high) / 2)
    write("\nIs your number " + str(guess) + "?")
    count += 1

def too_high():
    global low, guess, count
    low = int(guess)
    guess = int((low + high) / 2)
    write("\nIs your number " + str(guess) + "?")
    count += 1

def win():
    if count == 1:
        answer = "\nHa! I've got your number! It took me", str(count), "guess to figure it out!"
        write(answer)
    else:
        answer = "\nHa! I've got your number! It took me", str(count), "guesses to figure it out!"
        write(answer)

# SETUP

title = Label(root, text="Magic Trickster", background="midnightblue", fg="white", font=("Times New Roman", 20, "bold"))
magik_img = PhotoImage(file="magik.png")
magik_photo_label = Label(root, image=magik_img)
yes_button = Button(root, text="Yes", background="green", fg="white", font=("Courier New", 12, "bold"), command=lambda: win())
too_high_button = Button(root, text="Too low", background="red", fg="white", font=("Courier New", 12, "bold"), command=lambda: too_high())
too_low_button = Button(root, text="Too high", background="red", fg="white", font=("Courier New", 12, "bold"), command=lambda: too_low())

# LAYOUT SETUP

root.pack()
title.grid(row=0, columnspan=3, padx=10)
magik_photo_label.grid(row=1, columnspan=3, pady=10)
message_box.grid(row=2, columnspan=3, padx=10, pady=5)
yes_button.grid(row=3, column=0, pady=10)
too_high_button.grid(row=3, column=1, pady=10)
too_low_button.grid(row=3, column=2, pady=10)

# COMMENCING LOOP

window.mainloop()
