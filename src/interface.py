import tkinter as tk

number = 0

def start():
    global number, counter
    number += 1
    counter.config(text=number)

root = tk.Tk()

root.geometry("500x500")
root.iconbitmap('../assets/i.ico')
root.title('Task Manager')

frame = tk.Frame(root, width=100, height=100)
frame.pack()

counter = tk.Label(frame,text=f"{number}")
counter.pack()
tk.Button(text="Start!", background="light blue", width=30, height=5,command=start).pack(padx=10, pady=10)

root.mainloop()
