# Assignment Submission
# Project: Multi-Utility CLI Application

A single Python command-line program that combines all required functionalities into one simple menu.
All data (books, URLs, calculator history) is stored automatically using JSON files inside a data/ folder.

# How to Run
Requires Python 3.8+
Download or extract the project folder
Open terminal → go to the project directory
Run:python main.py
Choose utilities from the menu
JSON files are created automatically

# Files Included
main.py → complete program + menu
data/books.json → stores books and IDs
data/urls.json → stores URL → code mappings
data/calc_history.json → stores calculator history
README.md → documentation
submission.zip → zipped project folder

# Logic Summary
1. Word Frequency Counter
Converts text to lowercase
Removes punctuation
Splits text into words
Counts each unique word using a dictionary
Sorts by:
highest frequency first
alphabetical order if counts match
Prints results in word - count format

2. Balanced Brackets Checker
Uses a stack method
Pushes opening brackets: ( { [
When closing bracket appears:
checks if it matches the last opening bracket
If mismatch or leftover stack → not balanced
Fully balanced only if stack is empty at the end

3. Library Management System
All books stored in data/books.json
Each book contains:
ID:Title, Author, Availability status
Features included:
Add a book
Search by title/author
Borrow a book (marks unavailable)
Return a book
List all books
Data automatically saved after each action

4. Longest Increasing Subsequence (LIS) Length
Uses efficient O(n log n) algorithm
Maintains a tails list
Uses binary search to place each number
Length of tails = LIS length
Handles any sequence of integers

5. URL Shortener
Creates unique 6-character codes
Characters include A–Z, a–z, 0–9
Stores two mappings in data/urls.json:
code → original URL
URL → code
shorten(url) returns a short code
redirect(code) returns original URL
Prevents collisions by re-generating codes if needed

6. Calculator with History
Supports:Addition, Subtraction, Multiplication, Division
After each calculation:Expression + result saved to data/calc_history.json
Users can view entire calculation history
Simple and safe character-validated input

# General Notes
JSON storage ensures data persists even after closing the program
Code is intentionally simple and readable
No third-party libraries required
Ideal for structured, clear demonstration of logic for a coding round

# Submission
Submit the Anushree SM_Spyyda Tech_Assessment.zip file or upload to GitHub as required
Ensure all files, especially the data/ folder, are included