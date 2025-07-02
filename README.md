# GUI-Based Library Management System

A Python-based application built using Tkinter that allows users to manage a library of books through a graphical interface. Designed as part of an Advanced Higher Computing course, this project demonstrates core programming concepts including GUI development, algorithms, object-oriented design, and file handling.

## Features

- View all books in a sortable table (Treeview)
- Search for a book by title using binary search
- Sort books by ID, title, author, or gente using bubble sort
- Borrow and return books with real-time status updates
- Load and save book data from and to a CSV file
- Input validation and user feedback via Tkinter message boxes

## Technologies Used

- Language: Python 3
- GUI Toolkit: Tkinter (including ttk widgets)
- File Handling: csv module
- Algorithms: Bubble Sort, Binary Search
- OOP Structure: Custom classes for Book, Library, and LibraryApp

## File Structure

library_management/
├── main.py              # Entry point of the application
├── library.py           # Core logic and classes (Book, Library)
├── gui.py               # GUI layout and functionality (LibraryApp)
├── books.csv            # Sample book dataset
├── README.md            # Project documentation

## Getting Started

1. Clone the repository:
   git clone https://github.com/guanyiwang-gyw/library-management-system.git
   cd library-management-system

2. Run the program:
   python main.py

3. Usage:
   - Click "Load" to import data from the CSV file.
   - Use the interface to search, sort, borrow, and return books.
   - Click "Save" to save any changes.

## Notes

- Ensure Python 3 is installed on your system.
- This project uses only standard Python libraries, so no external dependencies are required.

## Author

Created by Guanyi Wang as part of the S6 Advanced Higher Computing course (2025).

## License

This project is for educational purposes. Feel free to use or adapt with credit.