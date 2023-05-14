import tkinter as tk
from tkinter import filedialog
from deck_builder import DeckBuilder
from utils import get_version_number

class AnkiPackBuilderGUI:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Anki Pack Builder")
        self.window.geometry("400x200")

        version_label = tk.Label(self.window, text="Version: " + get_version_number())
        version_label.place(x=10, y=180)

        developer_label = tk.Label(self.window, text="by LRenTi")
        developer_label.place(x=310, y=180)

        self.input_file_path = None
        self.deck_name = None

        self.input_file_label = tk.Label(self.window, text="Input File:")
        self.input_file_label.pack()

        self.input_file_button = tk.Button(self.window, text="Select Input File", command=self.select_input_file)
        self.input_file_button.pack()

        self.deck_name_label = tk.Label(self.window, text="Deck Name:")
        self.deck_name_label.pack()

        self.deck_name_entry = tk.Entry(self.window)
        self.deck_name_entry.pack()

        self.generate_button = tk.Button(self.window, text="Generate Anki Deck", command=self.generate_anki_deck)
        self.generate_button.pack()

        self.success_label = tk.Label(self.window, text="")
        self.success_label.pack()

    def select_input_file(self):
        self.input_file_path = filedialog.askopenfilename(filetypes=[('Text Files', '*.txt')], title="Select Input File")
        self.input_file_label.config(text=f"Input File: {self.get_file_name(self.input_file_path)}")

    def get_file_name(self, file_path):
        if file_path:
            return file_path.split("/")[-1]
        return ""

    def generate_anki_deck(self):
        self.deck_name = self.deck_name_entry.get()
        DeckBuilder(self.input_file_path, self.deck_name).generate_anki_deck()
        self.success_label.config(text="Anki deck successfully generated!")

    def start(self):
        self.window.mainloop()
