#!/usr/bin/env python3
import os
import shutil
import time

def last_mod_time(fname):
    """Get the last modification time of a file."""
    return os.path.getmtime(fname)

def move_old_files(src_folder, dst_folder, threshold_days=730):
    """
    Move files not modified in the last threshold_days (default: 2 years).

    Args:
        src_folder (str): Source folder path.
        dst_folder (str): Destination folder path.
        threshold_days (int): Number of days to consider a file old (default: 730 days).
    """
    try:
        # Prompt the user to start the script by pressing SPACE
        print("Press SPACE to start the script...")
        while True:
            key = input()
            if key == " ":
                break

        # Get the current time
        now = time.time()
        threshold_seconds = threshold_days * 24 * 60 * 60

        # Traverse through files in the source folder
        for root, _, files in os.walk(src_folder):
            for fname in files:
                src_fname = os.path.join(root, fname)
                if last_mod_time(src_fname) < now - threshold_seconds:
                    # Create corresponding subdirectories in the destination folder
                    rel_path = os.path.relpath(src_fname, src_folder)
                    dst_subdir = os.path.join(dst_folder, os.path.dirname(rel_path))
                    os.makedirs(dst_subdir, exist_ok=True)

                    # Move the file
                    dst_fname = os.path.join(dst_subdir, fname)
                    shutil.move(src_fname, dst_fname)
                    print(f"Moved: {src_fname} -> {dst_fname}")

        print("Script completed successfully.")
        # Prompt the user to exit the script by pressing SPACE
        print("Press SPACE to exit the script...")
        while True:
            key = input()
            if key == " ":
                break

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    source_directory = "C:/path/to/source/folder"
    destination_directory = "D:/path/to/destination/folder"

    # Call the function with specified source and destination directories
    move_old_files(source_directory, destination_directory)