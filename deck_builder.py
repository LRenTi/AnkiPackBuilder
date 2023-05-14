import genanki
from anki_model import APBModel
from file_manager import FileManager

class DeckBuilder:
    def __init__(self, input_file_path, deck_name):
        self.input_file_path = input_file_path
        self.deck_name = deck_name

    def generate_anki_deck(self):
        # Read the questions and answers from the input file
        with open(self.input_file_path, 'r') as file:
            lines = file.readlines()

        # Create Anki deck
        deck = genanki.Deck(1234567890, self.deck_name)

        # Extract questions and answers from the lines
        question = ''
        answer = ''
        for line in lines:
            line = line.strip()

            # Skip empty lines
            if not line:
                continue

            # Check if it's a question
            if line.startswith("#"):
                # If previous question and answer exist, add them to the deck
                if question and answer:
                    my_note = genanki.Note(
                        model=APBModel.model,
                        fields=[question, answer.replace('\n', '<br>')]
                    )
                    deck.add_note(my_note)

                # Update the current question
                question = line.lstrip("#").strip()
                answer = ''
            else:
                # Append the line to the current answer
                answer += line + '\n'

        # If the last question and answer exist, add them to the deck
        if question and answer:
            my_note = genanki.Note(
                model=APBModel.model,
                fields=[question, answer.replace('\n', '<br>')]
            )
            deck.add_note(my_note)

        # Create Anki deck file
        output_file_path = FileManager.save_output_file()
        if output_file_path:
            # Generate Anki package
            genanki.Package(deck).write_to_file(output_file_path)
            print("Anki deck successfully generated!")
