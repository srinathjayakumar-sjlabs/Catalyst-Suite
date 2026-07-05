"""
=========================================================
CATALYST Suite
File      : app.py
Version   : 1.0.0
Author    : Srinath Jayakumar
Purpose   : Main Application Controller
=========================================================
"""

# =========================================================
# IMPORTS
# =========================================================

import customtkinter as ctk

from layouts.header import Header

from core.theme import BACKGROUND

from layouts.statusbar import StatusBar

from layouts.sidebar import Sidebar

from screens.home import HomeScreen

from screens.image_processing import ImageProcessingScreen

from modules.asin_packaging.ui import AsinPackagingUI

# =========================================================
# MAIN APPLICATION
# =========================================================

class CATALYSTSuite:
    """
    Main controller for CATALYSTSuite.

    Responsible for:
        • Creating the application layout
        • Managing navigation
        • Loading screens
    """

    # -----------------------------------------------------
    # Constructor
    # -----------------------------------------------------

    def __init__(self, root):

        self.root = root

        self.root.configure(
            fg_color=BACKGROUND
        )

        # ----------------------------------------------
        # Permanent Layout
        # ----------------------------------------------

        self.create_layout()

        # ----------------------------------------------
        # Load First Screen
        # ----------------------------------------------

        self.load_home()

    # =====================================================
    # LAYOUT
    # =====================================================

    def create_layout(self):

        # ---------------- Header ----------------

        self.header = Header(self.root)

        self.header.pack(fill="x")

        # ---------------- Middle Area ----------------

        self.middle_frame = ctk.CTkFrame(
            self.root,
            fg_color=BACKGROUND,
            corner_radius=0
        )

        self.middle_frame.pack(
            fill="both",
            expand=True
        )

        # ---------------- Sidebar ----------------

        self.sidebar = Sidebar(
            self.middle_frame,
            self.navigate
        )

        self.sidebar.pack(
            side="left",
            fill="y"
        )

        # ---------------- Content ----------------

        self.content_frame = ctk.CTkFrame(
            self.middle_frame,
            fg_color=BACKGROUND,
            corner_radius=0
        )

        self.content_frame.pack(
            side="left",
            fill="both",
            expand=True
        )

        # ---------------- Status Bar ----------------

        self.statusbar = StatusBar(self.root)

        self.statusbar.pack(
            fill="x",
            side="bottom"
        )

    # =====================================================
    # NAVIGATION
    # =====================================================

    def clear_content(self):

        for widget in self.content_frame.winfo_children():
            widget.destroy()

    # =====================================================
    # HOME
    # =====================================================

    def load_home(self):

        self.clear_content()

        home = HomeScreen(
            self.content_frame,
            self.navigate
        )

        home.pack(
            fill="both",
            expand=True
        )

    def navigate(self, screen_id):

        # Clear current content
        for widget in self.content_frame.winfo_children():
            widget.destroy()

        # -----------------------------
        # HOME
        # -----------------------------
        if screen_id == "home":
            self.load_home()
            return

        # -----------------------------
        # IMAGE PROCESSING
        # -----------------------------
        if screen_id == "image_processing":

            screen = ImageProcessingScreen(self.content_frame)
            screen.pack(fill="both", expand=True)

            return

        # -----------------------------
        # ASIN PACKAGING
        # -----------------------------
        if screen_id == "asin_packaging":

            screen = AsinPackagingUI(self.content_frame)

            screen.pack(
                fill="both",
                expand=True
            )

            return

        # -----------------------------
        # Remaining screens
        # -----------------------------

        label = ctk.CTkLabel(
            self.content_frame,
            text=f"{screen_id.replace('_',' ').title()} Screen\n\nComing Soon",
            font=("Segoe UI", 24)
        )

        label.pack(expand=True)