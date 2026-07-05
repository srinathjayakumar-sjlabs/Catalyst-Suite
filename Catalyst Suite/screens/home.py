"""
=========================================================
CATALYST Suite
File      : home.py
Version   : 1.0.0
Author    : Srinath Jayakumar
Purpose   : Home Dashboard
=========================================================
"""

import customtkinter as ctk

from components.suite_card import SuiteCard
from components.quick_card import QuickCard

from core.theme import *


from screens.base_screen import BaseScreen


class HomeScreen(BaseScreen):

    def __init__(
        self,
        master,
        navigate_callback
    ):

        super().__init__(
            master=master,
            title="Welcome Back, Srinath",
            subtitle="Choose one of the suites below to begin your work."
        )

        self.navigate = navigate_callback

        self.build_ui()

    # -----------------------------------------------------

    def build_ui(self):


        suite_heading = ctk.CTkLabel(
             self,
             text="Your Suites",
             font=TITLE_FONT,
             text_color=TEXT_COLOR
        )

        suite_heading.pack(
            anchor="w",
            padx=PAGE_PADDING,
            pady=(40, 10)
        )

        # ==========================================
        # Suite Cards
        # ==========================================

        suite_frame = ctk.CTkFrame(
            self,
            fg_color="transparent"
        )

        suite_frame.pack(
            pady=30
        )

        image_suite = SuiteCard(
            suite_frame,
            title="Image Processing Suite",
            description="Background Removal\nImage Optimizer\nImage Validator",

            icon_name="image_suite",

            command=lambda: self.navigate("image_processing")
        )

        image_suite.pack(
            side="left",
            padx=20
        )

        asin_suite = SuiteCard(
            suite_frame,
            title="ASIN Packaging Suite",
            description="Folder Creation\nRenaming\nPackaging",

            icon_name="package_suite",

            command=lambda: self.navigate("asin_packaging")
        )

        asin_suite.pack(
            side="left",
            padx=20
        )

        # ==========================================
        # Quick Access
        # ==========================================

        quick_title = ctk.CTkLabel(
            self,
            text="Quick Access",
            font=TITLE_FONT
        )

        quick_title.pack(
            anchor="w",
            padx=30,
            pady=(20,10)
        )

        quick_frame = ctk.CTkFrame(
            self,
            fg_color="transparent"
        )

        quick_frame.pack()

        QuickCard(
            quick_frame,
            title="Settings",

            icon_name="settings",

            command=lambda: self.navigate("settings")
        ).pack(side="left", padx=10)

        QuickCard(
            quick_frame,
            title="Help",

            icon_name="help",

            command=lambda: self.navigate("help")
        ).pack(side="left", padx=10)

        QuickCard(
            quick_frame,
            title="About",

            icon_name="about",

            command=lambda: self.navigate("about")
        ).pack(side="left", padx=10)

        QuickCard(
            quick_frame,
            title="Logs",

            icon_name="logs",

            command=lambda: self.navigate("logs")
        ).pack(side="left", padx=10)