"""
=========================================================
CATALYST Suite
File      : header.py
Version   : 1.0.0
Author    : Srinath Jayakumar
Purpose   : Permanent Application Header
=========================================================
"""

# =========================================================
# IMPORTS
# =========================================================

import customtkinter as ctk

from core.theme import (
    PRIMARY_BLUE,
    APP_NAME,
    APP_VERSION,
)

# =========================================================
# HEADER
# =========================================================

class Header(ctk.CTkFrame):

    def __init__(self, master):

        super().__init__(
            master=master,
            fg_color=PRIMARY_BLUE,
            height=90,
            corner_radius=0
        )

        self.pack_propagate(False)

        self.build_ui()

    # -----------------------------------------------------

    def build_ui(self):

        # Left Section
        left = ctk.CTkFrame(
            self,
            fg_color="transparent"
        )

        left.pack(
            side="left",
            padx=25,
            pady=15
        )

        # Application Name

        app_name = ctk.CTkLabel(
            left,
            text=APP_NAME,
            font=("Bahnschrift", 24, "bold"),
            text_color="white"
        )

        app_name.pack(anchor="w")

        # Subtitle

        subtitle = ctk.CTkLabel(
            left,
            text="Enterprise Automation Platform",
            font=("Segoe UI", 11),
            text_color="#DCEBFF"
        )

        subtitle.pack(anchor="w")

        # Right Section

        right = ctk.CTkFrame(
            self,
            fg_color="transparent"
        )

        right.pack(
            side="right",
            padx=25
        )

        version = ctk.CTkLabel(
            right,
            text=f"Version {APP_VERSION}",
            font=("Segoe UI", 12),
            text_color="white"
        )

        version.pack()