class UserSession:
    def __init__(self, user_id, language):
        self.user_id = user_id
        self.language = language
        self.message_history = []

    def add_message(self, role, content):
        self.message_history.append({"role": role, "content": content})

    def get_history(self):
        return self.message_history
