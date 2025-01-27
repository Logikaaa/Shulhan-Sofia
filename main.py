from random import choice, shuffle
from time import sleep
from PyQt5.QtWidgets import QApplication

app = QApplication([])

from main_window import *


class Question:
    def __init__(self, question, answer, wrong_answer1, wrong_answer2, wrong_answer3):
        self.question = question
        self.answer = answer
        self.wrong_answer1 = wrong_answer1
        self.wrong_answer2 = wrong_answer2
        self.wrong_answer3 = wrong_answer3
        self.isAsking = True
        self.count_ask = 0
        self.count_right = 0
    def got_right(self):
        self.count_ask += 1
        self.count_right += 1
    def got_wrong(self):
        self.count_ask += 1

q1 = Question('У якому році Україна стала незалежною?', '1991', '1990', '1989', '1992')
q2 = Question('Яка планета найблища до сонця?', 'Венера', 'Земля', 'Марс', 'Меркурій')
q3 = Question('Яка пташка не вміє літати?', 'Пінгвін', 'Орел', 'Лебідь', 'Синиця')
q4 = Question('Який танець родом з аргентини?', 'Танго', 'Сальса', 'Вальс', 'Фламенко')
q5 = Question('Яка тварина вміє змінювати колір шкіри?', 'Хамелеон', 'Восьменіг', 'Лев', 'Жирафа')
q6= Question('Як називається дитинча коня?', 'Лоша', 'Восьменіг', 'Кобила', 'Теля')




radio_buttons = [rb_ans1, rb_ans2, rb_ans3, rb_ans4]
questions = [q1, q2, q3, q4, q5, q6]

def new_question():
    global cur_q
    cur_q = choice(questions)
    lb_question.setText(cur_q.question)
    lb_right_answer.setText(cur_q.answer)
    shuffle(radio_buttons)

    radio_buttons[0].setText(cur_q.wrong_answer1)
    radio_buttons[1].setText(cur_q.wrong_answer2)
    radio_buttons[2].setText(cur_q.wrong_answer3)
    radio_buttons[3].setText(cur_q.answer)

new_question()

def check():
    RadioGroup.setExclusive(False)
    for answer in radio_buttons:
        if answer.isChecked():
            if answer.text() == lb_right_answer.text():
                cur_q.got_right()
                lb_result.setText('Вірно!')
                answer.setChecked(False)
                break
    else:
        lb_result.setText('Не вірно!')
        cur_q.got_wrong()

    RadioGroup.setExclusive(True)

def click_ok():
    if btn_next.text() == 'Відповісти':
        check()
        gb_question.hide()
        gb_answer.show()

        btn_next.setText('Наступне запитання')
    else:
        new_question()
        gb_question.show()
        gb_answer.hide()

        btn_next.setText('Відповісти')

btn_next.clicked.connect(click_ok)

def rest():
    window.hide()
    n = sp_rest.value() 
    sleep(n)
    window.show()

btn_rest.clicked.connect(rest)









window.show()
app.exec_()