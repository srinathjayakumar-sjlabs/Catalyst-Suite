"""
=========================================================
CATALYST	 Suite
File      : quick_card.py
Version   : 1.0.0
Author    : Srinath Jayakumar
Purpose   : Quick Access Dashboard Card
=========================================================
"""

# =========================================================
# IMPORTS
# =========================================================

from core.icon_manager import icon_manager

import customtkinter as ctk

from typing import Callable

from core.theme import *

# =========================================================
# QUICK CARD
# =========================================================

class QuickCard(ctk.CTkFrame):

    def __init__(
        self,
        master,
        title: str,
        icon_name: str,
        command: Callable
    ):

        super().__init__(
            master=master,
            width=QUICK_CARD_WIDTH,
            height=QUICK_CARD_HEIGHT,
            fg_color=CARD_BACKGROUND,
            border_width=0,
            border_color=BORDER_COLOR,
            corner_radius=CARD_CORNER_RADIUS,

            cursor="hand2"
        )

        self.command = command

        self.pack_propagate(False)

        self.build_ui(
            title,
            icon_name
        )

    # =====================================================

    def build_ui(
        self,
        title,
        icon_name
    ):

        icon = ctk.CTkLabel(
            self,
            text="",
            image=icon_manager.get_icon(
                "quick_access",
                icon_name,
                size=(36,36)
            )
        )

        icon.pack(
            pady=(20,8)
        )

        title_label = ctk.CTkLabel(
            self,
            text=title,
            font=BUTTON_FONT,
            text_color=TEXT_COLOR
        )

        title_label.pack()

        self.bind(
            "<Button-1>",
            lambda e: self.command()
        )

        icon.bind(
            "<Button-1>",
            lambda e: self.command()
        )

        title_label.bind(
            "<Button-1>",
            lambda e: self.command()
        )

        self.bind_hover(self)

        self.bind_hover(icon)

        self.bind_hover(title_label)

    def on_enter(self, event=None):

        self.configure(
            fg_color="#EDF4FF"
        )


    def on_leave(self, event=None):

        self.configure(
            fg_color=CARD_BACKGROUND
        )


    def bind_hover(self, widget):

        widget.bind("<Enter>", self.on_enter)
        widget.bind("<Leave>", self.on_leave)