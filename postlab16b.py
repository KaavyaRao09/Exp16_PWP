import tkinter as tk

def display_text():
    text = entry.get()
    label.config(text=f"You typed: {text}")

root = tk.Tk()

entry = tk.Entry(root, font=("Arial", 14))
entry.pack(pady=10)

button = tk.Button(root, text="Show Text", command=display_text, font=("Arial", 14))
button.pack(pady=5)

label = tk.Label(root, text="", font=("Arial", 16))
label.pack(pady=10)

root.mainloop()
