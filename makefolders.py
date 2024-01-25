"""
* * * * * * * * * *

Uses a tkinter prompt to ask you where you want to save your folders.

* * * * * * * * * *
"""

import os
import calendar
from tkinter import Tk, filedialog

def create_folders(start_year, start_month, location):
    current_year = start_year
    current_month = start_month

    for month_num in range(1, 13):
        month_name = calendar.month_name[current_month]
        folder_name = os.path.join(location, f"{month_num:02d}_{month_name}_{current_year}")
        os.makedirs(folder_name)

        current_month += 1
        if current_month > 12:
            current_month = 1
            current_year += 1

if __name__ == "__main__":
    start_year = int(input("Enter the starting year: "))
    start_month = int(input("Enter the starting month (1-12): "))
    
    root = Tk()
    root.withdraw()  # Hide the main tkinter window

    location = filedialog.askdirectory(title="Select a folder to create the structure")
    
    create_folders(start_year, start_month, location)
    print("Folders created successfully!")
