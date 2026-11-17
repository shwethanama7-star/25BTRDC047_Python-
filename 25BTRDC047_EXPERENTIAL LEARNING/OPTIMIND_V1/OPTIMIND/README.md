# OPTIMIND V1.0 — Local PC Optimization Agent

A beginner-friendly, offline Python terminal application for Windows 11.

## Features
- Live CPU, RAM and system-drive usage snapshot
- Top processes by resident memory
- User temporary-folder scan and confirmed cleanup
- Large-file discovery in Downloads, Desktop and Documents
- Rule-based local recommendations
- SQLite activity history

## Requirements
- Windows 10/11
- Python 3.10 or newer (Python 3.11+ recommended)
- Internet only for the one-time installation of dependencies; the application itself runs offline.

## Setup (Windows PowerShell)

1. Extract the ZIP file.
2. Open the extracted `OPTIMIND` folder in VS Code.
3. Open Terminal > New Terminal.
4. Check Python:

   `py --version`

5. Create a virtual environment:

   `py -m venv .venv`

6. Activate it in PowerShell:

   `.\.venv\Scripts\Activate.ps1`

   If PowerShell blocks activation, run this for the current terminal only:

   `Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass`

   Then activate again.

7. Install dependencies (requires internet once):

   `py -m pip install -r requirements.txt`

8. Run:

   `py main.py`

After dependencies are installed, OPTIMIND runs locally without internet or API keys.

## If you want to install completely offline
Download the required wheels on another computer with internet using:

`py -m pip download -r requirements.txt -d wheels`

Copy the `wheels` folder to this project, then install with:

`py -m pip install --no-index --find-links=wheels -r requirements.txt`

## Safety notes
- Cleanup is limited to the current user's temporary directory.
- Files are listed before cleanup and deletion requires confirmation.
- Large files are reported, never deleted by this version.
- Process termination is opt-in and uses a normal terminate request; no forced kill is attempted.
- Some files may be locked or inaccessible and will be skipped.
- Do not terminate processes unless you recognize them and have saved your work.
- This tool does not magically free RAM; Windows manages memory and caching itself.
- The disk percentage shown is for the Windows system drive.
