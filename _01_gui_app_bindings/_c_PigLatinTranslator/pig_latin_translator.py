"""
 Create an app that checks the user's typing skills
"""
import tkinter as tk
from PigLatinConverter import PigLatinConverter

class PigLatinTranslator(tk.Tk):
    def __init__(self):
        super().__init__()

        # TODO: Declare and initialize an Entry (tk.Entry) for the input text
        self.plain_text = tk.Entry()
        self.plain_text.place(relx=0, rely=0.2, relwidth=0.4, relheight=0.6)
        # TODO: Declare and initialize a Button (tk.Button) that will translate
        #  the input text to pig latin when pressed
        self.translate_button = tk.Button(text='Translate', bg='lime green')
        self.translate_button.place(relx=0.4, rely=0.2, relwidth=0.2, relheight=0.6)
        # TODO: Declare and initialize an label (tk.Label) for the translated
        #  text
        self.cipher_text = tk.Label(bg='white')
        self.cipher_text.place(relx=0.6, rely=0.2, relwidth=0.4, relheight=0.6)
        # TODO: Look at the example image () and place all the
        #  components in the same order

        # TODO: Call the label's bind() method to call the on_key_release()
        #  method when a key is released
        self.translate_button.bind("<ButtonPress>", self.on_key_press)


    def on_key_press(self, event):
        print('button pressed!')
        translated_text = PigLatinConverter.translate(str(self.plain_text.get()))
        self.cipher_text.configure(text=translated_text)

        # TODO: Use the _c_PigLatinTranslator.translate() method to translate
        #  the text in the input entry and set the text in the output entry


if __name__ == '__main__':
    translator = PigLatinTranslator()
    translator.title("Pig Latin Translator")
    translator.geometry("500x80")
    translator.mainloop()
    # TODO: Create a new _c_PigLatinTranslator object and set the title and geometry.
    #  Remember to call mainloop() at the end
