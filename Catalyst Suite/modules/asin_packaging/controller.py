"""
=========================================================
CATALYST Suite
File      : controller.py
Module    : ASIN Packaging Suite
Version   : 1.0.0
Author    : Srinath Jayakumar
Purpose   : ASIN Packaging Controller
=========================================================
"""

from modules.asin_packaging.services import AsinPackagingService
from modules.asin_packaging.validation_popup import ValidationPopup

class AsinPackagingController:

    def __init__(self, ui):

        self.ui = ui

        self.service = AsinPackagingService()

    def browse_folder(self):

        from tkinter import filedialog
        import os

        folder = filedialog.askdirectory(
            title="Select Image Folder"
        )

        if not folder:
            return

        self.image_folder = folder

        folder_name = os.path.basename(folder)

        self.ui.reset_packaging_state()

        self.ui.selected_folder_label.configure(
            text=folder_name
        )

        self.ui.add_log(
            f"📂 Image Folder Selected : {folder_name}"
        )

    def browse_excel(self):

        from tkinter import filedialog
        import os

        excel = filedialog.askopenfilename(
            title="Select Excel Mapping File",
            filetypes=[
                ("Excel Files", "*.xlsx *.xls")
            ]
        )

        if not excel:
            return

        self.excel_file = excel

        excel_name = os.path.basename(excel)

        self.ui.reset_packaging_state()

        self.ui.selected_excel_label.configure(
            text=excel_name
        )

        self.ui.add_log(
            f"📄 Excel Mapping Selected : {excel_name}"
        )
        
    def validate(self):

        # -----------------------------------------------------
        # Validation Started
        # -----------------------------------------------------

        self.ui.clear_log()

        self.ui.add_log(
            "🔍 Starting Validation..."
        )

        # -----------------------------------------------------
        # Check Image Folder
        # -----------------------------------------------------

        if not hasattr(self, "image_folder"):

            self.ui.add_log(
                "❌ Please select the Image Folder."
            )

            return

        # -----------------------------------------------------
        # Check Excel File
        # -----------------------------------------------------

        if not hasattr(self, "excel_file"):

            self.ui.add_log(
                "❌ Please select the Excel Mapping file."
            )

            return

        # -----------------------------------------------------
        # Call Service
        # -----------------------------------------------------

        validation = self.service.validate(
            self.image_folder,
            self.excel_file
        )

        summary = validation["summary"]

        results = validation["results"]

        self.ui.folders_found_label.configure(
            text=f"Folders Found : {summary['folders']}"
        )

        self.ui.images_found_label.configure(
            text=f"Images Found : {summary['images']}"
        )

        self.ui.add_log(
            "✅ Validation Completed."
        )

        popup = ValidationPopup(
            parent=self.ui,
            controller=self,
            summary=summary,
            results=results
        )

        popup.focus()

        # Placeholder
        # Actual packaging workflow will be implemented later.


    def stop_packaging(self):

        self.ui.add_log(
            "⛔ Packaging Stopped."
        )

    def start_packaging(
        self,
        results
    ):

        self.ui.reset_packaging_state()

        self.ui.add_log(
            "🚀 Packaging Started..."
        )

        print("Packaging Started")

        print(f"Folders received : {len(results)}")

        self.service.package_asins(
            image_folder=self.image_folder,
            results=results,
            log_callback=self.ui.add_log,
            progress_callback=self.ui.update_progress
        )

        # -----------------------------------------
        # Packaging Completed
        # -----------------------------------------

        self.ui.progress_label.configure(
            text="✔ Packaging Completed"
        )

        self.ui.add_log(
            "========================================"
        )

        self.ui.add_log(
            "✅ Packaging Completed Successfully"
        )

        self.ui.add_log(
            f"📁 Folders Processed : {len(results)}"
        )

        total_asins = sum(
            len(item["asins"])
            for item in results
            if item["status"] == "Ready"
        )

        self.ui.add_log(
            f"📦 ASINs Created : {total_asins}"
        )

        self.ui.add_log(
            f"🗜 ZIP Files Created : {total_asins}"
        )

        self.ui.add_log(
            "========================================"
        )

    def export_validation_report(
        self,
        summary,
        results
    ):

        self.service.export_validation_report(

            image_folder=self.image_folder,

            summary=summary,

            results=results

        )
