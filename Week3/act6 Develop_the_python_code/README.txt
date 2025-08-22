# Yoobee College Database Management System

## Overview
This project is developed for Activity 6 of Week 3. It implements a small college database system that allows administrative staff to:
- Add, view, and delete students  
- Add and view tutors  
- Add and view courses  

The system uses SQLite as the backend database and is operated via a menu-driven command-line interface.

## Technical Features
- Python 3 with sqlite3 module (no external dependencies)  
- Modular structure (separated into multiple Python files)  
- Robust input validation (e.g. numeric ID checks)  
- Simple terminal interface for ease of use  

## File Descriptions
- `database.py`: Sets up the SQLite database and creates required tables (Students, Tutors, Courses)  
- `db_manager.py`: Contains all database operations (add/view/delete) for each table  
- `main.py`: Entry point of the program. Shows menu and calls corresponding functions  

## How to Run the Program

### Step 1: Open a Terminal

Open a terminal to run the program:  

**Windows**:  
- Press `Win + R`, type `cmd`, and press Enter  
- Or search for "Command Prompt" or "Terminal" from the Start Menu  

**macOS**:  
- Press `Cmd + Space`, type `Terminal`, and press Enter  
- Or go to `Launchpad > Other > Terminal`  

**Linux**:  
- Usually you can press `Ctrl + Alt + T`  
- Or search for "Terminal" in the Applications menu  

### Step 2: Check if Python is Installed

Type the following command and press Enter:  
```bash
python --version
```
If you see a version number (e.g., Python 3.11.6), you have Python installed.  
If not, please [download and install Python](https://www.python.org/downloads/).

### Step 3: Navigate to the Project Folder

Before running the program, navigate to the folder where your `main.py` file is located. For example, if the file is in:  
```
Downloads/Week3/act6 Develop_the_python_code/
```

Use the following commands:

**macOS or Linux**:  
```bash
cd ~/Downloads/Week3/act6\ Develop_the_python_code
```

**Windows**:  
```cmd
cd "%USERPROFILE%\Downloads\Week3\act6 Develop_the_python_code"
```

💡 *Tip: After typing `cd ` (with a space), you can drag and drop the folder into your terminal window to automatically insert the correct path.*

### Step 4: Run the Program

Once you're in the correct directory, run the program using:  
```bash
python main.py
```
Or, if your system uses Python 2 by default:  
```bash
python3 main.py
```

You should then see the following menu interface:
```
----------Yoobee College Database Management System----------
1. Add Student
2. Delete Student
3. View All Students
4. Add Tutor
5. View All Tutors
6. Add Course
7. View All Courses
8. Exit
Enter your choice (1–8):
```
