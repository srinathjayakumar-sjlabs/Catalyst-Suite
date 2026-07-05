"""
=========================================================
CATALYST Suite
File      : statusbar.py
Version   : 1.0.0
Author    : Srinath Jayakumar
Purpose   : Permanent Application Status Bar
=========================================================
"""

# =========================================================
# IMPORTS
# =========================================================

import customtkinter as ctk

from core.theme import (
    PRIMARY_BLUE,
    BODY_FONT,
    APP_VERSION
)

# =========================================================
# STATUS BAR
# =========================================================

class StatusBar(ctk.CTkFrame):

    def __init__(self, master):

        super().__init__(
            master=master,
            fg_color=PRIMARY_BLUE,
            height=34,
            corner_radius=0
        )

        self.pack_propagate(False)

        self.build_ui()

    # -----------------------------------------------------

    def build_ui(self):

        # Left Status

        self.status_label = ctk.CTkLabel(
            self,
            text="🟢 Ready",
            font=BODY_FONT,
            text_color="white"
        )

        self.status_label.pack(
            side="left",
            padx=15
        )

        # Right Version

        self.version_label = ctk.CTkLabel(
            self,
            text=f"Version {APP_VERSION}",
            font=BODY_FONT,
            text_color="white"
        )

        self.version_label.pack(
            side="right",
            padx=15
        )

    # -----------------------------------------------------

    def set_status(self, message):

        self.status_label.configure(
            text=message
        )