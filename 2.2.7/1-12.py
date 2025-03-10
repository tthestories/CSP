import subprocess
import tkinter as tk
import tkinter.scrolledtext as tksc
from tkinter import filedialog
from tkinter.filedialog import asksaveasfilename
import os  # Import os module to check file existence

def do_command(command):
    global command_textbox
    url_val = url_entry.get()
    if len(url_val) == 0:
        # url_val = "127.0.0.1"
        url_val = "::1"
    command_textbox.delete(1.0, tk.END)
    command_textbox.insert(tk.END, command + " working....\n")
    command_textbox.update()

    p = subprocess.Popen(command + ' ' + url_val, stdout=subprocess.PIPE, stderr=subprocess.PIPE) #v2

    cmd_results, cmd_errors = p.communicate()
    command_textbox.insert(tk.END, cmd_results)
    command_textbox.insert(tk.END, cmd_errors)

def mSave():
    filename = asksaveasfilename(defaultextension='.txt', filetypes=(('Text files', '*.txt'), ('Python files', '*.py *.pyw'), ('All files', '*.*')))
    if filename is None:
        return
    file = open(filename, mode='w')
    text_to_save = command_textbox.get("1.0", tk.END)
    
    file.write(text_to_save)
    file.close()    

root = tk.Tk()
frame = tk.Frame(root)
frame.pack()

# Define the image variable
image_path = "your_image_file.png"  # Make sure to replace this with the actual image file path

# Check if the image file exists
if os.path.exists(image_path):
    img = tk.PhotoImage(file=image_path)
else:
    print("Image file not found. Please check the file path.")

# set up button to run the do_command function
ping_btn = tk.Button(frame, text="Check to see if a URL is up and active", 
    command=lambda: do_command("ping"),
    compound="center",
    font=("comic sans", 12),
    bd=0, 
    relief="flat",
    cursor="heart",
    image=img if os.path.exists(image_path) else None, bg="red", activebackground="gray")
ping_btn.pack()

save_btn = tk.Button(frame, text="Save", command=lambda: mSave())
save_btn.pack()

# creates the frame with label for the text box
frame_URL = tk.Frame(root, pady=10, bg="red") # change frame color
frame_URL.pack()

# decorative label
url_label = tk.Label(frame_URL, text="Enter a URL of interest: ", 
    compound="center",
    font=("comic sans", 14),
    bd=0, 
    relief=tk.FLAT, 
    cursor="heart",
    fg="mediumpurple3",
    bg="black")
url_label.pack(side=tk.LEFT)
url_entry = tk.Entry(frame_URL, font=("comic sans", 14)) # change font
url_entry.pack(side=tk.LEFT)

frame = tk.Frame(root, bg="black") # change frame color
frame.pack()

command_textbox = tksc.ScrolledText(frame, height=10, width=100)
command_textbox.pack()

root.mainloop()
