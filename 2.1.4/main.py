import tkinter as tk

root = tk.Tk()
root.wm_geometry("200x100")
frame_login = tk.Frame(root)
frame_login.grid()

lbl_username = tk.Label(frame_login, text='Username:')
lbl_username.pack()
ent_username = tk.Entry(frame_login, bd=3)
ent_username.pack(pady=5)

lbl_Pass = tk.Label(frame_login,text="Password:",font="Courier")
lbl_Pass.pack()
ent_pass = tk.Entry(frame_login, bd=3)
ent_pass.pack(pady=5)

root.mainloop()
