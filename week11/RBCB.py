import tkinter as tk
from tkinter import messagebox
window = tk.Tk()
window.title("Preferences Form")
window.geometry("350x300")
tk.Label(window, text="Select Your Hobbies:").pack(anchor="w", padx=10)
hobby1 = tk.IntVar()
hobby2 = tk.IntVar()
hobby3 = tk.IntVar()
tk.Checkbutton(window, text="Reading", variable=hobby1).pack(anchor="w", padx=20)
tk.Checkbutton(window, text="Gaming", variable=hobby2).pack(anchor="w", padx=20)
tk.Checkbutton(window, text="Sports", variable=hobby3).pack(anchor="w", padx=20)
tk.Label(window, text="\nSelect Your Gender:").pack(anchor="w", padx=10)
gender = tk.StringVar()
gender.set("None")  # default value
tk.Radiobutton(window, text="Male", variable=gender, value="Male").pack(anchor="w", padx=20)
tk.Radiobutton(window, text="Female", variable=gender, value="Female").pack(anchor="w", padx=20)
tk.Radiobutton(window, text="Other", variable=gender, value="Other").pack(anchor="w", padx=20)
def submit():
    hobbies = []
    if hobby1.get() == 1:
        hobbies.append("Reading")
    if hobby2.get() == 1:
        hobbies.append("Gaming")
    if hobby3.get() == 1:
        hobbies.append("Sports")
    selected_gender = gender.get()
    messagebox.showinfo("Your Selection",
                        f"Hobbies: {', '.join(hobbies)}\nGender: {selected_gender}")
tk.Button(window, text="Submit", command=submit).pack(pady=15)
window.mainloop()