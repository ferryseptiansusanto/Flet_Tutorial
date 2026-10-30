from dataclasses import dataclass

@dataclass
class ChatState:
    messages: list = None
    current_message: str = ""
