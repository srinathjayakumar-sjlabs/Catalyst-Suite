"""
=========================================================
CATALYST Suite
File      : services.py
Module    : ASIN Packaging Suite
Version   : 1.0.0
Author    : Srinath Jayakumar
Purpose   : Validation & Packaging Business Logic
=========================================================
"""

import os
import pandas as pd
import shutil
from datetime import datetime
import zipfile


class AsinPackagingService:

    def __init__(self):
        pass

    # =====================================================
    # Normalize Text
    # =====================================================

    def normalize_text(self, value):

        if pd.isna(value):
            return ""

        return " ".join(
            str(value).strip().lower().split()
        )

    # =====================================================
    # Validate
    # =====================================================

    def validate(
        self,
        image_folder,
        excel_file
    ):

        # -------------------------------------------------
        # Read Excel
        # -------------------------------------------------

        try:

            df = pd.read_excel(excel_file)

        except Exception as e:

            return {

                "summary": {

                    "folders": 0,
                    "images": 0,
                    "excel_rows": 0,
                    "matched": 0,
                    "warnings": 0,
                    "errors": 1

                },

                "results": [

                    {

                        "folder": "",
                        "excel_row": "",
                        "folder_color": "",
                        "excel_color": "",
                        "asin_count": 0,
                        "status": "Error",
                        "remarks": str(e)

                    }

                ]

            }

        # -------------------------------------------------
        # Standardize Excel Columns
        # -------------------------------------------------

        df.columns = df.columns.str.strip()

        required_columns = [

            "Style",
            "Color",
            "ASIN"

        ]

        for column in required_columns:

            if column not in df.columns:

                raise ValueError(

                    f"Missing Required Column : {column}"

                )

        excel_rows = len(df)

        # -------------------------------------------------
        # Counters
        # -------------------------------------------------

        folder_count = 0

        image_count = 0

        matched = 0

        warnings = 0

        errors = 0

        results = []

        # -------------------------------------------------
        # Scan Image Folder
        # -------------------------------------------------

        for item in sorted(os.listdir(image_folder)):
            
            # Skip system folders

            if item.lower() in (
                "output",
                "compressed output",
                "reports"
            ):
                continue

            if item.startswith("."):
               continue

            item_path = os.path.join(
                image_folder,
                item
            )

            if not os.path.isdir(item_path):
                continue

            folder_count += 1

            image_total = 0

            for file in os.listdir(item_path):

                if file.lower().endswith(

                    (
                        ".jpg",
                        ".jpeg",
                        ".png",
                        ".webp",
                        ".bmp",
                        ".tif",
                        ".tiff",
                        ".avif"
                    )

                ):

                    image_total += 1

            image_count += image_total

            # -------------------------------------------------
            # Split Folder Name
            # -------------------------------------------------

            parts = item.split()

            if len(parts) < 2:

                errors += 1

                results.append(

                    {

                        "folder": item,

                        "excel_row": "-",

                        "folder_color": "-",

                        "excel_color": "-",

                        "asin_count": 0,

                        "asins": [],

                        "status": "Error",

                        "remarks": "Invalid Folder Name"

                    }

                )

                continue

            style = parts[0].strip()

            folder_color = " ".join(
                parts[1:]
            ).strip()

            # -------------------------------------------------
            # Match Style
            # -------------------------------------------------

            style_rows = df[
                df["Style"].astype(str).str.strip() == style
            ]

            if style_rows.empty:

                errors += 1

                results.append(

                    {

                        "folder": item,
                        "excel_row": "-",
                        "folder_color": folder_color,
                        "excel_color": "-",
                        "asin_count": 0,
                        "status": "Error",
                        "remarks": "Style Not Found"

                    }

                )

                continue

            # -------------------------------------------------
            # Match Color
            # -------------------------------------------------

            color_rows = style_rows[

                style_rows["Color"].apply(
                    self.normalize_text
                )

                ==

                self.normalize_text(
                    folder_color
                )

            ]

            if color_rows.empty:

                errors += 1

                results.append(

                    {

                        "folder": item,
                        "excel_row": "-",
                        "folder_color": folder_color,
                        "excel_color": "-",
                        "asin_count": 0,
                        "status": "Error",
                        "remarks": "Color Not Found"

                    }

                )

                continue

            # -------------------------------------------------
            # Duplicate Check
            # -------------------------------------------------

            matched += 1

            status = "Ready"

            remarks = f"{len(color_rows)} ASIN(s) Found"

            # -------------------------------------------------
            # Excel Row Range
            # -------------------------------------------------

            excel_row_numbers = list(
                color_rows.index + 2
            )

            if len(excel_row_numbers) == 1:

                excel_row = str(
                    excel_row_numbers[0]
                )

            else:

                excel_row = (

                    f"{excel_row_numbers[0]}"

                    f"-"

                    f"{excel_row_numbers[-1]}"

                )

            # -------------------------------------------------
            # ASIN Count
            # -------------------------------------------------

            asin_count = len(
                color_rows
            )

            # -------------------------------------------------
            # Store Result
            # -------------------------------------------------

            results.append(

                {

                    "folder": item,

                    "excel_row": excel_row,

                    "folder_color": folder_color,

                    "excel_color": color_rows.iloc[0]["Color"],

                    "asin_count": asin_count,

                    "asins": color_rows["ASIN"].tolist(),

                    "status": status,

                    "remarks": remarks

                }

            )

        # =====================================================
        # Validation Summary
        # =====================================================

        summary = {

            "folders": folder_count,

            "images": image_count,

            "excel_rows": excel_rows,

            "matched": matched,

            "warnings": warnings,

            "errors": errors

        }

        # =====================================================
        # Return Validation Result
        # =====================================================

        return {

            "summary": summary,

            "results": results

        }

    def package_asins(
        self,
        image_folder,
        results,
        log_callback,
        progress_callback
    ):

        print("=" * 60)
        print("PACKAGING ENGINE")
        print("=" * 60)

        output_folder = os.path.join(
            image_folder,
            "Output"
        )

        os.makedirs(
            output_folder,
            exist_ok=True
        )

        compressed_output_folder = os.path.join(
            image_folder,
            "Compressed Output"
        )

        os.makedirs(
           compressed_output_folder,
            exist_ok=True
        )

        print(f"Output Folder : {output_folder}")

        # -----------------------------------------
        # Progress Tracking
        # -----------------------------------------

        total_asins = sum(
            len(item["asins"])
            for item in results
            if item["status"] == "Ready"
        )

        processed_asins = 0

        for item in results:

            print("=" * 50)

            print(f'Folder : {item["folder"]}')

            log_callback(
                f"📁 Processing Folder : {item['folder']}"
            )

            print(f'ASIN Count : {item["asin_count"]}')

            # Skip invalid folders
            if item["status"] != "Ready":
                continue

            # Create one folder per ASIN
            source_folder = os.path.join(
                image_folder,
                item["folder"]
            )

            print(f"Source Folder : {source_folder}")
            print(os.listdir(source_folder))
    
            for asin in item["asins"]:

                asin_folder = os.path.join(
                    output_folder,
                    asin
                )

                os.makedirs(
                    asin_folder,
                    exist_ok=True
                )

                print(f"Created : {asin}")

                log_callback(
                    f"📦 Creating ASIN : {asin}"
                )

                # -----------------------------------------
                # Categorize Images
                # -----------------------------------------

                main_image = None

                front_image = None

                other_images = []

                for file in os.listdir(source_folder):

                    source_file = os.path.join(
                        source_folder,
                        file
                    )

                    if not os.path.isfile(source_file):
                        continue

                    filename = file.lower()

                    if "main" in filename:

                        main_image = file

                    elif "front" in filename:

                        front_image = file

                    else:

                        other_images.append(file)

                # -----------------------------------------
                # Copy MAIN Image
                # -----------------------------------------

                if main_image:

                    source_file = os.path.join(
                        source_folder,
                        main_image
                    )

                    destination_file = os.path.join(
                        asin_folder,
                        f"{asin}.MAIN.jpg"
                    )

                    shutil.copy2(
                        source_file,
                        destination_file
                    )

                    print(f"    Copied : {asin}.MAIN.jpg")

                    log_callback(
                        f"      ✔ {asin}.MAIN.jpg"
                    )

                # -----------------------------------------
                # Copy FRONT Image
                # -----------------------------------------

                pt_counter = 1

                if front_image:

                    source_file = os.path.join(
                        source_folder,
                        front_image
                    )

                    destination_file = os.path.join(
                        asin_folder,
                        f"{asin}.PT01.jpg"
                    )

                    shutil.copy2(
                        source_file,
                        destination_file
                    )

                    print(f"    Copied : {asin}.PT01.jpg")

                    log_callback(
                        f"      ✔ {asin}.PT01.jpg"
                    )

                    pt_counter = 2

                # -----------------------------------------
                # Copy Remaining Images
                # -----------------------------------------

                for image in sorted(other_images):

                    source_file = os.path.join(
                        source_folder,
                        image
                    )

                    destination_file = os.path.join(
                        asin_folder,
                        f"{asin}.PT{pt_counter:02d}.jpg"
                    )

                    shutil.copy2(
                        source_file,
                        destination_file
                    )

                    print(
                        f"    Copied : {asin}.PT{pt_counter:02d}.jpg"
                    )

                    log_callback(
                        f"      ✔ {asin}.PT{pt_counter:02d}.jpg"
                    )

                    pt_counter += 1

                zip_path = os.path.join(
                    compressed_output_folder,
                    f"{asin}.zip"
                )

                with zipfile.ZipFile(
                    zip_path,
                    "w",
                    zipfile.ZIP_DEFLATED
                ) as zipf:

                    for file in os.listdir(asin_folder):

                        file_path = os.path.join(
                            asin_folder,
                            file
                        )

                        zipf.write(
                            file_path,
                            arcname=file
                        )

                print(f"ZIP Created : {asin}.zip")

                log_callback(
                    f"      📦 ZIP Created : {asin}.zip"
                )
                
                processed_asins += 1

                progress_callback(
                    processed_asins,
                    total_asins,
                    asin
                )        

    def export_validation_report(
        self,
        image_folder,
        summary,
        results
    ):

        reports_folder = os.path.join(
            image_folder,
            "Reports"
        )

        os.makedirs(
            reports_folder,
            exist_ok=True
        )

        timestamp = datetime.now().strftime(
            "%Y-%m-%d_%H-%M-%S"
        )

        report_path = os.path.join(

            reports_folder,

            f"Validation_Report_{timestamp}.xlsx"

        )

        report_data = []

        for item in results:

            report_data.append(

                {

                    "Folder Name": item["folder"],

                    "Excel Row": item["excel_row"],

                    "Folder Color": item["folder_color"],

                    "Excel Color": item["excel_color"],

                    "ASIN Count": item["asin_count"],

                    "Status": item["status"],

                    "Remarks": item["remarks"]

                }

            )

        df = pd.DataFrame(report_data)

        df.to_excel(
            report_path,
            index=False
        )

        print("=" * 60)
        print("VALIDATION REPORT EXPORTED")
        print("=" * 60)
        print(f"Saved To : {report_path}")