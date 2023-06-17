import tkinter as tk
import csv
from tkinter import messagebox
from after_login_window import create_after_login_window
from back import back

from const import USERS_FILE


def create_login_window(parentWindow: tk.Tk):
    # Create the login window
    window = tk.Toplevel()
    window.title('Login')
    width = 256
    height = 256

    # window size and position
    window.geometry(f"{width}x{height}")

    # Create labels and entry fields for login form
    username_label = tk.Label(window, text='Username:')
    username_label.pack()
    username_input = tk.Entry(window)
    username_input.pack()

    password_label = tk.Label(window, text='Password:')
    password_label.pack()
    password_input = tk.Entry(window, show="*")
    password_input.pack()

    # Create login button
    login_button = tk.Button(window, text="Login", width=15, height=2, command=lambda: login(
        window, parentWindow, username_input.get(), password_input.get()))
    login_button.pack(pady=10)

    # Create back button
    tk.Button(window, text="Back", width=15, height=2,
              command=lambda: back(window, parentWindow)).pack(pady=10)

    # Start the login window event loop
    window.mainloop()


def login(window: tk.Tk, parentWindow: tk.Tk, username, password):
    # Validate if username and password are provided
    if not username or not password:
        messagebox.showerror('Error', 'Please enter a username and password')
        return

    # Check if username and password match the ones in the CSV file
    with open(USERS_FILE, encoding="utf-8") as csvfile:
        reader = csv.reader(csvfile)

        next(reader)  # Skip the header row

        for row in reader:
            if len(row) == 2 and row[0] == username and row[1] == password:
                messagebox.showinfo('Success', 'Login successful')
                window.withdraw()
                # Call a function to proceed to the next step
                create_after_login_window(parentWindow)
                return

    messagebox.showerror('Error', 'Invalid username or password')
