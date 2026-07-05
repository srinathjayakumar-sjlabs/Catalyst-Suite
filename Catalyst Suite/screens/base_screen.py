"""
=========================================================
CATALYST Suite
File      : base_screen.py
Version   : 1.0.0
Author    : Srinath Jayakumar
Purpose   : Base Screen for all application screens
=========================================================
"""

# =========================================================
# IMPORTS
# =========================================================

import customtkinter as ctk

from core.theme import *

# =========================================================
# BASE SCREEN
# =========================================================

class BaseScreen(ctk.CTkFrame):

    def __init__(
        self,
        master,
        title,
        subtitle=""
    ):

        super().__init__(
            master=master,
            fg_color=BACKGROUND
        )

        self.title = title
        self.subtitle = subtitle

        self.build_header()

    # -----------------------------------------------------

    def build_header(self):

        self.title_label = ctk.CTkLabel(
            self,
            text=self.title,
            font=HEADER_FONT,
            text_color=TEXT_COLOR
        )

        self.title_label.pack(
            anchor="w",
            padx=PAGE_PADDING,
            pady=(25,5)
        )

        if self.subtitle:

            self.subtitle_label = ctk.CTkLabel(
                self,
                text=self.subtitle,
                font=BODY_FONT,
                text_color=SUBTEXT_COLOR
            )

            self.subtitle_label.pack(
                anchor="w",
                padx=PAGE_PADDING
            )