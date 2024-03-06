# Contact List Creation Script

This Python script reads a CSV file and creates a contact list in the vCard format that can be uploaded to a user's phone.

## Project Description

This project is designed to help users manage their contacts more efficiently. 
The script reads a CSV file where each line represents a contact with the first name, surname, and phone number. 
It then creates a new vCard file (`contacts.vcf`), which can be imported into most phone's contact lists.

## Requirements

- Python 3.6

## Usage

1. Prepare a CSV file with each line formatted as: `firstname,surname,phonenumber` and example is included.
2. Run the script: `python3 contact_list_creation.py` 
3. The script will create a `contacts.vcf` file in the same directory.

## Installation

1. Clone the repository: `git clone https://github.com/yourusername/contact-list-creation.git`
2. Navigate to the project directory: `cd contact-list-creation`
3. Run the script with Python 3: `python3 contact_list_creation.py`

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License

MIT
