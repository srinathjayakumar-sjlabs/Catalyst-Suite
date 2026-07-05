"""
=========================================================
CATALYST Suite
Image Processing Module UI
Version : 1.0.0
=========================================================
"""

import customtkinter as ctk

from core.icon_manager import icon_manager

import os

from modules.image_processing.controller import ImageProcessingController

class ImageProcessingUI(ctk.CTkFrame):

    def __init__(self, master):

        super().__init__(
            master,
            fg_color="transparent"
        )

        self.controller = ImageProcessingController(self)

        self.build_ui()

    # -----------------------------------------------------

    def build_ui(self):

        # ==============================
        # Top Section
        # ==============================

        top_section = ctk.CTkFrame(
            self,
            fg_color="transparent"
        )

        top_section.pack(
            fill="x",
            padx=30,
            pady=(10,20)
        )

        left_top = ctk.CTkFrame(
            top_section,
            fg_color="transparent"
        )

        left_top.pack(
            side="left",
            fill="x",
            expand=True
        )

        self.build_folder_card(left_top)     

        # ==============================
        # Processing Section
        # ==============================

        processing_frame = ctk.CTkFrame(
            self,
            fg_color="transparent"
        )

        processing_frame.pack(
            fill="x",
            padx=30,
            pady=(0,20)
        )

        # LEFT

        left = ctk.CTkFrame(
            processing_frame,
            fg_color="transparent"
        )

        left.pack(
            side="left"
        )

        self.start_btn = ctk.CTkButton(
            left,
            text="Start Processing",
            image=icon_manager.get_icon(
                "buttons",
                "start_packaging",
                size=(16,16)
            ),

            compound="left",
            width=180,
            height=40,
            command=self.controller.start_processing
        )

        self.start_btn.pack()

        self.stop_btn = ctk.CTkButton(
            left,
            text="Stop",
            image=icon_manager.get_icon(
                "buttons",
                "stop_packaging",
                size=(16,16)
            ),

            compound="left",
            width=180,
            height=40,
           fg_color="#D32F2F",
           hover_color="#B71C1C",
           state="normal",
           command=self.controller.stop_processing
        )

        self.stop_btn.pack(
            pady=(10,0)
        )

        # RIGHT

        right = ctk.CTkFrame(
            processing_frame,
            fg_color="transparent"
        )

        right.pack(
            side="right",
            fill="x",
            expand=True,
            padx=(25,0)
        )


        ctk.CTkLabel(
            right,
            text="Processing Progress",
            font=("Segoe UI",14,"bold")
        ).pack(anchor="w")

        self.progress = ctk.CTkProgressBar(
            right,
            width=520
        )

        self.progress.pack(
            pady=(8,0),
            anchor="w"
        )

        self.progress.set(0)

        self.progress_label = ctk.CTkLabel(
            right,
            text="Waiting..."
        )

        self.progress_label.pack(
            anchor="w",
            pady=(5,0)
        )

        # ==========================================
        # Activity Log
        # ==========================================

        log_card = ctk.CTkFrame(
            self,
            corner_radius=12,
            border_width=1,
            border_color="#D9D9D9",
            fg_color="white"
        )

        log_card.pack(
            fill="both",
            expand=True,
            padx=30,
            pady=(10,20)
        )

        ctk.CTkLabel(
            log_card,
            text="Activity Log",
            image=icon_manager.get_icon(
                "navigation",
                "logs",
                size=(22,22)
            ),
            compound="left",
            font=("Segoe UI",16,"bold")
        ).pack(
            anchor="w",
            padx=20,
            pady=(15,10)
        )

        self.activity_log = ctk.CTkTextbox(
            log_card,
            height=220,
            fg_color="#1E1E1E",
            text_color="#00FF7F",
            font=("Consolas",11),
            corner_radius=8
        )

        self.activity_log.pack(
            fill="both",
            expand=True,
            padx=20,
            pady=(0,20)
        )

        self.activity_log.configure(state="disabled")

        
    def update_folder_path(self, folder_path):

        self.folder_name.configure(
            text=f" {os.path.basename(folder_path)}",

            image=icon_manager.get_icon(
                "buttons",
                "browse_folder",
                size=(20,20)
            )
        )

        self.folder_path_label.configure(
            text=folder_path
        )

    def update_progress(self, current, total, filename=""):

        percentage = current / total if total else 0

        self.progress.set(percentage)

        self.progress_label.configure(
            text=f"{current}/{total}  ({int(percentage*100)}%)\n{filename}"
        )

        self.update_idletasks()

  
    def add_log(self, message):

        from datetime import datetime

        timestamp = datetime.now().strftime("%H:%M:%S")

        self.activity_log.configure(state="normal")

        self.activity_log.insert(
            "end",
            f"[{timestamp}] {message}\n"
        )

        # Auto Scroll
        self.activity_log.see("end")

        self.activity_log.update_idletasks()

        self.activity_log.configure(state="disabled")

    def clear_log(self):

        self.activity_log.configure(state="normal")

        self.activity_log.delete("1.0", "end")

        self.activity_log.configure(state="disabled")


    def build_folder_card(self, parent):

        # ==============================
        # Folder Card
        # ==============================

        self.folder_card = ctk.CTkFrame(
            parent,
            corner_radius=12,
            border_width=1,
            border_color="#D9D9D9",
            fg_color="white"
        )

        self.folder_card.pack(
            fill="x"
        )


        # ------------------------------
        # Header
        # ------------------------------

        header = ctk.CTkFrame(
            self.folder_card,
            fg_color="transparent"
        )

        header.pack(
            fill="x",
            padx=20,
            pady=(15,10)
        )

        header.grid_columnconfigure(0, weight=1)

        title = ctk.CTkLabel(
            header,
            text=" Selected Folder",

            image=icon_manager.get_icon(
                "buttons",
                "browse_folder",
                size=(22,22)
            ),

            compound="left",

            font=("Segoe UI",16,"bold")
        )

        title.grid(
            row=0,
            column=0,
            sticky="w"
        )

        self.browse_btn = ctk.CTkButton(
            header,
            text="Browse Folder",
            image=icon_manager.get_icon(
                "buttons",
                "browse_folder",
                size=(18,18)
            ),

            compound="left",
            width=140,
            command=self.controller.browse_folder
        )

        self.browse_btn.grid(
            row=0,
            column=1,
            sticky="e"
        )

        # ------------------------------
        # Folder Name
        # ------------------------------

        self.folder_name = ctk.CTkLabel(
            self.folder_card,
            text=" No Folder Selected",
            image=icon_manager.get_icon(
                "buttons",
                "browse_folder",
                size=(20,20)
            ),

            compound="left",
            font=("Segoe UI",18,"bold")
        )

        self.folder_name.pack(
            anchor="w",
            padx=20
        )

        # ------------------------------
        # Folder Path
        # ------------------------------

        self.folder_path_label = ctk.CTkLabel(
            self.folder_card,
            text="",
            font=("Segoe UI",11),
            text_color="gray40",
            anchor="w",
            justify="left",
            wraplength=350
        )

        self.folder_path_label.pack(
            anchor="w",
            padx=20,
            pady=(5,15)
        )

    