from tkinter import filedialog
import tkinter.messagebox as messagebox
import requests

class FileManager:
    @staticmethod
    def select_input_file():
        return filedialog.askopenfilename(filetypes=[('Text Files', '*.txt')], title="Select Input File")

    @staticmethod
    def save_output_file():
        return filedialog.asksaveasfilename(defaultextension=".apkg", filetypes=[('Anki Deck Files', '*.apkg')],
                                            title="Save Anki Deck")

def get_version_number():
    return "v0.1"  # Replace with your actual version number

def check_for_update():
    current_version = get_version_number()
    response = requests.get("https://api.github.com/repos/LRenTi/AnkiPackBuilder/releases/latest")
    latest_version = response.json()["tag_name"]

    if latest_version != current_version:
        messagebox.showinfo("Update Available", f"A new version ({latest_version}) of Anki Pack Builder is available. Please update to the latest version.")
