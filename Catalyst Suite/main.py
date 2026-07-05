"""
=========================================================
CATALYST Suite
File      : main.py
Version   : 1.0.0
Author    : Srinath Jayakumar
Purpose   : Application Entry Point
=========================================================
"""

import customtkinter as ctk

from core.theme import (
    APP_NAME,
    APP_VERSION,
    WINDOW_WIDTH,
    WINDOW_HEIGHT,
    MIN_WIDTH,
    MIN_HEIGHT,
)

from core.app import CATALYSTSuite


def main():

    # ----------------------------
    # Configure CustomTkinter
    # ----------------------------
    ctk.set_appearance_mode("Light")
    ctk.set_default_color_theme("blue")

    # ----------------------------
    # Create Main Window
    # ----------------------------
    root = ctk.CTk()

    root.title(f"{APP_NAME}  |  Version {APP_VERSION}")

    root.geometry(f"{WINDOW_WIDTH}x{WINDOW_HEIGHT}")

    root.minsize(MIN_WIDTH, MIN_HEIGHT)

    # ----------------------------
    # Start Application
    # ----------------------------
    CATALYSTSuite(root)

    root.mainloop()


if __name__ == "__main__":
    main()