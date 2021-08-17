"""
 Create a _e_Jeopardy trivia game!
"""
import random
import tkinter as tk
from tkinter import messagebox, simpledialog, Tk


class Jeopardy(tk.Tk):

    def __init__(self, categories):
        super().__init__()

        button_width, button_height, num_buttons = self.setup_buttons(categories)

        # TODO: Create a member variable for the list of categories
        self.categories = categories
        # TODO: Create a member variable for the score/money
        self.score = 0
        for i in range(num_buttons):
            row_num = int(i / len(categories))
            col_num = int(i % len(categories))
            row_y = row_num * button_height
            col_x = col_num * button_width
            category = self.categories[col_num]

            # Create the category header and buttons where
            # row 0 is the category title
            if row_num == 0:
                # TODO: To get the category name, use the categories member variable and column num
                label = tk.Label(text=self.categories[col_num].name, font=("times new roman", 20))
                label.place(x=col_x, y=row_y, width=button_width, height=button_height)
                # TODO: Place the Label using the 'col_x', 'row_y', 'button_width',
                #  and 'button_height' variables

            elif len(category.questions) > row_num - 1:
                value = category.questions[row_num - 1].value
                button = tk.Button(text=str(value), font=("times new roman", 30))
                # TODO: Create a tk.Button with the questions' value on the button

                # TODO: Place the Button using the 'col_x', 'row_y', 'button_width',
                #  and 'button_height' variables
                button.place(x=col_x, y=row_y, width=button_width, height=button_height)
                # TODO: Call the button's bind() method so the
                #  on_button_press() method is called when a mouse button is pressed
                #  example: self.joke_button.bind('<ButtonPress>', self.on_button_press)
                button.bind('<ButtonPress>', self.on_button_press)
                # TODO: Add the button to the category's list of buttons
                category.buttons.append(button)


    def on_button_press(self, event):
        button_pressed = event.widget
        print('button ' + repr(button_pressed) + ' clicked!')

        # TODO: Call the ask_question() method with button_pressed as an input
        self.ask_question(button_pressed)

    def ask_question(self, button_pressed):
        for category in self.categories:
            for i, button in enumerate(category.buttons):
                if button == button_pressed:
                    if category.questions[i].has_been_asked is False:
                        category.questions[i].has_been_asked = True
                        question = category.questions[i].question
                        answer = category.questions[i].answer
                        value = category.questions[i].value

                        # TODO: At this point the question corresponding to the button is found
                        #  Use the 'question', 'answer', and 'value' variables to ask the user
                        #  the question and get their response. If their response is correct,
                        #  increase the score member variable by the value. Otherwise, subtract
                        #  value from the score
                        user_answer = simpledialog.askstring(None, prompt=question)
                        if user_answer.lower() == answer:
                            self.score+=value
                            messagebox.showinfo(message="Correct! Your score is now " + str(self.score) + "!")
                        else:
                            self.score -= value
                            messagebox.showinfo(message="That is not the correct answer! The correct answer is " + answer + "!" + " Your score is now " + str(self.score) + ".")



    def setup_buttons(self, categories):
        # Window size needs to be updated immediately here so the
        # window width/height variables can be used below
        self.geometry('800x600')
        self.update_idletasks()

        # Get category with the max num of questions to determine the
        # total number of buttons to create
        questions_per_category = 0
        for category in categories:
            if len(category.questions) > questions_per_category:
                questions_per_category = len(category.questions)

        # +1 for the category title
        num_rows = questions_per_category + 1
        num_buttons = len(categories) * num_rows

        button_width = int(self.winfo_width() / len(categories))
        button_height = int(self.winfo_height() / num_rows)

        return button_width, button_height, num_buttons


class Category:
    def __init__(self, category_name):
        self.name = category_name
        self.questions = list()
        self.buttons = list()

    def add_question(self, question, answer, value):
        new_question = Category.Question(question, answer, value)
        self.questions.append(new_question)

    class Question:
        def __init__(self, question, answer, value):
            self.has_been_asked = False
            self.question = question
            self.answer = answer
            self.value = value


if __name__ == '__main__':
    j_categories = list()

    # TODO: Use the Category class above to create at least 3 question categories
    #  for your _e_Jeopardy game
    j_categories.append(Category("Books"))
    j_categories.append(Category("Music"))
    j_categories.append(Category("Math"))
    # TODO: For each Category, use the add_question method to add a question, answer, and
    #  a value for each question
    j_categories[0].add_question("What do you call the person who wrote a book?", "author", 10)
    j_categories[0].add_question("Do books typically start on the right or the left page? (answer right or left)", "right", 20)
    j_categories[0].add_question("Who wrote the Percy Jackson series?", "rick riordan", 30)
    j_categories[1].add_question("What do you call the different sounds that make up music?", "notes", 10)
    j_categories[1].add_question("If there is a note that is a circle with the inside unfilled and no line, what is it called?", "whole note", 20)
    j_categories[1].add_question("What do you call the spots in music where you don't play?", "rests", 30)
    j_categories[2].add_question("If x is three less than half of z, and z is 10, what is x?", "2", 10)
    j_categories[2].add_question("What is the square root of 256?", "16", 20)
    j_categories[2].add_question("i is the imaginary number. What is i*i?", "-1", 30)

    game = Jeopardy(j_categories)
    game.title('_e_Jeopardy')
    game.mainloop()
