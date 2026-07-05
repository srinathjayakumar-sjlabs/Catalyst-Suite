"""
=========================================================
CATALYST Suite
File      : ui.py
Module    : ASIN Packaging Suite
Version   : 1.0.0
Author    : Srinath Jayakumar
Purpose   : ASIN Packaging User Interface
=========================================================
"""

import customtkinter as ctk

from core.icon_manager import icon_manager

from modules.asin_packaging.controller import AsinPackagingController


class AsinPackagingUI(ctk.CTkFrame):

    def __init__(self, parent):

        super().__init__(
            parent,
            fg_color="transparent"
        )

        self.controller = AsinPackagingController(self)

        self.build_ui()

    def build_ui(self):

        self.pack(
            fill="both",
            expand=True
        )

        # -----------------------------------------
        # Main Container
        # -----------------------------------------

        self.main_container = ctk.CTkFrame(
            self,
            fg_color="transparent"
        )

        self.main_container.pack(
            fill="both",
            expand=True,
            padx=20,
            pady=20
        )

        # -----------------------------------------
        # Header
        # -----------------------------------------

        self.title_label = ctk.CTkLabel(
            self.main_container,
            text="ASIN Packaging Suite",
            font=("Segoe UI", 24, "bold")
        )

        self.title_label.pack(
            anchor="w",
            pady=(0, 15)
        )

        # -----------------------------------------
        # Top Card
        # -----------------------------------------

        self.build_top_card()

        self.build_processing_section()

        self.build_activity_log()

    def build_processing_section(self):

        self.processing_frame = ctk.CTkFrame(
            self.main_container,
            fg_color="transparent"
        )

        self.processing_frame.pack(
            fill="x",
            pady=(0, 20)
        )

        self.processing_left = ctk.CTkFrame(
            self.processing_frame,
            fg_color="transparent"
        )

        self.processing_left.pack(
            side="left"
        )

        self.processing_right = ctk.CTkFrame(
            self.processing_frame,
            fg_color="transparent"
        )

        self.processing_right.pack(
            side="left",
            fill="x",
            expand=True,
            padx=(25, 0)
        )

        self.build_start_stop_buttons()
        self.build_progress_section()

    def build_start_stop_buttons(self):

        self.stop_btn = ctk.CTkButton(
            self.processing_left,
            text="Stop Packaging",
            width=180,
            height=40,
            fg_color="#D32F2F",
            hover_color="#B71C1C",
            image=icon_manager.get_icon(
                "buttons",
                "stop_packaging",
                size=(18,18)
            ),

            compound="left",
            command=self.controller.stop_packaging
        )

        self.stop_btn.pack()

    def build_progress_section(self):

        self.progress_title = ctk.CTkLabel(
            self.processing_right,
            text="Packaging Progress",
            font=("Segoe UI", 16, "bold")
        )

        self.progress_title.pack(anchor="w")

        self.progress_bar = ctk.CTkProgressBar(
            self.processing_right,
            height=16
        )

        self.progress_bar.pack(
            fill="x",
            pady=(8, 8)
        )

        self.progress_bar.set(0)

        self.progress_label = ctk.CTkLabel(
            self.processing_right,
            text="Waiting to Start...",
            font=("Segoe UI", 13)
        )

        self.progress_label.pack(anchor="w")

    def build_top_card(self):

        # -----------------------------------------------------
        # Top Card
        # -----------------------------------------------------

        self.top_card = ctk.CTkFrame(
            self.main_container,
            corner_radius=12
        )

        self.top_card.pack(
            fill="x",
            pady=(0, 20)
        )

        # -----------------------------------------------------
        # 40 | 30 | 30 Layout
        # -----------------------------------------------------

        self.top_card.grid_columnconfigure(
            0,
            weight=4
        )

        self.top_card.grid_columnconfigure(
            1,
            weight=3
        )

        self.top_card.grid_columnconfigure(
            2,
            weight=3
        )

        # -----------------------------------------------------
        # Left Column
        # -----------------------------------------------------

        self.left_frame = ctk.CTkFrame(
            self.top_card,
            fg_color="transparent"
        )

        self.left_frame.grid(
            row=0,
            column=0,
            sticky="nsew",
            padx=(20, 10),
            pady=20
        )

        # -----------------------------------------------------
        # Image Folder
        # -----------------------------------------------------

        self.image_folder_label = ctk.CTkLabel(
            self.left_frame,
            text=" Image Folder",

            image=icon_manager.get_icon(
                "buttons",
                "browse_folder",
                size=(20,20)
            ),

            compound="left",
            font=("Segoe UI", 15, "bold")
        )

        self.image_folder_label.pack(
            anchor="w"
        )

        self.selected_folder_label = ctk.CTkLabel(
            self.left_frame,
            text=" No Folder Selected",

            image=icon_manager.get_icon(
                "buttons",
                "browse_folder",
                size=(18,18)
            ),

            compound="left",
            font=("Segoe UI", 14)
        )

        self.selected_folder_label.pack(
            anchor="w",
            pady=(5, 20)
        )

        # -----------------------------------------------------
        # Excel Mapping
        # -----------------------------------------------------

        self.excel_mapping_label = ctk.CTkLabel(
            self.left_frame,
            text=" Excel Mapping",

            image=icon_manager.get_icon(
                "buttons",
                "browse_excel",
                size=(20,20)
            ),

            compound="left",
            font=("Segoe UI", 15, "bold")
        )

        self.excel_mapping_label.pack(
            anchor="w"
        )

        self.selected_excel_label = ctk.CTkLabel(
            self.left_frame,
            text=" No Excel File Selected",

            image=icon_manager.get_icon(
                "buttons",
                "browse_excel",
                size=(18,18)
            ),

            compound="left",
            font=("Segoe UI", 14)
        )

        self.selected_excel_label.pack(
            anchor="w",
            pady=(5, 0)
        )

        # -----------------------------------------------------
        # Middle Column
        # -----------------------------------------------------

        self.middle_frame = ctk.CTkFrame(
            self.top_card,
            fg_color="transparent"
        )

        self.middle_frame.grid(
            row=0,
            column=1,
            sticky="nsew",
            padx=10,
            pady=20
        )

        # -----------------------------------------------------
        # Browse Folder Button
        # -----------------------------------------------------

        self.browse_folder_btn = ctk.CTkButton(
            self.middle_frame,
            text="Browse Folder",
            width=180,
            height=40,
            image=icon_manager.get_icon(
                "buttons",
                "browse_folder",
                size=(18,18)
            ),

            compound="left",
            command=self.controller.browse_folder
        )

        self.browse_folder_btn.pack(
            pady=(8, 35)
        )

        # -----------------------------------------------------
        # Browse Excel Button
        # -----------------------------------------------------

        self.browse_excel_btn = ctk.CTkButton(
            self.middle_frame,
            text="Browse Excel",
            width=180,
            height=40,
            image=icon_manager.get_icon(
                "buttons",
                "browse_excel",
                size=(18,18)
            ),

            compound="left",
            command=self.controller.browse_excel
        )

        self.browse_excel_btn.pack()

        # -----------------------------------------------------
        # Right Column
        # -----------------------------------------------------

        self.right_frame = ctk.CTkFrame(
            self.top_card,
            fg_color="transparent"
        )

        self.right_frame.grid(
            row=0,
            column=2,
            sticky="nsew",
            padx=(10, 20),
            pady=20
        )

        # -----------------------------------------------------
        # Validation Summary
        # -----------------------------------------------------

        self.validation_title = ctk.CTkLabel(
            self.right_frame,
            text="Validation Summary",
            font=("Segoe UI", 15, "bold")
        )

        self.validation_title.pack(
            anchor="w"
        )

        self.folders_found_label = ctk.CTkLabel(
            self.right_frame,
            text="Folders Found : 0",
            font=("Segoe UI", 14)
        )

        self.folders_found_label.pack(
            anchor="w",
            pady=(8, 5)
        )

        self.images_found_label = ctk.CTkLabel(
            self.right_frame,
            text="Images Found : 0",
            font=("Segoe UI", 14)
        )

        self.images_found_label.pack(
            anchor="w",
            pady=(0, 20)
        )

        # -----------------------------------------------------
        # Validate Button
        # -----------------------------------------------------

        self.validate_btn = ctk.CTkButton(
            self.right_frame,
            text="Validate",
            width=180,
            height=40,
            image=icon_manager.get_icon(
                "buttons",
                "validate",
                size=(18,18)
            ),

            compound="left",
            command=self.controller.validate
        )

        self.validate_btn.pack(
            fill="x"
        )

    def build_activity_log(self):

        # -----------------------------------------------------
        # Activity Log Card
        # -----------------------------------------------------

        self.log_card = ctk.CTkFrame(
            self.main_container,
            corner_radius=12
        )

        self.log_card.pack(
            fill="both",
            expand=True
        )

        # -----------------------------------------------------
        # Activity Log Title
        # -----------------------------------------------------

        self.log_title = ctk.CTkLabel(
            self.log_card,
            text=" Activity Log",

            image=icon_manager.get_icon(
                "navigation",
                "logs",
                size=(20,20)
            ),

            compound="left",
            font=("Segoe UI", 16, "bold")
        )

        self.log_title.pack(
            anchor="w",
            padx=20,
            pady=(15, 10)
        )

        # -----------------------------------------------------
        # Activity Log Textbox
        # -----------------------------------------------------

        self.activity_log = ctk.CTkTextbox(
            self.log_card,
            fg_color="#1E1E1E",
            text_color="#00FF66",
            font=("Consolas", 11),
            corner_radius=8
        )

        self.activity_log.pack(
            fill="both",
            expand=True,
            padx=20,
            pady=(0, 20)
        )

        self.activity_log.configure(
            state="disabled"
        )

    def add_log(self, message):

        self.activity_log.configure(
            state="normal"
        )

        self.activity_log.insert(
            "end",
            message + "\n"
        )

        self.activity_log.see(
            "end"
        )

        self.activity_log.configure(
            state="disabled"
        )

    def clear_log(self):

        self.activity_log.configure(
            state="normal"
        )

        self.activity_log.delete(
            "1.0",
            "end"
        )

        self.activity_log.configure(
            state="disabled"
        )

    def update_progress(
        self,
        current,
        total,
        filename=""
    ):

        if total <= 0:
            percentage = 0
        else:
            percentage = current / total

        self.progress_bar.set(
            percentage
        )

        self.progress_label.configure(
            text=f"{current}/{total}  •  {filename}"
        )

    def reset_packaging_state(self):

        # Reset Progress Bar
        self.progress_bar.set(0)

        # Reset Progress Text
        self.progress_label.configure(
            text="Waiting to Start..."
        )

        # Clear Activity Log
        self.clear_log()