from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"




class QuizInterface:
    def next_question(self):
        self.canvas.config(bg='white')
        if self.quiz.still_has_questions():
            self.score_text.config(text = f'Score : {self.quiz.score}')
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text = q_text)
        else:
            self.canvas.itemconfig(self.question_text, text ="You've reached the end of the quiz.")
            self.true_button.config(state='disabled')
            self.false_button.config(state='disabled')

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg='green')
        else:
            self.canvas.config(bg='red')
        self.window.after(1000, self.next_question)
 
        
    def answer_true(self):
        self.give_feedback(self.quiz.check_answer('True'))

    def answer_false(self):
        self.give_feedback(self.quiz.check_answer('False'))

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title('Quizzler')
        self.window.config(padx=20,pady=20, bg=THEME_COLOR)
        self.score_text = Label(text='Score: 0', fg= 'white', bg=THEME_COLOR)
        self.score_text.grid(column = 1, row = 0)

        self.canvas = Canvas(width=300, height=250, bg='white', highlightthickness=0)    
        self.canvas.grid(column=0,row=1,columnspan=2, pady=50)
        self.question_text = self.canvas.create_text(
            150,125, 
            width=280,
            text='Sample question', 
            fill=THEME_COLOR, 
            font=('Arial', 20, 'italic'))

        true_image = PhotoImage(file='images/true.png')
        self.true_button = Button(image=true_image, highlightthickness=0, command=self.answer_true)
        self.true_button.grid(column=0,row=2)
        false_image = PhotoImage(file='images/false.png')
        self.false_button = Button(image=false_image, highlightthickness=0, command=self.answer_false)
        self.false_button.grid(column=1,row=2)
        
        self.next_question()

        self.window.mainloop()