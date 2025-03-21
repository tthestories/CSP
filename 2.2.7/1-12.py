from urllib.parse import urlparse
import subprocess
import tkinter as tk
import tkinter.scrolledtext as tksc
from tkinter.filedialog import asksaveasfilename
import os

def do_command(command):
    global command_textbox
    url_val = url_entry.get().strip()
    if len(url_val) == 0:
        url_val = "::1"  # Default to localhost

    # Strip protocols from URL
    parsed_url = urlparse(url_val)
    url_val = parsed_url.netloc if parsed_url.netloc else url_val

    command_textbox.delete(1.0, tk.END)
    command_textbox.insert(tk.END, f"{command} working on: {url_val}\n")
    command_textbox.update()

    try:
        # Execute the command
        p = subprocess.Popen([command, url_val], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        cmd_results, cmd_errors = p.communicate()

        # Display results/errors
        if cmd_results:
            command_textbox.insert(tk.END, cmd_results.decode())
        if cmd_errors:
            command_textbox.insert(tk.END, cmd_errors.decode())
    except Exception as e:
        command_textbox.insert(tk.END, f"Error: {str(e)}\n")

def mSave():
    filename = asksaveasfilename(defaultextension='.txt', filetypes=[('Text files', '*.txt'), ('Python files', '*.py *.pyw'), ('All files', '*.*')])
    if filename:
        with open(filename, mode='w') as file:
            text_to_save = command_textbox.get("1.0", tk.END)
            file.write(text_to_save)

# Tkinter GUI Setup
root = tk.Tk()
frame = tk.Frame(root)
frame.pack()

# Check for the image file
image_path = "your_image_file.png"
img = tk.PhotoImage(file=image_path) if os.path.exists(image_path) else None
if not img:
    print("Image file not found. Button will render without image.")

# Add Ping Button
ping_btn = tk.Button(frame, text="Check URL Status", 
                     command=lambda: do_command("ping"),
                     compound="center", font=("Comic Sans MS", 12), bd=0, relief="flat",
                     cursor="heart", image=img, bg="red", activebackground="gray")
ping_btn.pack()

# Add Tracert Button
tracert_btn = tk.Button(frame, text="Trace Route (tracert)", 
                        command=lambda: do_command("tracert"),
                        compound="center", font=("Comic Sans MS", 12), bd=0, relief="flat",
                        cursor="heart", bg="blue", activebackground="gray")
tracert_btn.pack()

# Add Nslookup Button
nslookup_btn = tk.Button(frame, text="Name Lookup (nslookup)", 
                         command=lambda: do_command("nslookup"),
                         compound="center", font=("Comic Sans MS", 12), bd=0, relief="flat",
                         cursor="heart", bg="green", activebackground="gray")
nslookup_btn.pack()

save_btn = tk.Button(frame, text="Save", command=mSave)
save_btn.pack()

frame_URL = tk.Frame(root, pady=10, bg="red")
frame_URL.pack()

url_label = tk.Label(frame_URL, text="Enter a URL of interest: ",
                     font=("Comic Sans MS", 14), fg="mediumpurple3", bg="black")
url_label.pack(side=tk.LEFT)
url_entry = tk.Entry(frame_URL, font=("Comic Sans MS", 14))
url_entry.pack(side=tk.LEFT)

frame = tk.Frame(root, bg="black")
frame.pack()

command_textbox = tksc.ScrolledText(frame, height=10, width=100)
command_textbox.pack()

root.mainloop()
