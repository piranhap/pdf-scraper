################################
# imports and variables
################################
from pdfquery import PDFQuery
import re
import pandas as pd


pdf = PDFQuery('p1.pdf')
pdf.load()

################################

#Data Collection 

################################

gender = pdf.pq('LTTextBoxHorizontal:in_bbox("101.285, 496.411, 117.541, 503.911")').text()
m_name = pdf.pq('LTTextBoxHorizontal:in_bbox("101.285, 470.911, 120.321, 478.411")').text()
l_name = pdf.pq('LTTextBoxHorizontal:in_bbox("101.285, 458.161, 130.465, 465.661")').text()
f_name = pdf.pq('LTTextBoxHorizontal:in_bbox("101.285, 483.661, 124.349, 491.161")').text()
initials = pdf.pq('LTTextBoxHorizontal:in_bbox("101.285, 445.411, 127.271, 452.911")').text()
maiden_name = pdf.pq('LTTextBoxHorizontal:in_bbox("101.285, 432.661, 120.46, 440.161")').text()
bday = pdf.pq('LTTextBoxHorizontal:in_bbox("101.285, 411.661, 199.548, 419.161")').text()
b_place = pdf.pq('LTTextBoxHorizontal:in_bbox("101.285, 398.911, 173.802, 406.411")').text()
z_sign = pdf.pq('LTTextBoxHorizontal:in_bbox("101.285, 386.161, 125.041, 393.661")').text()
uname = pdf.pq('LTTextBoxHorizontal:in_bbox("101.285, 373.411, 131.307, 380.911")').text()
passwd = pdf.pq('LTTextBoxHorizontal:in_bbox("101.285, 360.661, 137.562, 368.161")').text()
p_hashmd5 = pdf.pq('LTTextBoxHorizontal:in_bbox("101.285, 347.911, 229.323, 355.411")').text()
p_hashsha1 = pdf.pq('LTTextBoxHorizontal:in_bbox("101.285, 326.911, 257.961, 334.411")').text()
email = pdf.pq('LTTextBoxHorizontal:in_bbox("101.285, 305.911, 263.139, 313.411")').text().rstrip()
# email_link = pdf.pq('LTTextBoxHorizontal:in_bbox("")') # This one needs to be found differently, to look for the mailinator domain or something like that
phone = pdf.pq('LTTextBoxHorizontal:in_bbox("101.285, 293.161, 147.992, 300.661")').text()
address = pdf.pq('LTTextBoxHorizontal:in_bbox("101.285, 280.411, 266.242, 287.911")').text()
ssn = pdf.pq('LTTextBoxHorizontal:in_bbox("101.285, 254.911, 226.764, 262.411")').text()


drivers_license_raw = pdf.pq('LTTextBoxHorizontal:contains("issued in")').text()

# Extract from drivers_license_raw
license_match = re.findall(
    r"(?P<number>[A-Z0-9\-]+) - issued in(?P<state>[A-Za-z\s]+\([A-Z]{2}\)) on (?P<issued_date>\d{2}/\d{2}/\d{4})",
    drivers_license_raw
)
# if license match occurs, assign it 
if license_match:
    for match in license_match:
        drivers_license_n = match[0] # license number
        drivers_license_state = match[1] # state
        drivers_license_issued_date = match[2] # issued date
else:
    print("Error: could not find drivers license info")



drivers_license_exp_date = pdf.pq('LTTextBoxHorizontal:in_bbox("101.285, 186.661, 138.822, 194.161")').text()
car_model= pdf.pq('LTTextBoxHorizontal:in_bbox("101.285, 173.911, 166.734, 181.411")').text()


car_plate_raw = pdf.pq('LTTextBoxHorizontal:contains("issued in")').text()

# Extract from car_plate_raw
car_match = re.findall(
    r"(?P<platenumber>[A-Z0-9\-]+) - issued in (?P<state_issued>[A-Za-z\s]+(?:\s\([A-Z]{2}\))?) in year (?P<date_issued>\d{4})",
    car_plate_raw
)

if car_match:
    for match in car_match:
        car_plate_number = match[0] # plate number
        car_plate_state_issued = match[1] # state
        car_plate_date_issued = match[2] # issued date
else:
    print("Error: could not find drivers license info")


hair_color = pdf.pq('LTTextBoxHorizontal:in_bbox("31.5, 126.661, 110.067, 134.161")').text().split(sep=" ", maxsplit=2)
text1, text2, color = hair_color
hair_color = color


eyes_color = pdf.pq('LTTextBoxHorizontal:in_bbox("31.5, 113.911, 117.984, 121.411")').text().split(sep=" ", maxsplit=2)
text1, text2, e_color = eyes_color
eyes_color = e_color


height = pdf.pq('LTTextBoxHorizontal:in_bbox("73.395, 101.161, 128.839, 108.661")').text()
weight = pdf.pq('LTTextBoxHorizontal:in_bbox("73.395, 88.411, 138.448, 95.911")').text()

shoe_size = pdf.pq('LTTextBoxHorizontal:in_bbox("31.5, 75.661, 83.821, 83.161")').text().split(sep=" ", maxsplit=2)
text1, text2, size = shoe_size
shoe_size = size

blood_type = pdf.pq('LTTextBoxHorizontal:in_bbox("31.5, 62.911, 250.488, 70.411")').text()
guid = pdf.pq('LTTextBoxHorizontal:in_bbox("399.539, 222.661, 581.243, 230.161")').text()
uniqid = pdf.pq('LTTextBoxHorizontal:in_bbox("399.539, 209.911, 518.734, 217.411")').text()

mtcn = pdf.pq('LTTextBoxHorizontal:in_bbox("461.812, 175.411, 581.243, 182.911")').text().split()
text1, text2, text3, num = mtcn
mtcn = num

mtcn_mg = pdf.pq('LTTextBoxHorizontal:in_bbox("539.531, 162.661, 572.9, 170.161")').text()
credit_score_fico = pdf.pq('LTTextBoxHorizontal:in_bbox("562.898, 128.161, 575.412, 135.661")').text()
credit_score_exp = pdf.pq('LTTextBoxHorizontal:in_bbox("562.898, 115.411, 581.246, 122.911")').text()
credit_score_equi = pdf.pq('LTTextBoxHorizontal:in_bbox("562.898, 102.661, 581.246, 110.161")').text()
credit_score_vant = pdf.pq('LTTextBoxHorizontal:in_bbox("562.898, 89.911, 575.815, 97.411")').text()
credit_score_nextgen = pdf.pq('LTTextBoxHorizontal:in_bbox("562.898, 77.161, 575.412, 84.661")').text()

credit_score_sbss = pdf.pq('LTTextBoxHorizontal:in_bbox("405.434, 64.411, 575.412, 71.911")').text().split()
text1, text2, text3, text4, text5, text6, score = credit_score_sbss
credit_score_sbss = score

religion = pdf.pq('LTTextBoxHorizontal:in_bbox("111.035, 752.161, 138.131, 759.661")').text()
political_side = pdf.pq('LTTextBoxHorizontal:in_bbox("111.035, 739.411, 143.544, 746.911")').text()
f_color = pdf.pq('LTTextBoxHorizontal:in_bbox("111.035, 726.661, 124.794, 734.161")').text()

f_food = pdf.pq('LTTextBoxHorizontal:in_bbox("31.5, 713.911, 144.807, 721.411")').text().split()
text1, text2, text3, food = f_food
f_food = food

f_cereal = pdf.pq('LTTextBoxHorizontal:in_bbox("111.035, 701.161, 180.22, 708.661")').text()
f_season = pdf.pq('LTTextBoxHorizontal:in_bbox("111.035, 688.411, 132.715, 695.911")').text()
f_animal = pdf.pq('LTTextBoxHorizontal:in_bbox("111.035, 675.661, 125.9, 683.161")').text()
l_number = pdf.pq('LTTextBoxHorizontal:in_bbox("111.035, 662.911, 115.206, 670.411")').text()
ptin = pdf.pq('LTTextBoxHorizontal:in_bbox("194.555, 628.411, 232.926, 635.911")').text()
temp_ptin = pdf.pq('LTTextBoxHorizontal:in_bbox("194.555, 615.661, 232.926, 623.161")').text()
ein = pdf.pq('LTTextBoxHorizontal:in_bbox("194.555, 602.911, 232.095, 610.411")').text()

itin = pdf.pq('LTTextBoxHorizontal:in_bbox("31.5, 590.161, 231.538, 597.661")').text().split()
text1, text2, text3, text4, text5, itin_n = itin
itin = itin_n

atin = pdf.pq('LTTextBoxHorizontal:in_bbox("31.5, 577.411, 232.095, 584.911")').text().split()
text1, text2, text3, text4, text5, atin_n = atin
atin = atin_n

alignment = pdf.pq('LTTextBoxHorizontal:in_bbox("31.5, 542.911, 105.2, 550.411")').text().split(maxsplit=1)
text1, align_raw = alignment
alignment = align_raw

dnd_traits = pdf.pq('LTTextBoxHorizontal:contains("Charisma")').text().split()
charm, dnd_charm, const, dnd_const, dext, dnd_dext, inte, dnd_int, stren, dnd_str, wis, dnd_wise = dnd_traits

##########################

# Assigning collected data to a value to print

##########################

scraped_data = {
    "gender": gender,
    "first_name": f_name,
    "middle_name": m_name,
    "last_name": l_name,
    "initials": initials,
    "maiden_name": maiden_name,
    "birthday": bday,
    "birthplace": b_place,
    "zodiac_sign": z_sign,
    "username": uname,
    "password": passwd,
    "password_hash_md5": p_hashmd5,
    "password_hash_sha1": p_hashsha1,
    "email": email,
    "phone": phone,
    "address": address,
    "ssn": ssn,
    "drivers_license_number": drivers_license_n,
    "drivers_license_state": drivers_license_state,
    "drivers_license_issued_date": drivers_license_issued_date,
    "drivers_license_exp_date": drivers_license_exp_date,
    "car_model": car_model,
    "car_plate_number": car_plate_number,
    "car_plate_state_issued": car_plate_state_issued,
    "car_plate_date_issued": car_plate_date_issued,
    "hair_color": hair_color,
    "eyes_color": eyes_color,
    "height": height,
    "weight": weight,
    "shoe_size": shoe_size,
    "blood_type": blood_type,
    "guid": guid,
    "uniqid": uniqid,
    "mtcn": mtcn,
    "mtcn_mg": mtcn_mg,
    "credit_score_fico": credit_score_fico,
    "credit_score_exp": credit_score_exp,
    "credit_score_equi": credit_score_equi,
    "credit_score_vant": credit_score_vant,
    "credit_score_nextgen": credit_score_nextgen,
    "credit_score_sbss": credit_score_sbss,
    "religion": religion,
    "political_side": political_side,
    "favorite_color": f_color,
    "favorite_food": f_food,
    "favorite_cereal": f_cereal,
    "favorite_season": f_season,
    "favorite_animal": f_animal,
    "lucky_number": l_number,
    "ptin": ptin,
    "temp_ptin": temp_ptin,
    "ein": ein,
    "itin": itin,
    "atin": atin,
    "alignment": alignment,
    "dnd_charm": dnd_charm,
    "dnd_const": dnd_const,
    "dnd_dext": dnd_dext,
    "dnd_int": dnd_int,
    "dnd_str": dnd_str,
    "dnd_wise": dnd_wise,
}

#for key, value in scraped_data.items(): to print stuff to see if it grabs it
#   print(f"{value}")

# Headers for the spreadsheet
headers = [
    "Gender", "First Name", "Middle Name", "Last Name", "Initials", "Mother's maiden name",
    "Birthday", "Birthplace", "Zodiacal Sign", "Username", "Password", "Password Hash (MD5)",
    "Password Hash (SHA1)", "E-mail", "Phone", "Address", "SSN (2141123212) - issued in maryland",
    "Drivers License Number", "Drivers License State issued", "Drivers License issued date",
    "Drivers License exp date", "Car", "Car License Plate Number", "Car License Plate state issued",
    "Car License Plate date issued", "Hair Color", "Eyes Color", "Height", "Weight", "Shoe Size",
    "Blood Type", "GUID", "UniqID", "Western Union MTCN", "MoneyGram MTCN", "FICO Credit Score",
    "Experian", "Equifax", "Vantage Score", "FICO NextGen Risk Score",
    "FICO Small Business Scoring Service(SBSS)", "Religion", "Political side", "Favorite Color",
    "Favorite comfort food", "Favorite Cereal", "Favorite Season", "Favorite Animal",
    "Lucky number", "Preparer Tax Identification Number (PTIN)", "Interim PTIN (temporary PTIN)",
    "Employer Identification Number (EIN)", "Individual Taxpayer Identification Number (ITIN)",
    "Adoption Taxpayer Identification Number (ATIN)", "Alignment", "Charisma", "Constitution",
    "Dexterity", "Intelligence", "Strength", "Wisdom"
]

# Map the scraped data to the headers
data = [
    scraped_data.get("gender", ""),
    scraped_data.get("first_name", ""),
    scraped_data.get("middle_name", ""),
    scraped_data.get("last_name", ""),
    scraped_data.get("initials", ""),
    scraped_data.get("maiden_name", ""),
    scraped_data.get("birthday", ""),
    scraped_data.get("birthplace", ""),
    scraped_data.get("zodiac_sign", ""),
    scraped_data.get("username", ""),
    scraped_data.get("password", ""),
    scraped_data.get("password_hash_md5", ""),
    scraped_data.get("password_hash_sha1", ""),
    scraped_data.get("email", ""),
    scraped_data.get("phone", ""),
    scraped_data.get("address", ""),
    scraped_data.get("ssn", ""),
    scraped_data.get("drivers_license_number", ""),
    scraped_data.get("drivers_license_state", ""),
    scraped_data.get("drivers_license_issued_date", ""),
    scraped_data.get("drivers_license_exp_date", ""),
    scraped_data.get("car_model", ""),
    scraped_data.get("car_plate_number", ""),
    scraped_data.get("car_plate_state_issued", ""),
    scraped_data.get("car_plate_date_issued", ""),
    scraped_data.get("hair_color", ""),
    scraped_data.get("eyes_color", ""),
    scraped_data.get("height", ""),
    scraped_data.get("weight", ""),
    scraped_data.get("shoe_size", ""),
    scraped_data.get("blood_type", ""),
    scraped_data.get("guid", ""),
    scraped_data.get("uniqid", ""),
    scraped_data.get("mtcn", ""),
    scraped_data.get("mtcn_mg", ""),
    scraped_data.get("credit_score_fico", ""),
    scraped_data.get("credit_score_exp", ""),
    scraped_data.get("credit_score_equi", ""),
    scraped_data.get("credit_score_vant", ""),
    scraped_data.get("credit_score_nextgen", ""),
    scraped_data.get("credit_score_sbss", ""),
    scraped_data.get("religion", ""),
    scraped_data.get("political_side", ""),
    scraped_data.get("favorite_color", ""),
    scraped_data.get("favorite_food", ""),
    scraped_data.get("favorite_cereal", ""),
    scraped_data.get("favorite_season", ""),
    scraped_data.get("favorite_animal", ""),
    scraped_data.get("lucky_number", ""),
    scraped_data.get("ptin", ""),
    scraped_data.get("temp_ptin", ""),
    scraped_data.get("ein", ""),
    scraped_data.get("itin", ""),
    scraped_data.get("atin", ""),
    scraped_data.get("alignment", ""),
    scraped_data.get("dnd_charm", ""),
    scraped_data.get("dnd_const", ""),
    scraped_data.get("dnd_dext", ""),
    scraped_data.get("dnd_int", ""),
    scraped_data.get("dnd_str", ""),
    scraped_data.get("dnd_wise", "")
]

# Create a Dataframe
df = pd.DataFrame([data], columns=headers)

# Save all to an excel file 
output_file = "junk_people.xlsx"
df.to_excel(output_file, index=False)
print("Data written in excel")
