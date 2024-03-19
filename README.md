# Otter.ai Automated Note Archiver and Cleaner

## Introduction

The Otter.ai Automated Note Archiver and Cleaner is a sophisticated Python utility designed to streamline the process of backing up and clearing notes from your Otter.ai account. It serves as an invaluable tool for users looking to efficiently manage their digital note space by downloading transcriptions for offline storage, subsequently cleaning up their online account by removing these notes. This script navigates the Otter.ai web platform, systematically downloads each note, and then deletes them from the cloud, ensuring users maintain control over their data while managing their cloud storage usage effectively.

![Project Image Overview](https://github.com/DevRex-0201/Project-Images/blob/main/Py-Otter.ai-Note-Archiver.png)

## Key Features

- **Seamless Account Navigation**: Automates the login and navigation process within Otter.ai to access user notes.
- **Efficient Note Downloading**: Individual notes are downloaded and saved locally with filenames reflecting the note's original title and date, facilitating easy organization.
- **Automatic Note Deletion**: Post-download, notes are removed from the Otter.ai account, helping users manage their online storage.
- **Robust Error Management**: Incorporates error handling mechanisms to alert users to potential issues during the download and deletion process.

## System Requirements

To use the Otter.ai Automated Note Archiver and Cleaner, ensure your system meets the following criteria:

- Python version 3.6 or later
- The Playwright package for Python
- An active Otter.ai account with notes available for download and deletion

## Setup Instructions

1. **Install Playwright**: Install the Playwright package and its dependencies with the command:
   ```bash
   pip install playwright
   playwright install
   ```
2. **Obtain the Script**: Download the Otter.ai Automated Note Archiver and Cleaner script to your computer.

## Running the Script

1. **Launch Terminal/CMD**: Navigate to the folder containing the script.
2. **Execute the Script**: Start the script with the command:
   ```bash
   python otter_ai_automated_note_archiver_and_cleaner.py
   ```
3. **User Authentication**: Manually log into your Otter.ai account in the Chromium browser window prompted by the script.
4. **Initiate Automation**: Press Enter in the terminal to begin the automated process of note downloading and deletion.

## Operational Overview

- The script accesses the "My Notes" section on Otter.ai, identifies available notes, and processes them individually—downloading each and formatting its title for local storage.
- Following download, it proceeds to delete each note from the Otter.ai account, thereby freeing up cloud storage.

## Troubleshooting and Support

- Ensure all system requirements are met and that dependencies are correctly installed.
- Refer to error messages logged by the script for troubleshooting insights.

## Disclaimer and Use Policy

This utility is independently developed and not officially endorsed or affiliated with Otter.ai. Users should employ this tool at their own discretion and risk. The developer is not liable for any data loss or account issues resulting from the use of this script.

## Contributions

Feedback and contributions to the Otter.ai Automated Note Archiver and Cleaner are welcome. Please feel free to fork the repository, make enhancements, and submit pull requests for review.
