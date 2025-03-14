# SymboLang - Convert Text into Symbols

SymboLang is a Python GUI application that converts English text into a custom-defined symbolic language. It also allows users to decode the symbols back into readable text. This project adds an extra layer of security for text representation, making it harder for others to interpret at a glance.

## Features
- Convert English text into a custom symbol-based language.
- Decode the symbol language back to English.
- Copy the converted text to the clipboard.
- Simple and intuitive GUI built with Tkinter.

## Screenshots
![SymboLang UI](https://github.com/Aman-toad/SymboLang/blob/main/Screenshot%202025-03-15%20011850.png?raw=true)

## Installation
### Prerequisites
Ensure you have Python installed on your system.

### Steps
1. Clone the repository:
   ```sh
   git clone https://github.com/Aman-toad/SymboLang.git
   ```
2. Navigate to the project directory:
   ```sh
   cd SymboLang
   ```
3. Install the required dependencies:
   ```sh
   pip install -r requirements.txt
   ```
4. Run the application:
   ```sh
   python symboLang.py
   ```

## Usage
1. Enter text in the input box.
2. Click **Convert to Secret Text** to transform the text into symbols.
3. Click **Convert to Normal Text** to decode the symbols back to English.
4. Click **Copy Secret Text** to copy the converted text to the clipboard.

## Customization
Modify the `custom_mapping` dictionary inside the code to define your own symbol mappings.

## Future Enhancements
- Store `custom_mapping` securely using environment variables.
- Implement stronger encryption for added security.
- Export the converted text as an image or file.

## Contributing
Feel free to fork this repository and submit pull requests with improvements!

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Author
Developed by [Aman Singh](https://github.com/Aman-toad)

