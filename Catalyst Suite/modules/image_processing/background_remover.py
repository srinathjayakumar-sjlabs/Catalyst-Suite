"""
==========================================
CATALYST Suite
Background Removal Engine
Version : 1.0
==========================================
"""

try:
    from transparent_background import Remover
except ImportError:
    Remover = None

import os
import numpy as np
from PIL import Image


class BackgroundRemover:

    def __init__(self):

        self.remover = None



    def initialize(self):

        if Remover is None:

            print("❌ transparent-background library not installed.")

            return

        try:

            print("Loading AI Background Removal Model...")

            self.remover = Remover(
                mode="base-nightly"
            )

            print("✅ AI Model Loaded Successfully")

        except Exception as e:

            print(f"❌ Failed to load model: {e}")

    def remove_background(self, image):

        if self.remover is None:
            self.initialize()

        if self.remover is None:
            return image

        result = self.remover.process(image).convert("RGBA")

        arr = np.array(result)

        alpha = arr[:, :, 3]
        alpha[alpha < 8] = 0
        arr[:, :, 3] = alpha

        fg = Image.fromarray(arr)

        bg = Image.new("RGBA", fg.size, (255, 255, 255, 255))
        bg.paste(fg, (0, 0), fg)

        return bg.convert("RGB")

    def load_image(self, image_path):

        image = Image.open(image_path).convert("RGB")

        return image