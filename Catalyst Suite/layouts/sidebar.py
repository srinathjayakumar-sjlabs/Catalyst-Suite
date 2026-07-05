"""
=========================================================
CATALYST Suite
File      : sidebar.py
Version   : 1.0.0
Author    : Srinath Jayakumar
Purpose   : Application Navigation Sidebar
=========================================================
"""

from core.icon_manager import icon_manager

import customtkinter as ctk

from core.theme import (
    PRIMARY_BLUE,
    BODY_FONT,
    SIDEBAR_WIDTH,
    SIDEBAR_HOVER
)


class Sidebar(ctk.CTkFrame):

    def __init__(self, master, callback):


        super().__init__(
            master=master,
            width=SIDEBAR_WIDTH,
            fg_color="#F3F6FA",
            corner_radius=0
        )

        self.callback = callback
  
        self.pack_propagate(False)

        self.build_ui()

    def build_ui(self):

        menu_items = [

            ("home", "Home", "home"),

            ("image_processing", "Image Processing", "image"),

            ("asin_packaging", "ASIN Packaging", "package"),

            ("settings", "Settings", "settings"),

            ("help", "Help", "help"),

            ("about", "About", "about"),

            ("logs", "Logs", "logs")

        ]

        for module_id, title, icon_name in menu_items:

            button = ctk.CTkButton(
                self,
                text=title,

                image=icon_manager.get_icon(
                    "navigation",
                    icon_name,
                    size=(24, 24)
                ),

                compound="left",   

                command=lambda m=module_id: self.callback(m),
                height=42,
                corner_radius=8,
                fg_color="transparent",
                hover_color=SIDEBAR_HOVER,
                text_color="black",
                anchor="w",
                border_spacing=10,
                font=BODY_FONT
            )

            button.pack(
                fill="x",
                padx=12,
                pady=5
            )