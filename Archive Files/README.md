# File Organizer Script

## Overview
This Python script organizes files from a source folder to a destination folder based on their last modification time. 
Files older than a specified threshold (default: 2 years) are moved to the destination Archive folder.

## Features
- **Threshold Days**: You can adjust the number of days to consider a file old.
- **Folder Structure**: The script creates corresponding subdirectories in the destination folder to maintain the original structure.
- **Interactive Start**: The script prompts you to press SPACE before execution.
- **Error Handling**: If any issues occur, an error message is displayed.

## Installation
1. Clone this repository to your local machine.
2. Ensure you have Python installed.
3. Modify the `source_directory` and `destination_directory` variables in the script to point to your desired folders.

## Usage
1. Open a terminal or command prompt.
2. Navigate to the directory containing the script.
3. Run the script using the command:
   ```bash
   python file_organizer.py
