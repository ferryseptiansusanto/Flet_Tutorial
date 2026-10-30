import asyncio
from dataclasses import dataclass
from typing import List, Optional

import flet as ft


@dataclass
class Message:
    user_name: str
    text: str
    message_type: str  # "chat_message" | "login_message"


@ft.control
class ChatMessage(ft.Row):
    message: Message = None
    vertical_alignment: ft.CrossAxisAlignment = ft.CrossAxisAlignment.START

    def init(self) -> None:
        self.controls = [
            ft.CircleAvatar(
                content=ft.Text(self.get_initials(self.message.user_name)),
                color=ft.Colors.WHITE,
                bgcolor=self.get_avatar_color(self.message.user_name),
            ),
            ft.Column(
                tight=True,
                spacing=5,
                controls=[
                    ft.Text(self.message.user_name, weight=ft.FontWeight.BOLD),
                    ft.Text(self.message.text, selectable=True),
                ],
            ),
        ]

    def get_initials(self, user_name: str) -> str:
        if user_name:
            return user_name[:1].capitalize()
        return "?"

    def get_avatar_color(self, user_name: str) -> str:
        colors_lookup: List[str] = [
            ft.Colors.AMBER,
            ft.Colors.BLUE,
            ft.Colors.BROWN,
            ft.Colors.CYAN,
            ft.Colors.GREEN,
            ft.Colors.INDIGO,
            ft.Colors.LIME,
            ft.Colors.ORANGE,
            ft.Colors.PINK,
            ft.Colors.PURPLE,
            ft.Colors.RED,
            ft.Colors.TEAL,
            ft.Colors.YELLOW,
        ]
        return colors_lookup[hash(user_name) % len(colors_lookup)]


async def main(page: ft.Page) -> None:
    page.horizontal_alignment = ft.CrossAxisAlignment.STRETCH
    page.title = "Flet Chat - v1.0+"

    # Chat messages stream container
    chat_list = ft.ListView(
        expand=True,
        spacing=10,
        auto_scroll=True,
    )

    current_user_name: Optional[str] = None

    async def on_message_received(message: Message) -> None:
        if message.message_type == "chat_message":
            msg_control: ft.Control = ChatMessage(message=message)
        else:
            msg_control = ft.Text(
                message.text,
                italic=True,
                color=ft.Colors.ON_SURFACE_VARIANT,
                size=12,
            )
        chat_list.controls.append(msg_control)
        page.update()

    page.pubsub.subscribe(on_message_received)

    # Message input form
    new_message_field = ft.TextField(
        hint_text="Write a message...",
        autofocus=True,
        shift_enter=True,
        min_lines=1,
        max_lines=5,
        filled=True,
        expand=True,
    )

    async def send_message_click(e: ft.ControlEvent) -> None:
        text: str = new_message_field.value.strip() if new_message_field.value else ""
        if text and current_user_name:
            page.pubsub.send_all(
                Message(
                    user_name=current_user_name,
                    text=text,
                    message_type="chat_message",
                )
            )
            new_message_field.value = ""
            new_message_field.focus()
            page.update()

    new_message_field.on_submit = send_message_click

    send_btn = ft.IconButton(
        icon=ft.Icons.SEND_ROUNDED,
        tooltip="Send message",
        on_click=send_message_click,
    )

    # Login / Welcome Dialog setup
    join_user_name = ft.TextField(
        label="Enter your name to join the chat",
        autofocus=True,
    )

    async def join_chat_click(e: ft.ControlEvent) -> None:
        nonlocal current_user_name
        name: str = join_user_name.value.strip() if join_user_name.value else ""
        if not name:
            join_user_name.error = "Name cannot be blank!"
            join_user_name.update()
            return

        current_user_name = name
        page.pop_dialog()

        new_message_field.prefix = ft.Text(f"{name}: ")
        page.update()

        page.pubsub.send_all(
            Message(
                user_name=name,
                text=f"{name} has joined the chat.",
                message_type="login_message",
            )
        )

    join_user_name.on_submit = join_chat_click

    welcome_dialog = ft.AlertDialog(
        modal=True,
        title=ft.Text("Welcome!"),
        content=ft.Column(
            controls=[join_user_name],
            width=300,
            height=70,
            tight=True,
        ),
        actions=[
            ft.Button(
                content=ft.Text("Join chat"),
                on_click=join_chat_click,
            )
        ],
        actions_alignment=ft.MainAxisAlignment.END,
    )

    # Layout assembling
    page.add(
        ft.Container(
            content=chat_list,
            border=ft.Border.all(1, ft.Colors.OUTLINE),
            border_radius=5,
            padding=10,
            expand=True,
        ),
        ft.Row(
            controls=[
                new_message_field,
                send_btn,
            ]
        ),
    )

    # Show entry dialog via Page Dialog Manager
    page.show_dialog(welcome_dialog)


if __name__ == "__main__":
    ft.run(main)