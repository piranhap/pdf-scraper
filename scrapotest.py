from pdfquery import PDFQuery
import re

pdf = PDFQuery('p1.pdf')
pdf.load()

# Extract the raw text for the driver's license
drivers_license_raw = pdf.pq('LTTextBoxHorizontal:in_bbox("101.285, 194.911, 333.921, 202.411")').text()

# Debug: Print the raw text before cleaning
print(f"Raw Driver's License Text (before cleaning): '{drivers_license_raw}'")

# Clean up the extracted text
drivers_license_raw = drivers_license_raw.strip()  # Remove leading/trailing whitespace

# Debug: Print the cleaned text
print(f"Raw Driver's License Text (after cleaning): '{drivers_license_raw}'")

# Use regular expressions to extract the required parts
license_match = re.match(
    r"(?P<number>[A-Z0-9\-]+)\s*-\s*issued in\s*(?P<state>.+?)\s*on\s*(?P<issued_date>\d{2}/\d{2}/\d{4})",
    drivers_license_raw
)

if license_match:
    drivers_license_n = license_match.group("number")  # Extract the license number
    drivers_license_state = license_match.group("state")  # Extract the state
    drivers_license_issued_date = license_match.group("issued_date")  # Extract the issued date
else:
    drivers_license_n = None
    drivers_license_state = None
    drivers_license_issued_date = None
    print("Error: Could not match the driver's license text.")

# Print the extracted values for debugging
print(f"Driver's License Number: {drivers_license_n}")
print(f"Driver's License State: {drivers_license_state}")
print(f"Driver's License Issued Date: {drivers_license_issued_date}")