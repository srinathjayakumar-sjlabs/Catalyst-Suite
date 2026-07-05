"""
=========================================================
CATALYST Suite
File      : services.py
Version   : 1.0.0
Author    : Srinath Jayakumar
Purpose   : Image Processing Business Logic
=========================================================
"""

from PIL import Image

import pillow_avif

from modules.image_processing.background_remover import BackgroundRemover

MIN_W = 660
MIN_H = 880

MAX_W = 1200
MAX_H = 1600


class ImageProcessingService:

    def __init__(self):
        self.bg_remover = BackgroundRemover()

        self.stop_requested = False

    def resize_image(self, img):
        """
        Resize only if the image is smaller than the minimum size.
        Never reduce the size of larger images.
        Preserve aspect ratio.
        """

        w, h = img.size

        # Already meets minimum size
        if w >= MIN_W and h >= MIN_H:
            return img

        # Calculate scale required to reach minimum
        scale = max(
            MIN_W / w,
            MIN_H / h
        )

        new_w = int(w * scale)
        new_h = int(h * scale)

        img = img.resize(
            (new_w, new_h),
            Image.Resampling.LANCZOS
        )

        return img


    def is_supported_image(self, filename):
        """
        Check whether a file is a supported image.
        """

        supported_extensions = (
            ".jpg",
            ".jpeg",
            ".png",
            ".webp",
            ".bmp",
            ".tif",
            ".tiff",
            ".avif"
        )

        return filename.lower().endswith(supported_extensions)

    def load_and_resize_image(self, image_path):
        """
        Open an image and resize it.
        """

        img = Image.open(image_path)

        original_size = img.size

        img = self.resize_image(img)

        resized_size = img.size

        return original_size, resized_size

     
    def count_total_images(self, folder_path):
        """
        Count all supported images inside a folder and its subfolders.
        """

        import os

        total = 0

        for root, _, files in os.walk(folder_path):
            for file in files:
                if self.is_supported_image(file):
                    total += 1

        return total


    def process_single_folder(
        self,
        folder_path,
        progress_callback=None,
        log_callback=None,
        progress_state=None
    ):

        import os

        output_folder = os.path.join(folder_path, "Processed")
        os.makedirs(output_folder, exist_ok=True)

        processed = 0
        failed = 0

        image_files = [
            f for f in os.listdir(folder_path)
            if self.is_supported_image(f)
        ]

        total_images = len(image_files)

        for filename in image_files:

            try:

                if self.stop_requested:
                    print("Processing stopped by user.")
                    break

                image_path = os.path.join(folder_path, filename)

                if log_callback:
                    log_callback(f"🖼 Processing : {filename}")
                    log_callback("📂 Loading Image...")

                img = self.bg_remover.load_image(image_path)

                if log_callback:
                    log_callback("📏 Checking Image Size...")

                img = self.resize_image(img)

                base_name = os.path.splitext(filename)[0]

                if "main" in filename.lower():

                    original_save = os.path.join(output_folder, f"{base_name}.jpg")

                    if log_callback:
                        log_callback("💾 Saving Original JPG...")

                    img.save(original_save, "JPEG", quality=100, subsampling=0, optimize=False)

                    if log_callback:
                        log_callback("✂ Removing Background...")

                    bg_removed = self.bg_remover.remove_background(img.copy())

                    amazon_save = os.path.join(output_folder, f"{base_name}_Amazon.jpg")

                    if log_callback:
                        log_callback("💾 Saving Amazon JPG...")

                    bg_removed.save(amazon_save, "JPEG", quality=100, subsampling=0, optimize=False)

                else:

                    save_path = os.path.join(output_folder, f"{base_name}.jpg")

                    if log_callback:
                        log_callback("💾 Saving JPG...")

                    img.save(save_path, "JPEG", quality=100, subsampling=0, optimize=False)

                processed += 1

                if progress_state is not None:
                    progress_state["processed"] += 1
                    overall = progress_state["processed"]
                    total = progress_state["total"]
                else:
                    overall = processed
                    total = total_images

                if log_callback:
                    log_callback(f"✅ Completed : {filename}")

                if progress_callback:
                    progress_callback(overall, total, filename)

            except Exception as e:

                failed += 1

                if log_callback:
                    log_callback(f"❌ Failed : {filename}")
                    log_callback(f"⚠ Reason : {str(e)}")

        if log_callback:
            log_callback("")
            log_callback("━━━━━━━━━━━━━━━━━━━━━━━━")
            log_callback(f"✅ Success : {processed}")
            log_callback(f"❌ Failed  : {failed}")
            log_callback("━━━━━━━━━━━━━━━━━━━━━━━━")

        return processed


    def process_folder(
        self,
        folder_path,
        progress_callback=None,
        log_callback=None
    ):

        import os

        image_files = [
            f for f in os.listdir(folder_path)
            if os.path.isfile(os.path.join(folder_path, f))
            and self.is_supported_image(f)
        ]

        total_processed = 0

        progress_state = {
            'total': self.count_total_images(folder_path),
            'processed': 0
        }

        # Selected folder contains images
        if image_files:
            return self.process_single_folder(
                folder_path,
                progress_callback,
                log_callback,
                progress_state
            )

        # Selected folder contains subfolders
        for item in os.listdir(folder_path):

            subfolder = os.path.join(folder_path, item)

            if not os.path.isdir(subfolder):
                continue

            print(f"\nProcessing Folder : {item}")

            if log_callback:
                log_callback(f"📂 Folder : {item}")

            total_processed += self.process_single_folder(
                subfolder,
                progress_callback,
                log_callback,
                progress_state
            )

            if self.stop_requested:
                break

        self.stop_requested = False
        return total_processed