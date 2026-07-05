"""
=========================================================
CATALYST Suite
Image Processing Screen
=========================================================
"""

from modules.image_processing.ui import ImageProcessingUI

from screens.base_screen import BaseScreen


class ImageProcessingScreen(BaseScreen):

    def __init__(self, master):

        super().__init__(
            master,
            title="Image Processing Suite",
            subtitle="Background Removal, Optimizer and Validation"
        )

        ui = ImageProcessingUI(self)
        ui.pack(fill="both", expand=True)