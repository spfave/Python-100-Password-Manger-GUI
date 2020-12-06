from tkinter import *
from tkinter import messagebox
from password_generator import generate_password
import json
import pyperclip


# ---------------------------- PASSWORD GENERATOR --------------------- #
def fill_password():
    new_password = generate_password()
    entry_password.delete(0, END)
    entry_password.insert(0, new_password)
    pyperclip.copy(new_password)


# ---------------------------- SAVE PASSWORD -------------------------- #
def save_password():
    website = entry_website.get()
    email_username = entry_email_username.get()
    password = entry_password.get()

    if check_validation(website, email_username, password):
        messagebox.showerror(title="Empty Field",
                             message="You can't leave any field empty")
    else:
        new_data = {
            website: {
                "email": email_username,
                "password": password,
            },
        }

        try:
            with open("password_vault.json", mode="r") as data_file:
                data = json.load(data_file)  # Read old data
        except FileNotFoundError:
            with open("password_vault.json", mode="w") as data_file:
                json.dump(new_data, data_file, indent=4)  # Saving updated data
        else:
            data.update(new_data)   # Updating old data with new data
            with open("password_vault.json", mode="w") as data_file:
                json.dump(data, data_file, indent=4)  # Saving updated data
        finally:
            reset_entry()


def check_validation(website, email_username, password):
    if len(website) == 0 or len(email_username) == 0 or len(password) == 0:
        return True


def reset_entry():
    entry_password.delete(0, END)
    entry_website.delete(0, END)
    entry_website.focus()


# ---------------------------- FIND PASSWORD -------------------------- #
def find_password():
    """  """
    website = entry_website.get()

    if len(website) > 0:
        try:
            with open("password_vault.json", mode="r") as data_file:
                data = json.load(data_file)
        except FileNotFoundError:
            messagebox.showinfo(title="Error", message="No data file found")
        else:
            if website in data:
                email = data[website]["email"]
                password = data[website]["password"]
                messagebox.showinfo(title=website, message=f"Email: {email}\nPassword: {password}",
                                    icon="question")  # icon = question for no sound
            else:
                messagebox.showinfo(
                    title="No data", message=f"No information for {website} exists")
    else:
        messagebox.showinfo(title="Error", message="No website entered")


# ---------------------------- UI SETUP ------------------------------- #
# Root window
root = Tk()
root.title("Password Manager")
root.minsize(width=450, height=400)
root.config(padx=50, pady=50)


# Top canvas with logo
canvas_logo = Canvas(root, width=200, height=200)
image_logo = PhotoImage(file="images/logo.png")
canvas_logo.create_image(100, 100, image=image_logo)
canvas_logo.pack()

# Main frame and labels, entries, and buttons
frame = Frame(root)
frame.pack()

# Labels
label_website = Label(frame, text="Website:")
label_website.grid(row=0, column=0, sticky="w")
label_email_username = Label(frame, text="Email/Username:")
label_email_username.grid(row=1, column=0, sticky="w")
label_password = Label(frame, text="Password:")
label_password.grid(row=2, column=0, sticky="w")

# Entries
entry_website = Entry(frame, width=30)
entry_website.focus()
entry_website.grid(row=0, column=1)
entry_email_username = Entry(frame, width=30)
entry_email_username.insert(0, "sebastian@email.com")
entry_email_username.grid(row=1, column=1)
entry_password = Entry(frame, width=30)
entry_password.grid(row=2, column=1)

# Buttons
button_password_search = Button(
    frame, text="Search", command=find_password, width=15)
button_password_search.grid(row=0, column=2)
button_password_generate = Button(
    frame, text="Generate Password", command=fill_password)
button_password_generate.grid(row=2, column=2)
button_add_password = Button(
    frame, text="Add", width=41, command=save_password)
button_add_password.grid(row=3, column=1, columnspan=2)

root.mainloop()
