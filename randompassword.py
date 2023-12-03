import tkinter as tk
import random
import string


def generate_password():
    length = lengthvar.get()
    if length < 8:
        passwordvar.set("Invalid length")
        return
    lowercase = random.choice(string.ascii_lowercase)
    uppercase = random.choice(string.ascii_uppercase)
    digit = random.choice(string.digits)
    symbol = '!@#$%^&*'

    passwordchars = string.ascii_letters + string.digits + '!@#$%^&*'
    password = lowercase + uppercase + digit + symbol + ''.join(random.choice(passwordchars) for _ in range(length - 4))

    passwordlist = list(password)
    random.SystemRandom().shuffle(passwordlist)
    password = ''.join(passwordlist)
    passwordvar.set(password)


root = tk.Tk()
root.title("Random Password Generator")
root.geometry("500x150")

font_style=('Georgia',10)

lengthvar = tk.IntVar()
passwordvar = tk.StringVar()

lengthlabel = tk.Label(root, text='Enter the password length:',font=font_style)
lengthlabel.pack()
lengthentry = tk.Entry(root, textvariable=lengthvar,font=font_style)
lengthentry.pack()

alertlabel = tk.Label(root, text='The minimum length of the password is 8',font=font_style)
alertlabel.pack()

generatebutton = tk.Button(root, text='Generate Password', command=generate_password,font=font_style)
generatebutton.pack()

passwordlabel = tk.Label(root, text='The generated password is:',font=font_style)
passwordlabel.pack()

passwordentry = tk.Entry(root, textvariable=passwordvar, state='readonly',font=font_style)
passwordentry.pack()

root.mainloop()
