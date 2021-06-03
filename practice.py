from tkinter import *
from tkinter import messagebox
window = Tk()
window.geometry("300x300")
window.config(bg="Aqua")
window.title("Exception Handling")

amount_label = Label(window, text="Please enter amount in account")
amount_label.pack()
amount_entry = Entry(window)
amount_entry.pack()

# Error handling function
def check():
    funds = amount_entry.get()
    try:
        funds = int(funds)
        if funds < 3000:
            messagebox.showerror("Insufficient Funds", "Please deposit more funds.")
        else:
            messagebox.showinfo("Congratulations", "You qualify for the trip to Malaysia")
    except ValueError:
        messagebox.showerror("Error", "Please insert a number.")


check_btn = Button(window, text="Check Qualification", bg="Aqua", command=check)
check_btn.pack()
window.mainloop()
