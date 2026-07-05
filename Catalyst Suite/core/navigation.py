"""
=========================================================
CATALYST Suite
File      : navigation.py
Version   : 1.0.0
Author    : Srinath Jayakumar
Purpose   : Navigation Manager
=========================================================
"""


class NavigationManager:

    def __init__(self):

        self.current_screen = None

    # -----------------------------------------------------

    def set_current_screen(self, screen_name):

        self.current_screen = screen_name

    # -----------------------------------------------------

    def get_current_screen(self):

        return self.current_screen