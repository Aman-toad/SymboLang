from tkinter import *
from tkinter import scrolledtext, messagebox

root = Tk()
root.title("SymboLang")
root.geometry("700x700")

# Define your custom mapping here
custom_mapping = {
  "a": "α", "b": "Ѡ", "c": "Ѥ", "d": "ї",
  "e": "಄", "f": "ϝ", "g": "Ϟ", "h": "ǂ",
  "i": "ι", "j": "֏", "k": "❮", "l": "ר",
  "m": "Ѫ", "n": "ѱ", "o": "ѳ", "p": "ʔ",
  "q": "ʕ", "r": "ܛ", "s": "ܟ", "t": "Ե",
  "u": "σ", "v": "۸", "w": "Ӟ", "x": "★",
  "y": "ח", "z": "ƻ",
  " ": "┄"
}

reverse_custom_mapping = {}

for key, value in custom_mapping.items():
  reverse_custom_mapping[value] = key # reversed the custom mapping

def translate_text():
  result = ""
  userText = inputText.get('1.0', END).strip(' ')

  for char in userText:
    if char in custom_mapping:
      result += custom_mapping[char]
      result_reversed = result[::-1]

  displayText.insert(END, result_reversed)
  inputText.delete('1.0', END)

def normalizing_text():
  result = ""
  userText = inputText.get('1.0', END).strip(' ')

  for char in userText:
    if char in reverse_custom_mapping:
      result += reverse_custom_mapping[char]
      reverse_result = result[::-1]

  displayText.insert(END, reverse_result)
  inputText.delete('1.0', END)

def copySecretText():
  root.clipboard_clear()
  root.clipboard_append(displayText.get('1.0', END))
  root.update()
  messagebox.showinfo('Info', "Secret text copied")

  # text = displayText.get('1.0', END)

  # for char in text:
    # if char in custom_mapping:
    #   root.clipboard_clear()
    #   root.clipboard_append(displayText.get('1.0', END))
    #   root.update()
    #   messagebox.showinfo('Info', "Secret text copied")
    # else:
    #   messagebox.showinfo('Info', "No Secret text")

AppHeader = Label(root, text='My SymbolLang', bg='green', fg='white', font=('Georgia', 24))
AppHeader.pack(fill=X, expand=True)

englishText = Label(root, text='Write Secret Text or Normal Text:')
englishText.pack(anchor=W, padx=10)

inputText = scrolledtext.ScrolledText(root, wrap=WORD, height=10, font=('Georgia', 15))
inputText.pack(fill=BOTH, expand=True, padx=10)

button_frame = Frame(root)
button_frame.pack(pady=10)

convertBtn1 = Button(button_frame, text='Convert to Secret text', command=translate_text, width=20, bg='Sky Blue', font=('Georgia', 12), relief=RAISED, bd=5)
convertBtn1.grid(row=0, column=0, padx=10)

convertBtn2 = Button(button_frame, text='Convert to Normal text', command=normalizing_text, width=20, bg='Yellow', font=('Georgia', 12), relief=RAISED, bd=5)
convertBtn2.grid(row=0, column=1, padx=10)

copyBtn = Button(button_frame, text='Copy Secret Text', command=copySecretText, width=20, bg='Light Green', font=('Georgia', 12), relief=RAISED, bd=5)
copyBtn.grid(row=0, column=2, padx=10)

symbolText = Label(root, text='Your Converted Text:')
symbolText.pack(anchor=W, padx=10)

displayText = scrolledtext.ScrolledText(root, wrap=WORD, height=10, font=('Georgia', 15))
displayText.pack(fill=BOTH, expand=True, padx=10)

root.mainloop()
