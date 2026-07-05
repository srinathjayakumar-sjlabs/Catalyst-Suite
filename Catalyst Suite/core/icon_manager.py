from pathlib import Path

from PIL import Image

import customtkinter as ctk


class IconManager:

    def __init__(self):

        self.icon_root = (
            Path(__file__).resolve().parent.parent
            / "assets"
            / "icons"
        )

        self.cache = {}

    def get_icon(
        self,
        category,
        name,
        size=(20, 20)
    ):

        cache_key = (
            category,
            name,
            size
        )

        if cache_key in self.cache:
            return self.cache[cache_key]

        icon_path = (
            self.icon_root
            / category
            / f"{name}.png"
        )

        if not icon_path.exists():
            raise FileNotFoundError(
                f"Icon not found : {icon_path}"
            )

        image = Image.open(
            icon_path
        )

        icon = ctk.CTkImage(
            light_image=image,
            dark_image=image,
            size=size
        )

        self.cache[cache_key] = icon

        return icon

icon_manager = IconManager()