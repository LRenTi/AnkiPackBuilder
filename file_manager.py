from tkinter import filedialog

class FileManager:
    @staticmethod
    def select_input_file():
        return filedialog.askopenfilename(filetypes=[('Text Files', '*.txt')], title="Select Input File")

    @staticmethod
    def save_output_file():
        return filedialog.asksaveasfilename(defaultextension=".apkg", filetypes=[('Anki Deck Files', '*.apkg')],
                                            title="Save Anki Deck")
