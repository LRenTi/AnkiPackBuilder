import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
from deck_builder import DeckBuilder
from utils import get_version_number
import webbrowser

class AnkiPackBuilderGUI:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Anki Pack Builder")
        self.window.geometry("350x200")
        self.window.resizable(False, False)
        self.window.configure(bg="#202020")

        self.version_label = tk.Label(self.window, text="Version: " + get_version_number(), bg="#202020", fg="white")
        self.version_label.place(x=10, y=180)

        self.developer_label = tk.Label(self.window, text="by LRenTi", bg="#202020", fg="white")
        self.developer_label.place(x=290, y=180)

        self.input_file_path = None
        self.deck_name = None

        self.deck_name_label = tk.Label(self.window, text="Deck Name:", font=("Helvetica", 12, "bold"), bg="#202020", fg="white")
        self.deck_name_label.place(x=10, y=20)

        self.deck_name_entry = tk.Entry(self.window)
        self.deck_name_entry.place(x=125, y=25)

        self.input_file_label = tk.Label(self.window, text="Input File:", font=("Helvetica", 12, "bold"), bg="#202020", fg="white")
        self.input_file_label.place(x=10, y=70)

        self.input_file_button = tk.Button(self.window, text="Select Input File", command=self.select_input_file, bg="#3498db", fg="white", relief="flat", padx=10, borderwidth=0, cursor="hand2")
        self.input_file_button.place(x=125, y=70)

        self.selected_file_label = tk.Label(self.window, text="", font=("Helvetica", 8), bg="#202020", fg="white")
        self.selected_file_label.place(x=240, y=72)

        self.generate_button = tk.Button(self.window, text="Create Anki Deck", command=self.generate_anki_deck, bg="#3498db", fg="white", relief="flat", padx=10, pady=5, borderwidth=0, cursor="hand2")
        self.generate_button.place(x=10, y=125)

        self.help_button = tk.Button(self.window, text="?", command=self.open_help, font=("Helvetica", 9, "bold"), bg="#202020", fg="white", relief="flat", width=2, cursor="hand2")
        self.help_button.place(x=320, y=10)

        self.success_label = tk.Label(self.window, text="",bg="#202020", fg="white")
        self.success_label.pack()
        self.success_label.place(x=135, y=130)

    def select_input_file(self):
        self.input_file_path = filedialog.askopenfilename(filetypes=[('Text Files', '*.txt')], title="Select Input File")
        self.selected_file_label.config(text=self.get_file_name(self.input_file_path))

    def get_file_name(self, file_path):
        if file_path:
            return file_path.split("/")[-1]
        return ""

    def generate_anki_deck(self):
        self.deck_name = self.deck_name_entry.get()
        if self.deck_name and self.input_file_path:
            DeckBuilder(self.input_file_path, self.deck_name).generate_anki_deck()
            self.success_label.config(text="Anki deck successfully generated!")

    def open_help(self):
        webbrowser.open("https://github.com/LRenTi/AnkiPackBuilder/")

    def start(self):
        self.window.mainloop()