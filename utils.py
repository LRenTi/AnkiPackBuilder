from tkinter import filedialog
import tkinter as tk
import tkinter.messagebox as messagebox
import requests
from tkinter import messagebox, Tk, Label, Button
import webbrowser

def get_version_number():
    return "v1.0"  # Replace with your actual version number

def check_for_update():
    current_version = get_version_number()
    response = requests.get("https://api.github.com/repos/LRenTi/AnkiPackBuilder/releases/latest")
    latest_version = response.json()["tag_name"]

    if latest_version != current_version:
        root = Tk()
        root.title("Update Available")
        root.geometry("300x120")
        root.resizable(False, False)
        root.configure(bg="#202020")

        message_label = Label(root, text=f"A new version ({latest_version}) of Anki Pack Builder is available.\n Please update to the latest version.", font=("Helvetica", 9), bg="#202020", fg="white")
        message_label.pack(pady=10)

        download_button = Button(root, text="Download", command=lambda: open_link("https://github.com/LRenTi/AnkiPackBuilder/releases/latest"))
        download_button.pack(pady=10)

        root.mainloop()

def open_link(url):
    webbrowser.open(url)
    pass
