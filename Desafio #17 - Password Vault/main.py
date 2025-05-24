from tkinter import Tk, Canvas, PhotoImage, END
from tkinter import ttk
from tkinter import messagebox
from random import randint, choice, shuffle
from pyperclip import copy
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_list = []
    password_list += [choice(letters) for _ in range(randint(8, 10))]
    password_list += [choice(symbols) for _ in range(randint(2, 4))]
    password_list += [choice(numbers) for _ in range(randint(2, 4))]

    shuffle(password_list)
    password = "".join(password_list)
    copy(password)
    input_pass.delete(0, END)
    input_pass.insert(0, password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def validate_fields():
    site = input_website.get()
    username = input_mail.get()
    password = input_pass.get()
    if not site or not username:
        messagebox.showwarning(title="Double Check!", message="Please, do not leave any fields empty!")
        input_website.focus()
    else:
        save(site, username, password)

def save(site, username, password):
    creds_dict = {site: {'email': username, 'password': password},}

    choice = messagebox.askokcancel(title=site or "Confirmation", message=f"These are the details entered: \n{site}\n{username}\n{password}\nSave these credentials?")
    if choice:
        try:
            with open(file="Day 29/passwords.json", mode="r", encoding="UTF-8") as file:
                file_content = json.load(file)
                file_content.update(creds_dict)
            with open(file="Day 29/passwords.json", mode="w", encoding="UTF-8") as file:
                json.dump(file_content, file, indent=4)
        except FileNotFoundError:
            with open(file="Day 29/passwords.json", mode="w", encoding="UTF-8") as file:
                json.dump(creds_dict, file, indent=4)
            messagebox.showwarning(message="file not found, creating new password file.")
            print("file not found, creating new password file.")
        finally:
            messagebox.showinfo(title="Sucess!", message="File saved successfully")
            print("File saved successfully")
            input_website.delete(0, END)
            input_mail.delete(0, END)
            input_pass.delete(0, END)
            input_mail.insert(0, "example@gmail.com")
    else:
        return

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pass Manager")
window.config(padx=20, pady=20, bg="#ffffff")

logo = PhotoImage(file=r"Desafio #17 - Password Vault/image_250.png")

#Widgets
canvas = Canvas(width=250, height=250, background="#ffffff")
canvas.create_image(125,125, image=logo)
lbl_website = ttk.Label(text="Website", width=20, anchor="e")
lbl_website.focus()
lbl_mail = ttk.Label(text="Username",  width=20, anchor="e")
lbl_pass = ttk.Label(text="Password",  width=20, anchor="e")

btn_genpass =  ttk.Button(text="Generate Password", width=20, command=generate_password)
btn_addcreds =  ttk.Button(text="Add", command=validate_fields)

input_website = ttk.Entry()
input_mail = ttk.Entry()
input_mail.insert(0, "example@gmail.com")
input_pass = ttk.Entry()


#layout
canvas.grid(column=1, row=0, sticky="e")

lbl_website.grid(column=0, row=1, pady=8, padx=8, sticky="e")
input_website.grid(column=1, row=1, columnspan=2, sticky="we")

lbl_mail.grid(column=0, row=2, pady=8)
input_mail.grid(column=1, row=2, columnspan=2, sticky="we")

lbl_pass.grid(column=0, row=3, pady=8)
input_pass.grid(column=1, row=3, columnspan=1,sticky="we")

btn_genpass.grid(column=2, row=3, sticky="w", padx=(8,0))
btn_addcreds.grid(column=1, row=4, columnspan=2, sticky="we")

#Commandos!
window.bind('<Return>', lambda event: validate_fields())
window.mainloop()