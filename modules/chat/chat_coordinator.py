import flet as ft
from modules.chat.chat_state import ChatState
from modules.chat.chat_logic import ChatLogic
from modules.chat.chat_view import ChatView

class ChatCoordinator:
    def __init__(self):
        self.state = ChatState()
        self.logic = ChatLogic(state=self.state)
        self.view = ChatView(logic=self.logic)
        self.logic.on_change = self.view.render

    def get_view(self):
        return self.view        