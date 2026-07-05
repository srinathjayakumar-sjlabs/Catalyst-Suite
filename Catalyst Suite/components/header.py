"""
=========================================================
CATALYSTF Suite
File      : header.py
Version   : 1.0.0
Author    : Srinath Jayakumar
Purpose   : Application Header Component
=========================================================
"""

import customtkinter as ctk

from core.theme import (
    PRIMARY_BLUE,
    TITLE_FONT,
    SUBTITLE_FONT
)


class Header(ctk.CTkFrame):
    """
    Reusable Header Component
    """

    def __init__(
        self,
        master,
        title,
        subtitle=""
    ):

        super().__init__(
            master,
            fg_color=PRIMARY_BLUE,
            corner_radius=0,
            height=110
        )

        self.pack_propagate(False)

        # ------------------------------------------
        # Main Title
        # ------------------------------------------

        title_label = ctk.CTkLabel(
            self,
            text=title,
            font=TITLE_FONT,
            text_color="white"
        )

        title_label.pack(
            pady=(18, 0)
        )

        # ------------------------------------------
        # Subtitle
        # ------------------------------------------

        subtitle_label = ctk.CTkLabel(
            self,
            text=subtitle,
            font=SUBTITLE_FONT,
            text_color="#DCEBFF"
        )

        subtitle_label.pack(
            pady=(5, 15)
        )