# AnkiPackBuilder       [![GitHub tag](https://img.shields.io/github/tag/LRenTi/AnkiPackBuilder?include_prereleases=&sort=semver)](https://github.com/LRenTi/AnkiPackBuilder/releases/) [![License](https://img.shields.io/badge/License-MIT-blue)](#license)


AnkiPackBuilder is a simple tool that allows you to easily create Anki decks from a text file. With AnkiPackBuilder, you can efficiently convert your collection of questions and answers into interactive flashcards for effective learning and revision.

## Features

- Create Anki decks from a text file with a specific format.
- Supports both single-line and multi-line answers.
- Customizable deck name for better organization.
- User-friendly GUI for easy interaction.

## How to build the .txt file

Make sure your input file follows the specified format:
- Each question starts with a '#' symbol, followed by the question text.
- The answer text immediately follows the question, starting from the next line.
- Questions and answers are separated by empty lines.

        #Question 1
        Answer 1
        Multiple lines possible

        #Question 2
        Answer 2
        Multiple lines possible
        
        .
        .
        .

    **or look into the example folder and look at the [.txt file](https://github.com/LRenTi/AnkiPackBuilder/blob/main/example/example.txt).**<br>
    
### ChatGPT
A prompt for ChatGPT to create Flashcards in the AnkiPackBuilder Format about the topic Bilirubin. <br>

	Create flashcards for me. The format you should use is as follows: Put a # before the question, followed immediately by the question itself. The answer should be written beneath the question and can span multiple lines. Everything should be in a .txt code file. You don't need to write "question" or "answer. 
        Here's an example card in the format you should follow:
        #What is the color of the sky?
        Blue
	
## Usage

1. Prepare a text file with your questions and answers in the specified format.

2. Run the APB.exe file.

3. Click the "Select File" button and choose the text file with your questions and answers.

4. Enter a deck name in the provided field.

5. Click the "Create Deck" button to generate the Anki deck.

6. Open Anki and import the generated .apkg file to start using your new deck.

## Contributing

Contributions are welcome! If you have any ideas, suggestions, or bug reports, please open an issue.

## Download

Windows: [Download](https://github.com/LRenTi/AnkiPackBuilder/releases/latest) `.zip`<br>
MacOS: [Download](https://github.com/LRenTi/AnkiPackBuilder/releases/latest) `.dmg`
## License

This project is released under [MIT](/LICENSE.md) by [@LRenTi](https://github.com/LRenTi). See the [LICENSE](LICENSE.md) file for more details.
