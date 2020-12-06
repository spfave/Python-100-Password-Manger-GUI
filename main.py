from tkinter import *
from tkinter import messagebox
from password_generator import generate_password


# ---------------------------- PASSWORD GENERATOR --------------------- #
def fill_password():
    entry_password.insert(0, generate_password())


# ---------------------------- SAVE PASSWORD -------------------------- #
def save_password():
    """  """
    website = entry_website.get()
    email_username = entry_email_username.get()
    password = entry_password.get()

    if check_validation(website, email_username, password):
        messagebox.showerror(title="Empty Field",
                             message="You can't leave any field empty")
    else:
        entry_ok = messagebox.askokcancel(
            title=website, message=f"You entered the following details: \nEmail: {email_username} \nPassword: {password} \nIs this what you want to save?")

        if entry_ok:
            with open("password_vault.txt", mode="a") as file:
                file.write(f"{website} | {email_username} | {password}\n")
            reset_entry()


def check_validation(website, email_username, password):
    if len(website) == 0 or len(email_username) == 0 or len(password) == 0:
        return True


def reset_entry():
    entry_password.delete(0, END)
    entry_website.delete(0, END)
    entry_website.focus()


# ---------------------------- UI SETUP ------------------------------- #
# Root window
root = Tk()
root.title("Password Manager")
root.minsize(width=450, height=375)
root.config(padx=50, pady=50)


# Top canvas with logo
canvas_logo = Canvas(root, width=200, height=200)
image_logo = PhotoImage(file="images/logo.png")
canvas_logo.create_image(100, 100, image=image_logo)
canvas_logo.pack()

# Main frame and labels, entries, and buttons
frame = Frame(root)
frame.pack()

label_website = Label(frame, text="Website:", anchor="e")
label_website.grid(row=0, column=0)
label_email_username = Label(frame, text="Email/Username:", anchor="e")
label_email_username.grid(row=1, column=0)
label_password = Label(frame, text="Password:", anchor="e")
label_password.grid(row=2, column=0)

entry_website = Entry(frame, width=40)
entry_website.focus()
entry_website.grid(row=0, column=1, columnspan=2)
entry_email_username = Entry(frame, width=40)
entry_email_username.insert(0, "sebastian@email.com")
entry_email_username.grid(row=1, column=1, columnspan=2)
entry_password = Entry(frame, width=21)
entry_password.grid(row=2, column=1)

button_password_generate = Button(
    frame, text="Generate Password", command=fill_password)
button_password_generate.grid(row=2, column=2)
button_add_password = Button(
    frame, text="Add", width=33, command=save_password)
button_add_password.grid(row=3, column=1, columnspan=2)

root.mainloop()
