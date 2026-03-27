import tkinter as tk
from tkinter import messagebox, filedialog
window = tk.Tk()
window.title("Advanced GUI App")
window.geometry("500x400")
def open_file():
    file = filedialog.askopenfilename()
    if file:
        messagebox.showinfo("File Selected", file)
def exit_app():
    window.quit()
menu_bar = tk.Menu(window)
file_menu = tk.Menu(menu_bar, tearoff=0)
file_menu.add_command(label="Open", command=open_file)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=exit_app)
menu_bar.add_cascade(label="File", menu=file_menu)
window.config(menu=menu_bar)
frame = tk.Frame(window)
frame.pack(pady=20)
scrollbar = tk.Scrollbar(frame)
scrollbar.pack(side="right", fill="y")
listbox = tk.Listbox(frame, yscrollcommand=scrollbar.set, height=8)
items = [
    "Python", "Java", "C", "C++", "JavaScript", "Go", "Rust", "Kotlin", "Swift",
    "HTML", "CSS", "SQL", "TypeScript", "Dart", "R", "MATLAB", "Perl", "Scala",
    "Haskell", "Lua", "Shell", "Assembly", "COBOL", "Fortran", "Pascal",
    "Objective-C", "Groovy", "Julia", "Crystal", "Zig", "Nim", "Elixir",
    "Erlang", "PowerShell", "Bash", "Hack", "OCaml", "ReasonML",
    "Visual Basic", "Delphi", "Scratch", "Smalltalk", "Ada",
    "Prolog", "VHDL", "Verilog", "Golang", "SML", "F#", "Chapel"
]
for item in items:
    listbox.insert(tk.END, item)
listbox.pack(side="left")
scrollbar.config(command=listbox.yview)
def show_selected():
    selected = listbox.curselection()
    if selected:
        item = listbox.get(selected)
        messagebox.showinfo("Selected Item", item)
    else:
        messagebox.showwarning("Warning", "No item selected")
tk.Button(window, text="Show Selected", command=show_selected).pack(pady=10)
def show_option(option):
    messagebox.showinfo("Option Selected", option)
menubtn = tk.Menubutton(window, text="Options", relief="raised")
menubtn.menu = tk.Menu(menubtn, tearoff=0)
menubtn.menu.add_command(label="Option 1", command=lambda: show_option("Option 1"))
menubtn.menu.add_command(label="Option 2", command=lambda: show_option("Option 2"))
menubtn.config(menu=menubtn.menu)
menubtn.pack(pady=10)
window.mainloop()