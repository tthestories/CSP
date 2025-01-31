import tkinter as tk
from tkinter import messagebox
import re

def validate_username(username):
    return len(username) > 8

def validate_password(password):
    if len(password) < 8 or len(password) > 24:
        return "Password must be between 8 and 24 characters long."
    if not re.search(r'[A-Za-z]', password):
        return "Password must contain at least one letter."
    if not re.search(r'[0-9]', password):
        return "Password must contain at least one number."
    return None

def submit():
    username = entry_username.get()
    password = entry_password.get()

    if not validate_username(username):
        messagebox.showerror("Error", "Username must be longer than 8 characters.")
        return
    
    validation_error = validate_password(password)
    if validation_error:
        messagebox.showerror("Error", validation_error)
        return
    
    messagebox.showinfo("Success", f"The username {username} and password {password} are saved.")

root = tk.Tk()
root.title("User Registration")

label_username = tk.Label(root, text="Username:")
label_username.grid(row=0, column=0, padx=10, pady=10)
entry_username = tk.Entry(root)
entry_username.grid(row=0, column=1, padx=10, pady=10)

label_password = tk.Label(root, text="Password:")
label_password.grid(row=1, column=0, padx=10, pady=10)
entry_password = tk.Entry(root, show='*')
entry_password.grid(row=1, column=1, padx=10, pady=10)

button_submit = tk.Button(root, text="Submit", command=submit)
button_submit.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

root.mainloop()
