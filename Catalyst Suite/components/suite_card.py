"""
=========================================================
CATALYST Suite
File      : suite_card.py
Version   : 1.0.0
Author    : Srinath Jayakumar
Purpose   : Large Dashboard Suite Card
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
# SUITE CARD
# =========================================================

class SuiteCard(ctk.CTkFrame):

    def __init__(
        self,
        master,
        title: str,
        description: str,
        icon_name: str,
        command: Callable
    ):

        super().__init__(
            master=master,
            width=SUITE_CARD_WIDTH,
            height=SUITE_CARD_HEIGHT,
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
            description,
            icon_name
        )

    # =====================================================

    def build_ui(
        self,
        title,
        description,
        icon_name
    ):

        # ---------------- Icon ----------------

        self.icon = ctk.CTkLabel(
            self,
            text="",

            image=icon_manager.get_icon(
                "suites",
                icon_name,
                size=(76,76)
            )
        )

        self.icon.pack(
            pady=(20,12)
        )

        # ---------------- Title ----------------

        self.title_label = ctk.CTkLabel(
            self,
            text=title,
            font=TITLE_FONT,
            text_color=TEXT_COLOR
        )

        self.title_label.pack()

        # ---------------- Description ----------------

        self.description_label = ctk.CTkLabel(
            self,
            text=description,
            font=BODY_FONT,
            text_color=SUBTEXT_COLOR,
            justify="center",
            wraplength=270
        )

        self.description_label.pack(
            pady=(10,20)
        )

        self.bind("<Button-1>", lambda e: self.command())

        self.icon.bind("<Button-1>", lambda e: self.command())

        self.title_label.bind("<Button-1>", lambda e: self.command())

        self.description_label.bind("<Button-1>", lambda e: self.command())

        self.bind_hover(self)

        self.bind_hover(self.icon)

        self.bind_hover(self.title_label)

        self.bind_hover(self.description_label)

    def on_enter(self, event=None):

        self.configure(
            fg_color="#EDF4FF"
        )


    def on_leave(self, event=None):

        self.configure(
            fg_color=CARD_BACKGROUND
        )

    def bind_hover(self, widget):

        widget.bind(
            "<Enter>",
            self.on_enter
        )

        widget.bind(
            "<Leave>",
            self.on_leave
        )