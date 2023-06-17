import tkinter as tk
from login_window import create_login_window
from register_window import create_register_window


def login(window: tk.Tk):
    # hide the main window
    window.withdraw()
    create_login_window(window)


def register(window: tk.Tk):
    window.withdraw()
    create_register_window(window)


def create_main_window():
    # Create the main window
    window = tk.Tk()
    window.title("Stock Market History App")
    width = 512
    height = 256

    # window size and position
    window.geometry(f"{width}x{height}")

    # Create welcome message label
    welcome_label = tk.Label(window, text="Welcome to the Stock App!")
    welcome_label.pack(pady=20)

    # Create instructions label
    instruction_label = tk.Label(
        window, text="To continue, please login or create an account")
    instruction_label.pack(pady=10)

    # Create login button
    login_button = tk.Button(window, text="Login", width=15,
                             height=2, command=lambda: login(window))
    login_button.pack(pady=10)

    # Create registration button
    registration_button = tk.Button(
        window, text="Register", width=15, height=2, command=lambda: register(window))
    registration_button.pack(pady=10)

    # Start the main window event loop
    window.mainloop()
