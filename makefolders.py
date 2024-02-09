"""
* * * * * * * * * *

Uses a tkinter prompt to ask you where you want to save your folders.

* * * * * * * * * *
"""

#libraries used for running this simple python script
import os
import calendar
from tkinter import Tk, filedialog

#function taking in arguments start year, month and location
def create_folders(start_year, start_month, location):
    current_year = start_year
    current_month = start_month

    #For loop checking for the month you select based on the number you select
    for month_num in range(1, 13):
        month_name = calendar.month_name[current_month]
        folder_name = os.path.join(location, f"{month_num:02d}_{month_name}_{current_year}")
        os.makedirs(folder_name) #makes the directory sets folder_name variable

        #sets the curent month and year
        current_month += 1
        if current_month > 12:
            current_month = 1
            current_year += 1

if __name__ == "__main__":
    start_year = int(input("Enter the starting year: "))
    start_month = int(input("Enter the starting month (1-12): "))

    #creates the tkinter window prompt
    root = Tk()
    root.withdraw()  # Hides the main tkinter window

    #location variable saves your folder where you want it located
    location = filedialog.askdirectory(title="Select a folder to create the structure")

    #run the function create_folders and prints out final message that folders were created successfully! 
    create_folders(start_year, start_month, location)
    print("Folders created successfully!")

"""
* * * * * * * * * *

Feel to contribute and make this program any simpler then this lol. 
Looking to create a simple GUI using PyQT in coming weeks. Might implement other functinoalities 

any ideas?

* * * * * * * * * *
"""
