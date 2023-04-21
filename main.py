from tkinter import *
from tkinter import messagebox
import string
import random
import json


# --------------------------- SEARCH DATA ---------------------------- #
def search_data():
    website = website_entry.get().title()
    try:
        with open("passwords.json") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showerror(title="Error", message="No Data File Found")
    else:
        if website in data:
            email = data[website]["email"]
            password = data[website]["password"]
            new_message = f"Email: {email}\nPassword: {password}"
            messagebox.showinfo(title=website, message=new_message)
        else:
            messagebox.showerror(title="Error", message=f"No details for {website} exists.")


# --------------------------- ADD PASSWORD ---------------------------- #
def append_password():
    website = website_entry.get().title()
    email = email_username_entry.get().lower()
    password = password_entry.get()
    new_data = {
        website: {
            "email": email,
            "password": password,
        }
    }

    if len(password_entry.get()) == 0 and len(website_entry.get()) == 0:
        messagebox.showerror(title="Error", message="Please do NOT leave any fields empty!")
    else:
        try:
            is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered: \nEmail: {email} "
                                                                  f"\nPassword: {password} \nIs it ok to save?")
            if is_ok:
                with open("passwords.json", mode="r") as passwords_file:
                    # Reading old data
                    data = json.load(passwords_file)
        except FileNotFoundError:
            with open("passwords.json", mode="w") as passwords_file:
                json.dump(new_data, passwords_file, indent=4)
        else:
            # Updating old data with new data
            data.update(new_data)

            with open("passwords.json", mode="w") as passwords_file:
                # Saving updated data
                json.dump(data, passwords_file, indent=4)
        finally:
            website_entry.delete(0, END)
            password_entry.delete(0, END)


# ------------------------ GENERATE PASSWORD -------------------------- #
def generate_password():
    lowercase_letters = string.ascii_lowercase
    uppercase_letters = string.ascii_uppercase
    digits = string.digits
    password_signs = "".join(lowercase_letters + uppercase_letters + digits + "!#$*?")
    new_password = "".join(random.sample(password_signs, 15))
    password_entry.insert(END, string=new_password)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
logo = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo)
canvas.grid(row=0, column=1)

# Labels
website_label = Label(text="Website:", pady=10)
website_label.grid(row=1, column=0)

email_username_label = Label(text="Email/Username:", pady=10)
email_username_label.grid(row=2, column=0)

password_label = Label(text="Password:", pady=10)
password_label.grid(row=3, column=0)

# Entries
website_entry = Entry(width=32)
website_entry.grid(row=1, column=1)

email_username_entry = Entry(width=50)
email_username_entry.grid(row=2, column=1, columnspan=2)
email_username_entry.insert(0, "example@gmail.com")

password_entry = Entry(width=32)
password_entry.grid(row=3, column=1)

# Buttons
search_button = Button(text="Search", width=15, command=search_data)
search_button.grid(row=1, column=2)

gen_password_button = Button(text="Generate Password", command=generate_password)
gen_password_button.grid(row=3, column=2)

add_password = Button(text="Add", width=43, command=append_password)
add_password.grid(row=4, column=1, columnspan=2)

window.mainloop()
