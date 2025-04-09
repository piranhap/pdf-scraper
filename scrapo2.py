# modules
import os
from pathlib import Path

"""
Steps for second iteration. 

Ask the user the directory where the pdfs are stored. (Ex: "C:\Users\user\Documents\pdfs")

Ask the user what is the naming conventions for the pdfs.(Ex: person*1*.pdf, where ** is the delimeter of the dynamic value for the naming convention)

Do a wget or curl? on the website to get fake info from ppl, and download that as a pdf?

Ask how many fake ppl the user wants, do that amount of requests to get the pdfs.
    Make sure to not be spotted as a bot on the website, so take random amount of time to make the requests.

Scan for headers or ask the user if they want to input their own headers.
    If the user gives their own headers use pdfquery using the LTTextBoxtHorizontal:contains("$word"), see if it finds something, ask the user if that is what he wants.

    If the user asks to scan for headers, scan them (How?)

Make a preview with the First PDF showing an ASCII table with the headers and the scraped information. 
    If correct, scrape them all, export
    IF not, how to solve or correct?

Put everything on a csv or excel.


"""

# Ask the user the directory where the pdfs are stored. (Ex: "C:\Users\user\Documents\pdfs")
def pdf_directory():
    while True:
        dir_path = input("Enter the directory path that contains the pdfs: ")
        if os.path.isdir(dir_path):
            return Path(dir_path)
        else:
            print("[red] Invalid directory Path, make sure it is the full path [/red]")

def naming_convention():
    conv = input("Enter the PDF naming convention (e.g., person*1*.pdf)")
    
