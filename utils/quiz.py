# coding=utf-8

import random
from utils.texts import Text


class Reply:
    def __init__(self, text, is_correct=False):
        self.is_correct = is_correct
        self.text = text


class Question:
    def __init__(self, question, replies):
        self.question = question
        self.replies = random.sample(replies, replies.__len__())


class Quiz:
    def __init__(self):
        self.current = -1
        self.questions = self.shuffle_questions()

    def next_question(self):
        self.current += 1
        if (self.current < self.questions.__len__()):
            return self.questions[self.current]

    def shuffle_questions(self):
        q1 = Question(question=Text(fr="Question 1", de="Frage 1"),
                      replies={Reply(Text(fr="Réponse 1A", de="Antwort 1A"), is_correct=True),
                               Reply(Text(fr="Réponse 1B", de="Antwort 1B"), is_correct=False),
                               Reply(Text(fr="Réponse 1C", de="Antwort 1C"), is_correct=False)})
        q2 = Question(question=Text(fr="Question 2", de="Frage 2"),
                      replies={Reply(Text(fr="Réponse 2A", de="Antwort 2A"), is_correct=False),
                               Reply(Text(fr="Réponse 2B", de="Antwort 2B"), is_correct=False),
                               Reply(Text(fr="Réponse 2C", de="Antwort 2C"), is_correct=True)})
        q3 = Question(question=Text(fr="Question 3", de="Frage 3"),
                      replies={Reply(Text(fr="Réponse 3A", de="Antwort 3A"), is_correct=False),
                               Reply(Text(fr="Réponse 3B", de="Antwort 3B"), is_correct=True)})
        questions = {q1, q2, q3}
        selection = questions.__len__()
        return random.sample(questions, selection)
