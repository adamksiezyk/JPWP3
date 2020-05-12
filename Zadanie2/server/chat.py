class Chat(object):

    def __init__(self, r):
        self.chat_tablica = []
        self.runda = r

    def update_chat(self, msg):
        self.chat_tablica.append(msg)

    def get_chat(self):
        return self.chat_tablica
