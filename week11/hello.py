import tkinter as tk
window = tk.Tk()
window.title("Hello App")
window.geometry("300x200")
label = tk.Label(window, text="Hello World", font=("Times New Roman", 20))
label.pack(pady=60)
window.mainloop()