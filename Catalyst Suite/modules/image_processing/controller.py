"""
=========================================================
CATALYST Suite
Image Processing Controller
Version : 1.0.0
=========================================================
"""

from tkinter import filedialog, messagebox

from modules.image_processing.services import ImageProcessingService

import threading


class ImageProcessingController:

    def __init__(self, ui):

        self.ui = ui
        self.selected_folder = None
        self.service = ImageProcessingService()

    # -----------------------------------------------------

    def browse_folder(self):

        folder = filedialog.askdirectory(
            title="Select Image Folder"
        )

        if folder:
            self.selected_folder = folder

            self.ui.update_folder_path(folder)

            self.ui.add_log(f"📂 Folder Selected : {folder}")

            print(f"Selected Folder: {folder}")

    # -----------------------------------------------------

    def start_processing(self):

        if not self.selected_folder:

            print("No folder selected.")
            return

        import os

        print("Starting Image Processing...")

        files = os.listdir(self.selected_folder)

        image_files = [
            file
            for file in files
            if self.service.is_supported_image(file)
        ]

        print(f"Images Found: {len(image_files)}")

        self.ui.add_log(f"🖼 Images Found : {len(image_files)}")

        self.ui.progress.set(0)

        self.ui.clear_log()

        self.ui.add_log("▶ Processing Started")

        self.ui.progress_label.configure(
            text="Starting..."
        )

        self.service.stop_requested = False

        self.ui.start_btn.configure(state="disabled")

        thread = threading.Thread(
            target=self.run_processing,
            daemon=True
        )

        thread.start()

    def stop_processing(self):

        self.service.stop_requested = True

        self.ui.add_log("⛔ Stop Requested")

        self.ui.progress_label.configure(
            text="Stopping after current image..."
        )


    def run_processing(self):

        processed = self.service.process_folder(
            self.selected_folder,
            progress_callback=self.ui.update_progress,
            log_callback=self.ui.add_log
        )

        self.ui.add_log(f"✅ Processing Completed ({processed} Images)")        

        print(f"\nSuccessfully Processed: {processed} images")

        self.ui.progress_label.configure(
            text=f"Completed ({processed} Images)"
        )

        messagebox.showinfo(
            "Processing Completed",
            f"Successfully processed\n\n{processed} images."
        )

        self.ui.start_btn.configure(state="normal")