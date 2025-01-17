from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
#Password Generator Project
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = []


    for char in range(nr_letters):
      password_list.append(random.choice(letters))

    for char in range(nr_symbols):
      password_list += random.choice(symbols)

    for char in range(nr_numbers):
      password_list += random.choice(numbers)

    random.shuffle(password_list)

    password = ""
    for char in password_list:
      password += char
    password_input.insert(0,password)
    pyperclip.copy(password)
    print(f"Your password is: {password}")


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website=website_input.get()
    email=email_input.get()
    password=password_input.get()
    new_data={
        website:{
            "email":email,
            "password":password,
        }
    }

    if len(website)==0 or len(password)==0:
        messagebox.showinfo(title="Oops",message="Please make sure you haven't left any field empty")
    else:
        try:
            with open("data.json","r") as data_file:
                #reading old data
                data=json.load(data_file)
                #updating old data with new_data
                data.update(new_data)
            with open("data.json","w") as data_file:
                json.dump(data,data_file,indent=4)
        except FileNotFoundError:
            with open("data.json","w") as data_file:
                json.dump(new_data,data_file,indent=4)
        website_input.delete(0,END)
        password_input.delete(0,END)
        email_input.delete(0,END)
        email_input.insert(0, "test@gmail.com")
def find_password():
    website=website_input.get()
    try:
        with open("data.json","r") as data_file:
            data=json.load(data_file)
        if website in data.keys():
            req=data[website]
            req_email=req["email"]
            req_password=req["password"]
            messagebox.showinfo(title="Found",message=f"email: {req_email}\npassword: {req_password}")
        else:
            raise KeyError
    except FileNotFoundError:
        messagebox.showinfo(title="Not found",message="No data file found")
    except KeyError:
        messagebox.showinfo(title='Error',message="No detail of the website exists")





# ---------------------------- UI SETUP ------------------------------- #

window=Tk()
window.title("Password Manager")
window.config(padx=50,pady=50)

canvas=Canvas(width=200,height=200)
logo_img=PhotoImage(file="logo.png")
canvas.create_image(100,100,image=logo_img)
canvas.grid(column=1,row=0)

website_label=Label(text="Website:")
website_label.grid(column=0,row=1)

website_input=Entry(width=35)
website_input.grid(column=1,row=1)
website_input.focus()

search=Button(text="Search",command=find_password)
search.grid(column=2,row=1)


email_label=Label(text="Email/Username:")
email_label.grid(column=0,row=2)

email_input=Entry(width=35)
email_input.grid(column=1,row=2,columnspan=2)
email_input.insert(0,"test@gmail.com")

password_label=Label(text="Password:")
password_label.grid(column=0,row=3)

password_input=Entry(width=17)
password_input.grid(column=1,row=3)

generate_password=Button(text="Generate Password",command=generate_password)
generate_password.grid(column=2,row=3)

add=Button(text="Add",width=36,command=save)
add.grid(column=1,row=4,columnspan=2)


















window.mainloop()