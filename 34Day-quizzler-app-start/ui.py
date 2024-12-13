
import tkinter
# import quiz_brain
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"

class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain

        self.window = tkinter.Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, background=THEME_COLOR)
        #Label
        self.score_label = tkinter.Label(text="Score: 0", fg="white", bg=THEME_COLOR)
        self.score_label.grid(row=0, column=1)
        # canvas
        self.canvas = tkinter.Canvas(width=300, height=250, bg="white")
        self.question_text = self.canvas.create_text(
            150, 125, text="question Goes HERE", font=("Arial", 20, "italic"), fill="black",
            width=280, # needed to fit the get_next_question() in canvas
        )
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)
        # buttons
        true_image = tkinter.PhotoImage(file="images/true.png") # not using self here as we don't need that anywhere outside class
                                                                    # - just to set up button
        self.true_button = tkinter.Button(image=true_image, highlightthickness=0, command=self.true_button_pressed)
        self.true_button.grid(row=2, column=0)

        false_image = tkinter.PhotoImage(file="images/false.png") # not using self here as we don't need that anywhere outside class
                                                                    # - just to set up button
        self.false_button = tkinter.Button(image=false_image, highlightthickness=0, command=self.false_button_pressed)
        self.false_button.grid(row=2, column=1)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")  # reset to white after give_feedback()
        if self.quiz.still_has_questions():
            self.score_label.config(text=f"Score: {self.quiz.score}")
            """Takes QuizBrain method next question and updates canvas text with the next_question()"""
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text="You've reached the end of the quiz.")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")

    def true_button_pressed(self):
        is_right = self.quiz.check_answer("True")
        self.give_feedback(is_right)

    def false_button_pressed(self):
        is_right = self.quiz.check_answer("False")
        self.give_feedback(is_right)

    def give_feedback(self, is_right):
        if not is_right:
            self.canvas.config(bg="red")
        else:
            self.canvas.config(bg="green")
        self.window.after(2000, self.get_next_question)
