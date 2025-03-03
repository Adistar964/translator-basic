
# Translator Project

## Overview

This Translator application allows users to translate text from one language to another using Google Translate. It provides a user-friendly interface built with **Tkinter**, a Python library for creating graphical user interfaces (GUIs). The app also integrates with **pyperclip** for clipboard functionality, allowing users to copy and paste text effortlessly.

The project supports multiple languages and lets the user select a target language from a dropdown menu. Translated text can be easily copied back to the clipboard.

---

## Features

- **Text Translation:** Translate any input text to a selected language.
- **Clipboard Integration:** Paste copied text directly into the input field and copy translated text to the clipboard.
- **Language Selection:** Choose from a variety of languages for translation.
- **GUI Interface:** Built with Tkinter, offering an interactive and simple-to-use interface.

---

## Requirements

- Python 3.x
- **googletrans** library (for translation)
- **tkinter** library (for GUI)
- **pyperclip** library (for clipboard management)

You can install the required dependencies using pip:

```bash
pip install googletrans==4.0.0-rc1
pip install pyperclip
```

Note: Tkinter comes pre-installed with Python, so you don't need to install it separately.

---

## Project Structure

```
Translator/
│
├── main.py         # Main file containing the logic for translation and GUI
├── langs.py        # Language codes and names
├── requirements.txt # List of required libraries
├── README.md       # Project documentation
└── .gitignore          # to ignore unneccessary files
```

---

## How to Run

1. Clone the repository to your local machine:

   ```bash
   git clone https://github.com/Adistar964/translator-basic.git
   ```

2. Install the required libraries:

   ```bash
   pip install -r requirements.txt
   ```

3. Run the main Python file:

   ```bash
   python main.py
   ```

This will launch the Translator application with the GUI, where you can enter text, select a target language, and get your translation!

---

## How to Use

1. **Input Text:** Type or paste the text you want to translate in the input text box.
2. **Select Language:** Choose the language you want to translate to from the "Translate to" dropdown menu.
3. **Translate:** Click the "Translate" button to get the translated text.
4. **Copy Translated Text:** Use the "Copy Translated" button to copy the translated text to your clipboard.
5. **Clipboard Functions:** Right-click to paste or copy text directly from the input text box using the right-click context menu.

---

## Contributing

Feel free to fork the repository and submit pull requests for any improvements or bug fixes. Please ensure your code follows Python’s PEP 8 standards.

---

## Acknowledgements

- [Google Translate API](https://pypi.org/project/googletrans/)
- [Tkinter](https://wiki.python.org/moin/TkInter)
- [pyperclip](https://github.com/asweigart/pyperclip)

---

## Contact

Author: [Mohammed Abdullah Amaan](mailto:abdullah@abdullahamaan.com)