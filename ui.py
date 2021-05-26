from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"

class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain

        self.score = 0
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(width=400, height=550, padx=20, pady=20, bg=THEME_COLOR)

        self.score_label = Label(text=f"Score: {self.score} ", fg="white",
                                 bg=THEME_COLOR, highlightthickness=0, font=("Arial", 13))
        self.score_label.place(x=280, y=0)

        self.canvas = Canvas(width=300, height=300, highlightthickness=0, bg="white")
        self.canvas.place(x=30, y=50)
        self.question = QuizBrain.next_question
        self.question_text = self.canvas.create_text(150,
                                                     125,
                                                     width=280,
                                                     fill="black",
                                                     text="Some Question",
                                                     font=("Arial", 18, "italic"))

        true_image = PhotoImage(file="images/true.png")
        self.true_button = Button(image=true_image, command=self.true_func, highlightthickness=0)
        self.true_button.place(x=50, y=380)

        false_image = PhotoImage(file="images/false.png")
        self.false_button = Button(image=false_image, command=self.false_func, highlightthickness=0)
        self.false_button.place(x=200, y=380)

        self.get_next_question()
        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.score_label.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.score_label.config(text="")
            self.canvas.itemconfig(self.question_text,
                                   text=f"You've reach the end of the quiz. \n\n\n\nYour score is: {self.quiz.score}")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")

    def true_func(self):
        is_right = self.quiz.check_answer("True")
        self.give_feedback(is_right)

    def false_func(self):
        self.give_feedback(self.quiz.check_answer("False"))

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")

        self.window.after(1000, self.get_next_question)

