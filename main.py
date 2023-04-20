from tkinter import *
import string
import random


# --------------------------- ADD PASSWORD ---------------------------- #
def append_password():
    with open("website_number.txt", mode="r") as website_n:
        n = int(website_n.read())
        n += 1
    with open("passwords.txt", mode="a") as passwords_file:
        passwords_file.write(f"{n}.Website: {website_entry.get().title()}"
                             f"\nEmail/Username: {email_username_entry.get().lower()}"
                             f"\nPassword: {password_entry.get()}\n")
    with open("website_number.txt", mode="w") as data:
        data.write(f"{n}")


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
website_entry = Entry(width=50)
website_entry.grid(row=1, column=1, columnspan=2)

email_username_entry = Entry(width=50)
email_username_entry.grid(row=2, column=1, columnspan=2)

password_entry = Entry(width=32)
password_entry.grid(row=3, column=1)

# Buttons
gen_password_button = Button(text="Generate Password", command=generate_password)
gen_password_button.grid(row=3, column=2)

add_password = Button(text="Add", width=43, command=append_password)
add_password.grid(row=4, column=1, columnspan=2)

window.mainloop()
