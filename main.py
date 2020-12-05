from tkinter import *


# ---------------------------- PASSWORD GENERATOR --------------------- #


# ---------------------------- SAVE PASSWORD -------------------------- #


# ---------------------------- UI SETUP ------------------------------- #
root = Tk()
root.title("Password Manager")
root.config(padx=20, pady=20)


canvas_logo = Canvas(root, width=200, height=200)
image_logo = PhotoImage(file="images/logo.png")
# default anchor is "center"
canvas_logo.create_image(100, 100, image=image_logo, anchor="center")
canvas_logo.pack()

frame = Frame(root)
frame.pack()

label_website = Label(frame, text="Website:")
label_website.grid(row=0, column=0)
label_email_username = Label(frame, text="Email/Username:")
label_email_username.grid(row=1, column=0)
label_password = Label(frame, text="Password:")
label_password.grid(row=2, column=0)


root.mainloop()
