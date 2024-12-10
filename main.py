from questions import questions_list
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.properties import StringProperty, ListProperty, NumericProperty
from kivy.uix.screenmanager import ScreenManager, Screen, SlideTransition
from kivy.animation import Animation
from kivy.clock import Clock
import random

class QuizScreen(Screen):
    question_text = StringProperty()
    options = ListProperty()
    current_score = NumericProperty(0)
    total_questions = NumericProperty(0)
    time_left = NumericProperty(15)
    question_answered = False  
    
    def __init__(self, **kwargs):
        super(QuizScreen, self).__init__(**kwargs)
        self.questions = questions_list  # Use imported questions
        self.start_new_round()

    def start_new_round(self):
        self.current_questions = random.sample(self.questions, 5)
        self.current_question_index = 0
        self.round_score = 0
        self.load_question()

    def load_question(self):
        if self.current_question_index < len(self.current_questions):
            question = self.current_questions[self.current_question_index]
            self.question_text = question.question
            self.options = question.options
            self.time_left = 15
            self.start_timer()
        else:
            self.manager.current = 'result'
            self.manager.get_screen('result').update_score(self.round_score)

    def start_timer(self):
        Clock.schedule_interval(self.update_timer, 1)

    def update_timer(self, dt):
        self.time_left -= 1
        if self.time_left <= 0:
            self.check_answer(None)

    def check_answer(self, answer):
        Clock.unschedule(self.update_timer)
        question = self.current_questions[self.current_question_index]
        if answer == question.correct_answer:
            self.round_score += 1
            self.current_score += 1
            self.ids.feedback.text = "Correct!"
            self.ids.feedback.color = (0, 1, 0, 1)  # Green
        else:
            self.ids.feedback.text = f"Incorrect. The correct answer was: {question.correct_answer}"
            self.ids.feedback.color = (1, 0, 0, 1)  # Red
        self.total_questions += 1
        self.ids.next_button.disabled = False
        self.animate_feedback()

    def animate_feedback(self):
        anim = Animation(opacity=1, duration=0.5) + Animation(opacity=1, duration=1) + Animation(opacity=0, duration=0.5)
        anim.start(self.ids.feedback)

    def next_question(self):
        self.current_question_index += 1
        self.ids.feedback.text = ""
        self.ids.next_button.disabled = True
        self.load_question()

class ResultScreen(Screen):
    round_score = NumericProperty(0)
    total_score = NumericProperty(0)
    total_questions = NumericProperty(0)

    def update_score(self, round_score):
        self.round_score = round_score
        self.total_score = self.manager.get_screen('quiz').current_score
        self.total_questions = self.manager.get_screen('quiz').total_questions

    def start_new_round(self):
        self.manager.get_screen('quiz').start_new_round()
        self.manager.transition = SlideTransition(direction='right')
        self.manager.current = 'quiz'

class dectquiz(App):
    def build(self):
        sm = ScreenManager(transition=SlideTransition())
        sm.add_widget(QuizScreen(name='quiz'))
        sm.add_widget(ResultScreen(name='result'))
        return sm

if __name__ == '__main__':
    dectquiz().run()