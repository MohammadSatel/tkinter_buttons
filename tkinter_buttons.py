import tkinter as tk

def change_color(button):
    color = button.cget("text")
    button.configure(bg=color)

root = tk.Tk()
root.title("Button Color Changer")

# Create Red Button
red_button = tk.Button(root, text="red", bg="black", fg="red", command=lambda: change_color(red_button))
red_button.pack()

# Create Blue Button
blue_button = tk.Button(root, text="blue", bg="black", fg="blue", command=lambda: change_color(blue_button))
blue_button.pack()

# Create Green Button
green_button = tk.Button(root, text="green", bg="black", fg="green", command=lambda: change_color(green_button))
green_button.pack()

root.mainloop()
