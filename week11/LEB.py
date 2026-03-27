import tkinter as tk
from tkinter import messagebox
window = tk.Tk()
window.title("User Form")
window.geometry("350x250")
name_label = tk.Label(window, text="Enter Name:")
name_label.grid(row=0, column=0, padx=10, pady=10)
age_label = tk.Label(window, text="Enter Age:")
age_label.grid(row=1, column=0, padx=10, pady=10)
name_entry = tk.Entry(window)
name_entry.grid(row=0, column=1, padx=10, pady=10)
age_entry = tk.Entry(window)
age_entry.grid(row=1, column=1, padx=10, pady=10)
def submit_data():
    name = name_entry.get()
    age = age_entry.get()
    if name == "" or age == "":
        messagebox.showwarning("Warning", "Please fill all fields!")
    else:
        messagebox.showinfo("Submitted", f"Name: {name}\nAge: {age}")
submit_button = tk.Button(window, text="Submit", command=submit_data)
submit_button.grid(row=2, column=0, columnspan=2, pady=20)
window.mainloop()