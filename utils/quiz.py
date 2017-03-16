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
        self.shuffle_questions()

    def next_question(self):
        self.current += 1
        if (self.current < self.questions.__len__()):
            return self.questions[self.current]

    def shuffle_questions(self):
        q1 = Question(question=Text(fr="Combien de mammifères meurent chaque année sur les routes suisses suite à une collision avec une voiture?", de="Wie viele Säugetiere sterben jährlich auf den schweizer Strassen in Folge von Autounfällen ?"),
                      replies={Reply(Text(fr="20’000", de="20’000"), is_correct=True),
                               Reply(Text(fr="100’000", de="100’000"), is_correct=False),
                               Reply(Text(fr="4’000", de="4’000"), is_correct=False)})
        q2 = Question(question=Text(fr="Quel est le problème de l’isolation des populations ?", de="Welches Problem entsteht, wenn Populationen isoliert werden ?"),
                      replies={Reply(Text(fr="les animaux ne trouvent plus de quoi se nourrir", de="die Tiere finden keine Nahrung mehr"), is_correct=False),
                               Reply(Text(fr="les animaux n’échangent plus assez de gènes", de="es findet zu wenig genetischer Austausch statt"), is_correct=True),
                               Reply(Text(fr="les animaux ne trouvent plus assez d’endroits chauds pour passer l’hiver", de="die Tiere finden keine Plätze mehr, um zu überwintern"), is_correct=False)})
        q3 = Question(question=Text(fr="Qu’est-ce qu’un corridor noir ?", de="Was ist ein « Schwarzkorridor » ?"),
                      replies={Reply(Text(fr="des espaces sans lumière artificielle  pour les animaux nocturnes", de="ein Ort ohne Kunstlicht für nachtaktive Tiere"), is_correct=True),
                               Reply(Text(fr="un tunnel sombre sous la route pour le passage des animaux", de="ein dunkler Tunnel für die Tiere, der unter einer Strasse hindurchführt"), is_correct=False),
                               Reply(Text(fr="un passage sous-terrain pour le déplacement des insectes", de="ein unterirdischer Durchgang, der speziell für Insekten gebaut wird"), is_correct=False)})
        q4 = Question(question=Text(fr="Les algues produites par les engrais nuisent aux poissons, car…", de="Durch Dünger entstandene Algen schaden den Fischen, weil…"),
                      replies={Reply(Text(fr="…elles diminuent la quantité d’oxygène dans l’eau, ce qui les empêche de respirer", de="…sie den Sauerstoffgehalt im Wasser reduzieren und dadurch die Fische am atmen hindern"), is_correct=True),
                               Reply(Text(fr="…elles réchauffent l’eau", de="…sie das Wasser erwärmen"), is_correct=False),
                               Reply(Text(fr="…elles forment un tapis sur lequel ils ne peuvent plus pondre leurs œufs", de="…die Fische auf den sich bildenden Algenteppichen nicht laichen können"), is_correct=False)})
        q5 = Question(question=Text(fr="Un corridor biologique, c’est…", de="Ein biologischer Korridor ist…"),
                      replies={Reply(Text(fr="… un ensemble d’espaces naturels assez proches les uns des autres, pour permettre aux animaux de se déplacer en sécurité", de="…ein System aus natürlichen Lebensräumen, die genügend nahe beieinander liegen, damit die Tiere sich sicher zwischen ihnen hin und her bewegen können"), is_correct=True),
                               Reply(Text(fr="… un champ utilisé pour faire des études biologiques sur les plantes", de="…ein Feld, auf dem Pflanzenforschung betrieben wird"), is_correct=False),
                               Reply(Text(fr="… un rayon de supermarché qui vend des produits bio", de="…eine Bio-Abteilung im Supermarkt"), is_correct=False)})
        q6 = Question(question=Text(fr="Que peut-on faire dans nos jardins pour faciliter la reproduction des lucanes ?", de="Was können wir in unserem Garten tun, um dem Hirschkäfer die Fortpflanzung zu erleichtern ?"),
                      replies={Reply(Text(fr="construire des murs en pierres sèches", de="Trockenmauern bauen"), is_correct=False),
                               Reply(Text(fr="laisser des tas de bois morts", de="Totholzhaufen liegen lassen"), is_correct=True),
                               Reply(Text(fr="planter des noisetiers", de="Haselsträucher pflanzen"), is_correct=False)})
        questions = {q1, q2, q3, q4, q5, q6}
        selection = questions.__len__()
        self.questions = random.sample(questions, selection)

        qi1 = Question(question=Text(fr="Sélectionnez le jardin qui est le meilleur corridor biologique. [i][Dessins: Mira Maeder][/i]", de="Wählen Sie denjenigen Garten aus, welcher den besten biologischen Korridor darstellt. [i][Zeichnen: Mira Maeder][/i]"),
                      replies={Reply(text='images/quiz/garden_draw1.jpg', is_correct=True),
                               Reply(text='images/quiz/garden_draw2.jpg', is_correct=False),
                               Reply(text='images/quiz/garden_draw3.jpg', is_correct=False)})
        qi2 = Question(question=Text(fr="Quel passage est construit spécialement pour les amphibiens ?  [i][Crédits photos: Trocmé / Meyer, KARCH / AURA Emmanuel Ammon][/i]", de="Welche der folgenden Wildtierpassagen wird speziell für Amphibien gebaut ? [i][Bildern: Trocmé / Meyer, KARCH / AURA Emmanuel Ammon][/i]"),
                      replies={Reply(text='images/quiz/passage_faune.jpg', is_correct=False),
                               Reply(text='images/quiz/tunnel_faune.jpg', is_correct=False),
                               Reply(text='images/quiz/crapauduc.jpg', is_correct=True)})
        questions = {qi1, qi2}
        self.question_images = random.sample(questions, 2)

        self.question_public_img = qi2

        self.question_public = Question(question=Text(fr="Quel âge avez-vous ?", de="Wie alt sind Sie ?"),
                      replies={Reply(Text(fr="Enfant (jusqu'à 16 ans)", de="Kinder (bis 16 Jahre)"), is_correct=True),
                               Reply(Text(fr="Adulte (à partir de 17 ans)", de="Erwaschene (ab 17 Jahre)"), is_correct=True)})
