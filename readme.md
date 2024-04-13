****Desktop File Organizer****

**Project Overview**
This Python script automates the organization of files on your desktop. It monitors your desktop for new files and moves them into designated folders based on their file type. For example, documents (like PDFs and Word files) are moved to a documents folder, while images (such as JPEGs and PNGs) are moved to an images folder.

**Features**
Real-time Monitoring: Automatically detects new files added to the desktop.
Automatic File Sorting: Moves files to appropriate directories based on their extensions.
Customizable: Easy to modify the script to add new file types and directories.

**Requirements**
Python 3.6+
watchdog Python library

**Intallation**
1. Clone the repository or download the script:
   git clone https://github.com/yourusername/desktop-file-organizer.git
   cd desktop-file-organizer
2. Set up a Python virtual environment (recommended):
  python -m venv venv
  source venv/bin/activate  # On Windows use `venv\Scripts\activate`
3. Install dependencies:
   pip install watchdog

**Usage**
Run the program
1. Navigate to the script's directory:
   cd path/to/desktop-file-organizer
2. Run the script:
   python desktop_organizer.py
3. Leave the script running in the background.
   The script will continuously monitor your desktop and organize new files as they are added.
   
Configuration
To add or change the file types and their corresponding directories:

1. Edit the categorize_files function in the script:
  You will find the function in utils module.
2. Add or remove the extensions and folders as needed.

**Troubleshooting**
Issue: The script is not detecting files.

Solution: Check if the script is running and if the path to the desktop is correctly defined.
Issue: Files are not moving to the intended folders.

Solution: Ensure the extensions are correctly mapped in the categorize_files function. Check folder permissions on your desktop.
