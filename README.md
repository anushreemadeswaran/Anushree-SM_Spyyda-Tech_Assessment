Multi-Utility CLI Application
Overview

This project is a Python-based command-line application that brings together multiple utilities within a single interactive menu. It uses JSON files for persistent data storage, automatically creating them inside a dedicated data folder whenever the program runs. The application requires Python 3.8 or higher and is designed to run smoothly on any system with a standard Python installation. Users can explore all available tools through a simple and intuitive text-based interface.

How to Run

To run the application, the user must first download or extract the project folder to their system. After that, they should open a terminal, navigate to the project directory, and ensure they are working within the same folder as the main.py file. Once inside the directory, the program can be launched by typing python main.py in the terminal. The application will immediately display a menu from which users can select various utilities. All related JSON files, including those for books, URLs, and calculator history, are created and updated automatically as the program is used.

Project Structure

The project consists of the main Python file (main.py), which contains all core logic and menu navigation. A data folder serves as the storage area for JSON files used by different modules, ensuring that book records, shortened URLs, and calculator history persist across sessions. Additionally, the project includes a README file that provides documentation for understanding and running the application, and it may also be packaged into a ZIP file for submission or distribution.

Word Frequency Counter

This module processes a block of text by converting it to lowercase, removing punctuation, breaking it into individual words, and counting the occurrences of each word. The results are displayed in descending order of frequency, with alphabetical order used for words that appear equally often. The design allows users to understand the frequency distribution of words in any given paragraph.

Balanced Brackets Checker

The balanced brackets checker evaluates a string containing brackets by using a stack-based method. It pushes opening brackets—such as parentheses, curly braces, and square brackets—onto the stack and checks for matching closing brackets as it processes the string. The string is considered balanced only when every opening bracket has a corresponding closing bracket and the stack is empty at the end.

Library Management System

This component manages a collection of books stored in books.json. Each book record contains a unique ID, title, author, and availability status. Users can add new books to the library, search for books by title or author name, borrow available books, return previously borrowed books, and view the entire list of stored entries. All changes are immediately saved to the JSON file, ensuring persistent data even after the program is closed.

Longest Increasing Subsequence (LIS)

The LIS module calculates the length of the Longest Increasing Subsequence in a sequence of numbers using an efficient O(n log n) algorithm. It maintains a dynamic list representing the smallest possible tail values for subsequences of different lengths and uses binary search to determine the correct position for each incoming number. The final length of this list gives the LIS length, making the tool effective for analyzing numerical patterns.

URL Shortener

The URL shortener generates unique six-character codes made from uppercase letters, lowercase letters, and digits. These codes are mapped to original URLs and stored inside the urls.json file. Users can create shortened versions of long URLs and retrieve the original URLs by entering their associated codes. When duplicates occur, the system automatically generates a new code to ensure uniqueness.

Calculator with History

The calculator performs basic arithmetic operations such as addition, subtraction, multiplication, and division. After each operation, the expression and its result are stored in the calc_history.json file, allowing users to review their past calculations at any time. The feature also includes input validation to ensure safe and accurate evaluation of mathematical expressions.

Conclusion

This CLI application provides a collection of useful tools packaged into a single program, demonstrating structured Python programming, JSON-based data management, and algorithmic problem-solving. With its clean design, modular functionality, and persistent storage features, it is well-suited for learning, academic submissions, technical assessments, and practical experimentation.
