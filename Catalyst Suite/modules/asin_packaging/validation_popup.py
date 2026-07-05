"""
=========================================================
CATALYST Suite
File      : validation_popup.py
Module    : ASIN Packaging Suite
Version   : 1.0.0
Author    : Srinath Jayakumar
Purpose   : Validation Results Popup
=========================================================
"""

import customtkinter as ctk

from tkinter import ttk


class ValidationPopup(ctk.CTkToplevel):

    def __init__(
        self,
        parent,
        controller,
        summary=None,
        results=None
    ):

        super().__init__(parent)

        self.controller = controller

        self.transient(parent)

        self.summary = summary or {}

        self.results = results or []

        self.title("Validation Results")

        self.geometry("820x500")

        self.resizable(True, True)

        self.minsize(700, 450)

        self.grab_set()

        self.focus()

        self.build_ui()

    def build_ui(self):

        # =====================================================
        # Main Container
        # =====================================================

        self.main_frame = ctk.CTkFrame(
            self,
            corner_radius=10
        )

        self.main_frame.pack(
            fill="both",
            expand=True,
            padx=20,
            pady=20
        )

        # =====================================================
        # Title
        # =====================================================

        self.title_label = ctk.CTkLabel(
            self.main_frame,
            text="Validation Results",
            font=("Segoe UI", 20, "bold")
        )

        self.title_label.pack(
            anchor="w",
            pady=(5, 20)
        )

        # =====================================================
        # Summary
        # =====================================================

        self.build_summary_section()

        # =====================================================
        # Validation Table
        # =====================================================

        self.build_validation_table()

        # =====================================================
        # Bottom Buttons
        # =====================================================

        self.build_bottom_buttons()

        self.load_summary()

        self.load_table()

        self.center_window()

    def build_summary_section(self):

        # =====================================================
        # Summary Card
        # =====================================================

        self.summary_frame = ctk.CTkFrame(
            self.main_frame,
            corner_radius=10
        )

        self.summary_frame.pack(
            fill="x",
            pady=(0, 20)
        )

        # -----------------------------------------------------
        # 3 Column Layout
        # -----------------------------------------------------

        self.summary_frame.grid_columnconfigure(0, weight=1)
        self.summary_frame.grid_columnconfigure(1, weight=1)
        self.summary_frame.grid_columnconfigure(2, weight=1)

        # -----------------------------------------------------
        # Total Folders
        # -----------------------------------------------------

        self.total_folders = ctk.CTkLabel(
            self.summary_frame,
            text="Folders : 0",
            font=("Segoe UI", 15, "bold")
        )

        self.total_folders.grid(
            row=0,
            column=0,
            padx=20,
            pady=15,
            sticky="w"
        )

        # -----------------------------------------------------
        # Total Images
        # -----------------------------------------------------

        self.total_images = ctk.CTkLabel(
            self.summary_frame,
            text="Images : 0",
            font=("Segoe UI", 15, "bold")
        )

        self.total_images.grid(
            row=0,
            column=1,
            padx=20,
            pady=15,
            sticky="w"
        )

        # -----------------------------------------------------
        # Excel Rows
        # -----------------------------------------------------

        self.total_rows = ctk.CTkLabel(
            self.summary_frame,
            text="Excel Rows : 0",
            font=("Segoe UI", 15, "bold")
        )

        self.total_rows.grid(
            row=0,
            column=2,
            padx=20,
            pady=15,
            sticky="w"
        )

        # -----------------------------------------------------
        # Matched
        # -----------------------------------------------------

        self.total_matched = ctk.CTkLabel(
            self.summary_frame,
            text="Matched : 0",
            font=("Segoe UI", 15, "bold"),
            text_color="#28A745"
        )

        self.total_matched.grid(
            row=1,
            column=0,
            padx=20,
            pady=(5,15),
            sticky="w"
        )

        # -----------------------------------------------------
        # Warnings
        # -----------------------------------------------------

        self.total_warnings = ctk.CTkLabel(
            self.summary_frame,
            text="Warnings : 0",
            font=("Segoe UI", 15, "bold"),
            text_color="#FFC107"
        )

        self.total_warnings.grid(
            row=1,
            column=1,
            padx=20,
            pady=(5,15),
            sticky="w"
        )

        # -----------------------------------------------------
        # Errors
        # -----------------------------------------------------

        self.total_errors = ctk.CTkLabel(
            self.summary_frame,
            text="Errors : 0",
            font=("Segoe UI", 15, "bold"),
            text_color="#DC3545"
        )

        self.total_errors.grid(
            row=1,
            column=2,
            padx=20,
            pady=(5,15),
            sticky="w"
        )

    def build_validation_table(self):

        # =====================================================
        # Table Frame
        # =====================================================

        self.table_frame = ctk.CTkFrame(
            self.main_frame,
            corner_radius=10
        )

        self.table_frame.pack(
            fill="both",
            expand=False,
            padx=5,
            pady=(0, 15)
        )

        # =====================================================
        # Treeview Style
        # =====================================================

        style = ttk.Style()

        style.theme_use("default")

        style.configure(
            "Treeview",
            rowheight=28,
            font=("Segoe UI", 10)
        )

        style.configure(
            "Treeview.Heading",
            font=("Segoe UI", 10, "bold")
        )


        # =====================================================
        # Treeview
        # =====================================================

        columns = (
            "folder",
            "row",
            "folder_color",
            "excel_color",
            "asin_count",
            "status",
            "remarks"
        )

        self.validation_tree = ttk.Treeview(
            self.table_frame,
            columns=columns,
            show="headings",
            height=12
        )

        # =====================================================
        # Row Colors
        # =====================================================

        self.validation_tree.tag_configure(
            "ready",
            background="#EAF7EA"
        )

        self.validation_tree.tag_configure(
            "warning",
            background="#FFF8DB"
        )

        self.validation_tree.tag_configure(
            "error",
            background="#FDECEC"
        )

        # =====================================================
        # Column Headings
        # =====================================================

        self.validation_tree.heading(
            "folder",
            text="Folder Name"
        )

        self.validation_tree.heading(
            "row",
            text="Excel Row"
        )

        self.validation_tree.heading(
            "folder_color",
            text="Folder Color"
        )

        self.validation_tree.heading(
            "excel_color",
            text="Excel Color"
        )

        self.validation_tree.heading(
            "asin_count",
            text="ASIN Count"
        )

        self.validation_tree.heading(
            "status",
            text="Status"
        )

        self.validation_tree.heading(
            "remarks",
            text="Remarks"
        )

        # =====================================================
        # Column Widths
        # =====================================================

        self.validation_tree.column(
            "folder",
            width=220,
            anchor="w",
            stretch=True
        )

        self.validation_tree.column(
            "row",
            width=90,
            anchor="center",
            stretch=False
        )

        self.validation_tree.column(
            "folder_color",
            width=130,
            anchor="center",
            stretch=False
        )

        self.validation_tree.column(
            "excel_color",
            width=130,
            anchor="center",
            stretch=False
        )

        self.validation_tree.column(
            "asin_count",
            width=90,
            anchor="center",
            stretch=False
        )

        self.validation_tree.column(
            "status",
            width=100,
            anchor="center",
            stretch=False
        )

        self.validation_tree.column(
            "remarks",
            width=170,
            anchor="w",
            stretch=True
        )

        # =====================================================
        # Vertical Scrollbar
        # =====================================================

        self.v_scrollbar = ctk.CTkScrollbar(
            self.table_frame,
            orientation="vertical",
            command=self.validation_tree.yview
        )

        self.validation_tree.configure(
            yscrollcommand=self.v_scrollbar.set
        )

        # =====================================================
        # Horizontal Scrollbar
        # =====================================================

        self.h_scrollbar = ctk.CTkScrollbar(
            self.table_frame,
            orientation="horizontal",
            command=self.validation_tree.xview
        )

        self.validation_tree.configure(
            xscrollcommand=self.h_scrollbar.set
        )

        # =====================================================
        # Layout
        # =====================================================

        self.validation_tree.pack(
            side="left",
            fill="both",
            expand=False
        )

        self.v_scrollbar.pack(
            side="right",
            fill="y"
        )

        self.h_scrollbar.pack(
            side="bottom",
            fill="x"
        )

    def build_bottom_buttons(self):

        self.bottom_frame = ctk.CTkFrame(
            self.main_frame,
            fg_color="transparent"
        )

        self.bottom_frame.pack(
            fill="x",
            pady=(10, 0)
        )

        # Export Button
        self.export_btn = ctk.CTkButton(
            self.bottom_frame,
            text="Export Validation Report",
            command=self.export_validation_report
        )

        self.export_btn.pack(
            side="left",
            padx=10
        )

        # Close Button
        self.close_btn = ctk.CTkButton(
            self.bottom_frame,
            text="Close",
            command=self.destroy
        )

        self.close_btn.pack(
            side="right",
            padx=10
        )

        # Start Packaging Button
        self.start_btn = ctk.CTkButton(
            self.bottom_frame,
            text="Start Packaging",
            command=self.start_packaging
        )

        self.start_btn.pack(
            side="right",
            padx=10
        )

    def center_window(self):

        parent = self.master

        parent.update_idletasks()

        # Fixed popup size
        width = 850
        height = 520

        parent_x = parent.winfo_rootx()
        parent_y = parent.winfo_rooty()

        parent_width = parent.winfo_width()
        parent_height = parent.winfo_height()

        x = parent_x + (parent_width - width) // 2
        y = parent_y + (parent_height - height) // 2

        self.geometry(f"{width}x{height}+{x}+{y}")

    def load_summary(self):

        self.total_folders.configure(
            text=f"Folders : {self.summary.get('folders', 0)}"
        )

        self.total_images.configure(
            text=f"Images : {self.summary.get('images', 0)}"
        )

        self.total_rows.configure(
            text=f"Excel Rows : {self.summary.get('excel_rows', 0)}"
        )

        self.total_matched.configure(
            text=f"Matched : {self.summary.get('matched',0)}"
        )

        self.total_warnings.configure(
            text=f"Warnings : {self.summary.get('warnings',0)}"
        )

        self.total_errors.configure(
            text=f"Errors : {self.summary.get('errors',0)}"
        )

    def load_table(self):

        for row in self.validation_tree.get_children():

            self.validation_tree.delete(row)

        for item in self.results:

            status = item["status"].lower()

            if status == "ready":
                tag = "ready"

            elif status == "warning":
                tag = "warning"

            else:
                tag = "error"

            self.validation_tree.insert(
                "",
                "end",
                values=(
                    item["folder"],
                    item["excel_row"],
                    item["folder_color"],
                    item["excel_color"],
                    item["asin_count"],
                    item["status"],
                    item["remarks"]
                ),
                tags=(tag,)
            )

    def start_packaging(self):

        self.destroy()

        self.controller.start_packaging(
            self.results
        )

    def export_validation_report(self):

        self.controller.export_validation_report(

            summary=self.summary,

            results=self.results

        )