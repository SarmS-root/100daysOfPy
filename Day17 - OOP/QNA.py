class QNA:
    def __init__(self, text, answer):
        self.text = text
        self.answer = answer

    def ask(self):
        print("Question: ")
        print(self.text)

