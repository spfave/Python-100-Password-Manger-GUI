from tkinter import *


# ---------------------------- PASSWORD GENERATOR --------------------- #


# ---------------------------- SAVE PASSWORD -------------------------- #


# ---------------------------- UI SETUP ------------------------------- #
# Root window
root = Tk()
root.title("Password Manager")
root.config(padx=20, pady=20)


# Top canvas with logo
canvas_logo = Canvas(root, width=200, height=200)
image_logo = PhotoImage(file="images/logo.png")
canvas_logo.create_image(100, 100, image=image_logo)
canvas_logo.pack()

# Main frame and labels, entries, and buttons
frame = Frame(root)
frame.pack()

label_website = Label(frame, text="Website:")
label_website.grid(row=0, column=0)
label_email_username = Label(frame, text="Email/Username:")
label_email_username.grid(row=1, column=0)
label_password = Label(frame, text="Password:")
label_password.grid(row=2, column=0)

entry_website = Entry(frame, width=35)
entry_website.grid(row=0, column=1, columnspan=2)
entry_email_username = Entry(frame, width=35)
entry_email_username.grid(row=1, column=1, columnspan=2)
entry_password = Entry(frame, width=21, anchor="w")
entry_password.grid(row=2, column=1)

button_password_generate = Button(frame, text="Genrate Password")

root.mainloop()
