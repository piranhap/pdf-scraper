from pdfquery import PDFQuery
import re

pdf = PDFQuery('p1.pdf')
pdf.load()


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
email_link = pdf.pq('LTTextBoxHorizontal:in_bbox("")') # This one needs to be found differently, to look for the mailinator domain or something like that
phone = pdf.pq('LTTextBoxHorizontal:in_bbox("101.285, 293.161, 147.992, 300.661")').text()
address = pdf.pq('LTTextBoxHorizontal:in_bbox("101.285, 280.411, 266.242, 287.911")').text()
ssn = pdf.pq('LTTextBoxHorizontal:in_bbox("101.285, 254.911, 226.764, 262.411")').text()
passport_n = pdf.pq('LTTextBoxHorizontal:in_bbox("101.285, 242.161, 154.664, 249.661")').text()
passport_issued_date = pdf.pq('LTTextBoxHorizontal:in_bbox("101.285, 233.911, 190.923, 241.411")').text()
passport_exp_date = pdf.pq('LTTextBoxHorizontal:in_bbox("101.285, 225.661, 193.42, 233.161")').text()
passport_code = pdf.pq('LTTextBoxHorizontal:in_bbox("101.285, 217.118, 282.721, 224.618]")').text()


drivers_license_raw = pdf.pq('LTTextBoxHorizontal:in_bbox("101.285, 194.911, 333.921, 202.411")').text()
# Extract from drivers_license_n
license_match = re.match(
    r"(?P<number>[A-Z0-9\-]+) - issued in(?P<state>.+?) on (?P<issued_date>\d{2}/\d{2}/\d{4})",
    drivers_license_raw
)
# if license match occurs 
if license_match: 
    drivers_license_n = license_match.group("number")
    drivers_license_state = license_match.group("state")
    drivers_license_issued_date = license_match.group("issued_date")
else:
    print("error matching ")

print(f"DL #: {drivers_license_n}")
print(f"DL #: {drivers_license_state}")
print(f"DL #: {drivers_license_issued_date}")


drivers_license_exp_date = pdf.pq('LTTextBoxHorizontal:in_bbox("101.285, 186.661, 138.822, 194.161")').text()
car_model= pdf.pq('LTTextBoxHorizontal:in_bbox("101.285, 173.911, 166.734, 181.411")').text()
car_plate_number = pdf.pq('LTTextBoxHorizontal:in_bbox("")').text() # same ^
car_plate_state_issued = pdf.pq('LTTextBoxHorizontal:in_bbox("")').text() # same ^
car_plate_date_issued = pdf.pq('LTTextBoxHorizontal:in_bbox("")').text() # same ^
hair_color = pdf.pq('LTTextBoxHorizontal:in_bbox("31.5, 126.661, 110.067, 134.161")').text() # remove the first words
eyes_color = pdf.pq('LTTextBoxHorizontal:in_bbox("31.5, 113.911, 117.984, 121.411")').text() # remove the first words
height = pdf.pq('LTTextBoxHorizontal:in_bbox("73.395, 101.161, 128.839, 108.661")').text()
weight = pdf.pq('LTTextBoxHorizontal:in_bbox("73.395, 88.411, 138.448, 95.911")').text()
shoe_size = pdf.pq('LTTextBoxHorizontal:in_bbox("31.5, 75.661, 83.821, 83.161")').text() # remove the first words
blood_type = pdf.pq('LTTextBoxHorizontal:in_bbox("31.5, 62.911, 250.488, 70.411")').text() # remove can donate to:
guid = pdf.pq('LTTextBoxHorizontal:in_bbox("399.539, 222.661, 581.243, 230.161")').text()
uniqid = pdf.pq('LTTextBoxHorizontal:in_bbox("399.539, 209.911, 518.734, 217.411")').text()
mtcn = pdf.pq('LTTextBoxHorizontal:in_bbox("461.812, 175.411, 581.243, 182.911")').text() # remove the first words
mtcn_mg = pdf.pq('LTTextBoxHorizontal:in_bbox("539.531, 162.661, 572.9, 170.161")').text()
credit_score_fico = pdf.pq('LTTextBoxHorizontal:in_bbox("562.898, 128.161, 575.412, 135.661")').text()
credit_score_exp = pdf.pq('LTTextBoxHorizontal:in_bbox("562.898, 115.411, 581.246, 122.911")').text()
credit_score_equi = pdf.pq('LTTextBoxHorizontal:in_bbox("562.898, 102.661, 581.246, 110.161")').text()
credit_score_vant = pdf.pq('LTTextBoxHorizontal:in_bbox("562.898, 89.911, 575.815, 97.411")').text()
credit_score_nextgen = pdf.pq('LTTextBoxHorizontal:in_bbox("562.898, 77.161, 575.412, 84.661")').text()
credit_score_sbss = pdf.pq('LTTextBoxHorizontal:in_bbox("405.434, 64.411, 575.412, 71.911")').text() # remove the first words
religion = pdf.pq('LTTextBoxHorizontal:in_bbox("111.035, 752.161, 138.131, 759.661")').text()
political_side = pdf.pq('LTTextBoxHorizontal:in_bbox("111.035, 739.411, 143.544, 746.911")').text()
f_color = pdf.pq('LTTextBoxHorizontal:in_bbox("111.035, 726.661, 124.794, 734.161")').text()
f_food = pdf.pq('LTTextBoxHorizontal:in_bbox("31.5, 713.911, 144.807, 721.411")').text() # Remove Favorite comfort food string
f_cereal = pdf.pq('LTTextBoxHorizontal:in_bbox("111.035, 701.161, 180.22, 708.661")').text()
f_season = pdf.pq('LTTextBoxHorizontal:in_bbox("111.035, 688.411, 132.715, 695.911")').text()
f_animal = pdf.pq('LTTextBoxHorizontal:in_bbox("111.035, 675.661, 125.9, 683.161")').text()
l_number = pdf.pq('LTTextBoxHorizontal:in_bbox("111.035, 662.911, 115.206, 670.411")').text()
ptin = pdf.pq('LTTextBoxHorizontal:in_bbox("194.555, 628.411, 232.926, 635.911")').text()
temp_ptin = pdf.pq('LTTextBoxHorizontal:in_bbox("194.555, 615.661, 232.926, 623.161")').text()
ein = pdf.pq('LTTextBoxHorizontal:in_bbox("194.555, 602.911, 232.095, 610.411")').text()
itin = pdf.pq('LTTextBoxHorizontal:in_bbox("31.5, 590.161, 231.538, 597.661")').text() # clean output 
atin = pdf.pq('LTTextBoxHorizontal:in_bbox("31.5, 577.411, 232.095, 584.911")').text() # clean output
alignment = pdf.pq('LTTextBoxHorizontal:in_bbox("31.5, 542.911, 105.2, 550.411")').text() # clean output
dnd_charm = pdf.pq('LTTextBoxHorizontal:in_bbox("69.352, 530.161, 109.781, 537.661")').text() # clean output
dnd_const = pdf.pq('LTTextBoxHorizontal:in_bbox("69.352, 521.911, 121.467, 529.411")').text() # clean output
dnd_dext = pdf.pq('LTTextBoxHorizontal:in_bbox("69.352, 513.661, 107.28, 521.161")').text() # clean output
dnd_int = pdf.pq('LTTextBoxHorizontal:in_bbox("69.352, 505.411, 119.804, 512.911")').text() # clean output
dnd_str = pdf.pq('LTTextBoxHorizontal:in_bbox("69.352, 497.161, 106.042, 504.661")').text() # clean output
dnd_wise = pdf.pq('LTTextBoxHorizontal:in_bbox("69.352, 488.911, 108.946, 496.411")').text() # clean output

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
    "passport_number": passport_n,
    "passport_issued_date": passport_issued_date,
    "passport_exp_date": passport_exp_date,
    "passport_code": passport_code,
    "drivers_license_number": drivers_license_n,
    "car_model": car_model,
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

for key, value in scraped_data.items():
    print(f"{value}")






# Variables to get
"""
f_name = pdf.pq('LTTextBoxHorizontal:in_bbox("")').text()

Headers for sheet 
    Gender
    First Name
    Middle Name
    Last Name
    Initials
    Mother's maiden name
    Birthday
    Birthplace
    Zodiacal Sign 
    Username
    Password
    Password Hash (MD5)
    Password Hash (SHA1)
    E-mail
    Phone
    Address
    SSN (2141123212) - issued in maryland
    Passport
        Passport #
        Passport issued date
        Passport exp date 
        Passport code 
            P<USAANDREWS<<WAYNE<VICTOR<<<<<<<<<<<<<<<<<<
            5730248430USA9605280M3012073<<<<<<<<<<<<<<08
    Drivers License
        Number
        State issued 
        issued date
        exp date
    Car
    Car License Plate  
        Number
        state issued 
        date issued
    Hair Color 
    Eyes Color
    Height
    Weight
    Shoe Size
    Blood Type 
    Unique ID Numbers 
        GUID
        UniqID
    Western Union MTCN
    MoneyGram MTCN
    FICO Credit Score
    Experian
    Equifax
    Vantage Score
    FICO NextGen Risk Score
    FICO Small Business Scoring Service(SBSS)
    Religion
    Political side
    Favorite Color 
    Favorite comfort food 
    Favorite Cereal
    Favorite Season
    Favorite Animal
    Lucky number
    Preparer Tax Identification Number (PTIN)
    Interim PTIN (temporary PTIN)
    Employer Identification Number (EIN)
    Individual Taxpayer Identification Number (ITIN)
    Adoption Taxpayer Identification Number (ATIN)
    Alignment 
    Abilities
        Charisma
        Constitution
        Dexterity
        Intelligence
        Strength
        Wisdom
"""