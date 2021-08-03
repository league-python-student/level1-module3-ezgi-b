"""
 Create an app that tells a joke, then a punchline
"""
import tkinter as tk
import random
from tkinter import messagebox


# Use this function to return a random character
def generate_random_letter():
    return chr(random.randint(0, 25) + ord('a'))


class ChuckleClicker(tk.Tk):
    def __init__(self):
        super().__init__()

        # TODO: Declare and initialize 2 buttons (tk.Button)
        #  one button for the joke and another for the punchline
        self.joke_button = tk.Button(text = "Joke")
        self.punchline_button = tk.Button(text="Punchline")
        # TODO: Place the 2 buttons next to each other (see example image)
        self.joke_button.place(relx=0, rely=0, relwidth=0.5, relheight=1)
        self.punchline_button.place(relx=0.5, rely=0, relwidth=0.5, relheight=1)
        # TODO: Call the joke button's bind() method to call the on_joke()
        #  method when a mouse button is pressed
        #  example: self.joke_button.bind('<ButtonPress>', self.on_joke)
        self.joke_button.bind('<ButtonPress>', self.on_joke)

        # TODO: Call the joke button's bind() method to call the on_punchline()
        #  method when a mouse button is pressed
        self.punchline_button.bind('<ButtonPress>', self.on_punchline)

    def on_joke(self, event):
        print('Joke button pressed')
        messagebox.showinfo(message="What did one Frenchman say to the other?")

        # TODO: Write your joke below!

    def on_punchline(self, event):
        print('Punchline button pressed')
        messagebox.showinfo(message="I don't know - I don't speak French.")
        # TODO: Write a punchline to your joke!


if __name__ == '__main__':
    pass
    # TODO: Create a new ChuckleClicker object and set the title and geometry.
    #  Remember to call mainloop() at the end
    c = ChuckleClicker()
    c.mainloop()

