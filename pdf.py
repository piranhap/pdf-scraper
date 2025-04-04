from pdfquery import PDFQuery

# load the pdf
pdf = PDFQuery('p1.pdf')
pdf.load()

#convert to xml 
pdf.tree.write('p1.xml', pretty_print = True)
pdf



# Variables
"""
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