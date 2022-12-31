from tkinter import *
from tkinter import messagebox
from random import shuffle, randint, choice
import pyperclip
import json


# _________________________________________PASSWORD GENERATOR_____________________________________

def password_generator():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v',
               'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q',
               'R',
               'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_list1 = [choice(letters) for _ in range(randint(8, 10))]

    password_list2 = [choice(symbols) for _ in range(randint(2, 4))]

    password_list3 = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_list1 + password_list2 + password_list3

    shuffle(password_list)

    password = "".join(password_list)

    password_entry.insert(END, f"{password}")
    if_yes = messagebox.askyesno(title='New password', message='A new password generated.Do you want to regenerate a '
                                                               'new password?')
    if if_yes:
        password_entry.delete(0, END)
        password_generator()
    else:
        pyperclip.copy(password)


# _________________________________________SAVING USER DATA_______________________________________
def add():
    website = website_entry.get()
    email = email_entry.get()
    password1 = password_entry.get()
    new_data = {
        website: {
            'email': email,
            'password': password1
        }
    }

    if len(website) == 0 or len(email) == 0 or len(password1) == 0:
        messagebox.showerror(title='Empty boxes', message="You can't left any empty boxes")
    else:
        is_ok = messagebox.askokcancel(title='Confirm your details', message=f'your,\nWebsite: {website}\n'
                                                                             f'Email: {email}\nPassword: {password1}')
        if is_ok:
            try:
                with open('data.json', 'r', ) as data_file:
                    data = json.load(data_file)

            except FileNotFoundError:
                with open('data.json', 'w') as data_file:
                    json.dump(new_data, data_file, indent=4)
            else:
                data.update(new_data)
                with open('data.json', 'w') as data_file:
                    json.dump(data, data_file, indent=4)

            finally:
                website_entry.delete(0, END)
                email_entry.delete(0, END)
                email_entry.insert(END, 'anujadilshan8@gmail.com')
                password_entry.delete(0, END)


# ________________________USER INTERFACE SECTION______________________________________________________


window = Tk()
window.title('Password Manager')
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
logo = PhotoImage(file='logo.png')
canvas.create_image(100, 100, image=logo)
canvas.grid(row=0, column=1)

# labels

website_label = Label(text='Website:')
website_label.grid(row=1, column=0)
email_label = Label(text='Email/Username:')
email_label.grid(row=2, column=0)
password_label = Label(text='Password:')
password_label.grid(row=3, column=0)

# entries

website_entry = Entry(width=35)
website_entry.focus()
website_entry.grid(row=1, column=1, columnspan=2)
email_entry = Entry(width=35)
email_entry.insert(END, 'anujadilshan8@gmail.com')
email_entry.grid(row=2, column=1, columnspan=2)
password_entry = Entry(width=21)
password_entry.grid(row=3, column=1)

# buttons

generate_password_button = Button(text='Generate Password', highlightthickness=0, command=password_generator)
generate_password_button.grid(row=3, column=2)
add_button = Button(text='Add', width=36, highlightthickness=0, command=add)
add_button.grid(row=4, column=1, columnspan=2)

window.mainloop()
