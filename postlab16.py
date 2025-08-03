import tkinter as tk

def increment():
    global count
    count += 1
    label.config(text=f"Counter: {count}")

root = tk.Tk()
count = 0

label = tk.Label(root, text=f"Counter: {count}", font=("Arial", 18))
label.pack(pady=10)

button = tk.Button(root, text="Increment", command=increment, font=("Arial", 14))
button.pack(pady=5)

root.mainloop()
