import webbrowser  # Add this import at the top of the file
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.properties import StringProperty, ListProperty, NumericProperty, DictProperty
from kivy.uix.screenmanager import ScreenManager, Screen, SlideTransition
from kivy.animation import Animation
from kivy.clock import Clock
import random
import sqlite3 
from collections import Counter

conn = sqlite3.connect('quiz_questions.db')
cursor = conn.cursor()

# Create a table for questions
cursor.execute('''
CREATE TABLE IF NOT EXISTS questions (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    question TEXT NOT NULL,
    options TEXT NOT NULL,
    correct_answer TEXT NOT NULL,
    subject TEXT NOT NULL
)
''')

class Question:
    def __init__(self, question, options, correct_answer, subject):
        self.question = question
        self.options = options
        self.correct_answer = correct_answer
        self.subject = subject



class HomeScreen(Screen):
    pass

class StartQuizScreen(Screen):
    pass

class AboutScreen(Screen):
    subject_counts = DictProperty()
    total_questions = NumericProperty()

    def on_pre_enter(self):
        self.update_subject_counts()

    def update_subject_counts(self):
        conn = sqlite3.connect('quiz_questions.db')
        cursor = conn.cursor()
        
        # Get total question count
        cursor.execute('SELECT COUNT(*) FROM questions')
        self.total_questions = cursor.fetchone()[0]

        # Get subject counts
        cursor.execute('SELECT subject, COUNT(*) FROM questions GROUP BY subject')
        rows = cursor.fetchall()
        conn.close()

        # Update subject_counts dictionary
        self.subject_counts = {row[0]: row[1] for row in rows}

        # Clear existing widgets and add new ones
        self.ids.subject_counts_box.clear_widgets()
        for subject, count in self.subject_counts.items():
            self.ids.subject_counts_box.add_widget(
                Label(
                    text=f'{subject}: {count}',
                    font_size='16sp',
                    color=(0.4, 0.4, 0.4, 1),
                    size_hint_y=None,
                    height='30dp',
                    halign='left',
                    valign='middle'
                )
            )

    def open_github_link(self):
        webbrowser.open('https://github.com/vaibhav-rm/Dcet-prep-app')


class QuizScreen(Screen):
    question_text = StringProperty()
    options = ListProperty()
    current_score = NumericProperty(0)
    total_questions = NumericProperty(0)
    time_left = NumericProperty(15)
    question_answered = False  
    
    def __init__(self, **kwargs):
        super(QuizScreen, self).__init__(**kwargs)
        self.questions = self.load_questions_from_db()  # Load questions from the database
        self.start_new_round()

    def load_questions_from_db(self):
        conn = sqlite3.connect('quiz_questions.db')
        cursor = conn.cursor()
        cursor.execute('SELECT question, options, correct_answer, subject FROM questions')
        rows = cursor.fetchall()
        conn.close()
        
        # Convert rows to Question objects
        return [Question(question=row[0], options=row[1].split(','), correct_answer=row[2], subject=row[3]) for row in rows]

    def start_new_round(self):
        self.current_questions = random.sample(self.questions, 5)
        self.current_question_index = 0
        self.round_score = 0
        self.load_question()  # Call load_question to display the first question

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
            self.ids.feedback.color = (0, 1, 0, 1)
        else:
            self.ids.feedback.text = f"Incorrect. The correct answer was: {question.correct_answer}"
            self.ids.feedback.color = (1, 0, 0, 1)
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
        self.load_question()  # Call load_question to load the next question

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
        sm.add_widget(HomeScreen(name='home'))
        sm.add_widget(StartQuizScreen(name='start_quiz'))
        sm.add_widget(AboutScreen(name='about'))
        sm.add_widget(QuizScreen(name='quiz'))
        sm.add_widget(ResultScreen(name='result'))
        return sm

if __name__ == '__main__':
    dectquiz().run()

conn.commit()
conn.close()
