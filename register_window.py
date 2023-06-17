import tkinter as tk
import csv
from tkinter import messagebox
from back import back

from const import USERS_FILE


def create_register_window(parentWindow: tk.Tk):
    # Create the register window
    window = tk.Toplevel()
    window.title("Registration")
    width = 256
    height = 256

    # window size and position
    window.geometry(f"{width}x{height}")

    # Create labels and entry fields for register form
    username_label = tk.Label(window, text='Username:')
    username_label.pack()
    username_input = tk.Entry(window)
    username_input.pack()

    password_label = tk.Label(window, text='Password:')
    password_label.pack()
    password_input = tk.Entry(window, show="*")
    password_input.pack()

    # Create register button
    register_button = tk.Button(window, text="Register", width=15, height=2, command=lambda: register(
        window, parentWindow, username_input.get(), password_input.get()))
    register_button.pack(pady=10)

    # Create back button
    tk.Button(window, text="Back", width=15, height=2,
              command=lambda: back(window, parentWindow)).pack(pady=10)

    # Start the register window event loop
    window.mainloop()


def register(window: tk.Tk, parentWindow: tk.Tk, username, password):

    # Validate if username and password are provided
    if not username or not password:
        messagebox.showerror('Error', 'Please enter a username and password')
        return

    # Check if username already exists in the CSV file
    with open(USERS_FILE, encoding="utf-8", mode="r") as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            if len(row) == 2 and row[0] == username:
                messagebox.showerror('Error', 'Username already exists')
                return

    # Save the new user to the CSV file
    with open(USERS_FILE, encoding="utf-8", mode="a", newline="") as csvfile:
        csv.writer(csvfile).writerow([username, password])

    messagebox.showinfo('Success', 'Registration successful')
    back(window, parentWindow)
