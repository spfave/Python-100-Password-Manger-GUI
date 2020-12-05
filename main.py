from tkinter import *


# ---------------------------- PASSWORD GENERATOR --------------------- #


# ---------------------------- SAVE PASSWORD -------------------------- #


# ---------------------------- UI SETUP ------------------------------- #
root = Tk()
root.title("Password Manager")
root.config(padx=20, pady=20)


canvas_logo = Canvas(width=200, height=200)
image_logo = PhotoImage(file="images/logo.png")
# default anchor is "center"
canvas_logo.create_image(100, 100, image=image_logo, anchor="center")
canvas_logo.pack()


root.mainloop()
