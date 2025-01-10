import tkinter as tk

root = tk.Tk()
root.wm_geometry("200x150")

frame_auth = tk.Frame(root)
frame_auth.grid(column=0, row=0, sticky="news")

frame_login = tk.Frame(root)
frame_login.grid(column=0, row=0, sticky="news")
frame_login.tkraise

lbl_username = tk.Label(frame_login, text='Username:',font="Courier")
lbl_username.pack()
ent_username = tk.Entry(frame_login, bd=3)
ent_username.pack(pady=5,padx=5)

lbl_Pass = tk.Label(frame_login,text="Password:",font="Courier")
lbl_Pass.pack()
ent_pass = tk.Entry(frame_login, bd=3)
ent_pass.pack(pady=5,padx=5)

login = tk.Button(frame_login,text="Login",font="Courier",test_my_button)
login.pack()

def test_my_button:
  

root.mainloop()
