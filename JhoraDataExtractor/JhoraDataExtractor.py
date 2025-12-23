'''

This script is not optimized  for large amount of data, use it wisely.

This was for made for short, simple, personal use and not for large scaled applications 

'''

import os
import sys
import csv
import tkinter as tk
from tkinter import filedialog,messagebox
# import pandas as pd

#Global Variables
processed_list = []
files_to_be_processed = []
path = ""
csv_path_for_excel = ""
total_files = 0
skipped_files = 0

def AskfilePath():
    global path
    root = tk.Tk()
    root.withdraw()

    folder_path = filedialog.askdirectory(title="Select the folder containing your Jhora files (.jhd)")

    if folder_path:

        path = folder_path
        # print(f'The folder is set to {path}')
    else:
        messagebox.showwarning(
            title="No Folder Selected",
            message="No folder path was selected. The program will exit."
        )
        # sys.exit()

#Validation Check
def valid_check(filepath):
    global total_files
    global skipped_files
    count = 0
    skip_count = 0
    for file in os.listdir(filepath):
        if file.lower().endswith(".jhd"):
            files_to_be_processed.append(file)
            count+=1
        else: 
            skip_count+=1
    total_files = count
    skipped_files = skip_count
    # print(f"{count} valid file(s) found")
    # print(f"{skip_count} invalid file(s) skipped")

'''
# Previews
def file_preview(folder_path):
    count = 0
    print('Top 5 files previews :\n')

    for file in os.listdir(folder_path):
        print(file)
        count += 1
        if count == 5:
            break
    print('\n')
'''

def load_existing_names(csv_path):
    if not os.path.exists(csv_path):
        return set()
    existing = set()
    with open(csv_path, "r", encoding="utf-8") as f:
        reader = csv.reader(f)
        next(reader, None)  # skip header
        for row in reader:
            if row:
                existing.add(row[0])  # person_name is first column
    return existing

def batch_processor(file_list):
    global csv_path_for_excel
    csv_path = os.path.join(path, "1Extracted_details.csv")
    csv_path_for_excel  = csv_path
    existing = load_existing_names(csv_path)

    new_files = [f for f in file_list if f.replace(".jhd", "") not in existing]

    if len(new_files) == 0:
        messagebox.showinfo(
            title="No New Records",
            message="All .jhd files were already processed. Nothing new to extract."
        )
        # sys.exit()
    for file in new_files:
        Data_extractor(file)

    export_to_csv(processed_list, csv_path)


def Data_extractor(file):

    person_name = file.replace('.jhd','')

    open_file = open(os.path.join(path, file))
    line = open_file.readlines()

    data = [str.strip(value) for value in line]
    data.insert(0,person_name)
    open_file.close()

    processed_list.append(data)

# def csv_to_excel(csv_path):
#     excel_path = os.path.splitext(csv_path)[0] + ".xlsx"
#     df = pd.read_csv(csv_path)
#     # Sort by name
#     df.sort_values("Name", inplace=True)
#     df.to_excel(excel_path, index=False)

def export_to_csv(data, csv_path):
    file_exists = os.path.exists(csv_path)

    header = ["Name", "Month", "Day", "Year", "Time", "Timezone", "Longitude", "Latitude", 
              "Value1", "Value2", "Value3", "Value4", "Value5", "City_Name", "Country",
              "Value6", "Atmospheric pressure", "Temperature", "Gender"]

    with open(csv_path, "a", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)

        if not file_exists:
            writer.writerow(header)

        writer.writerows(data)

    messagebox.showinfo(
        title="Done",
        message=f"Processed {len(data)} new files. Appended to existing CSV."
    )

# Main run Script

AskfilePath()
valid_check(path)
# file_preview(path)
batch_processor(files_to_be_processed)
# csv_to_excel(csv_path_for_excel)
sys.exit()
