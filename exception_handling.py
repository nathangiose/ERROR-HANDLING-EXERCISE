# Nathan John Giose
# Import everything from tkinter
# Import the messagebox from tkinter


from tkinter import *
from tkinter import messagebox

# Now I will design the GUI

root = Tk()
root.geometry("500x300")
root.config(bg="Green")
root.title("Authentication")


heading = Label(root, text="Please enter login details", font=("Arial", 13))
heading.pack()


#found=False


# Creating Username label and entry

username = Label(root, text="Username", font=("Arial", 10))
username.pack(pady=10)
username_entry = Entry(root, width=40)
username_entry.pack(pady=2)

# Creating Password label and entry
password_label = Label(root, text=" ", font=("Arial", 10))
password_label.pack(pady=7)
password_entry = Entry(root, show="*", width=40)
password_entry.pack(pady=2)

def getUsername():
    found=False
    Usernames = ["Nathan", "Uthmaan", "Tashwill", "Mujaid", "Abdul"]
    Passwords = ["1000", "2000", "3000", "4000", "5000"]
    for x1 in range(len(Usernames)):
       if username_entry.get() == Usernames[x1] and password_entry.get() == Passwords[x1]:
         found=True
    if found==True:
        messagebox.showinfo("Message","Access granted")
        root.destroy()
        import practice
    else:
        messagebox.showinfo("Message","Access Denied")
# Creating login button and function


login_btn = Button(root, text="Login", command=getUsername, font=("Arial", 10), width=30)
login_btn.pack(pady=5)


root.mainloop()
