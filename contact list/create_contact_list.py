import csv
import os

def create_vcard(filename):
    try:
        with open(filename, 'r') as csv_file:
            csv_reader = csv.reader(csv_file)
            for row in csv_reader:
                firstname, surname, phone_number = row
                vcard_format = f"""
BEGIN:VCARD
VERSION:2.1
N:{surname};{firstname};;;
FN:{firstname} {surname}
TEL;CELL:{phone_number}
END:VCARD
"""
                with open('contacts.vcf', 'a') as vcf_file:
                    vcf_file.write(vcard_format)
    except Exception as e:
        print(f"An error occurred: {e}")

# Check if the file exists
if os.path.exists('contacts.vcf'):
    print("File exists, proceeding...")
else:
    print("File does not exist, creating and proceeding...")
    open('contacts.vcf', 'w').close()

create_vcard('contacts.csv')
