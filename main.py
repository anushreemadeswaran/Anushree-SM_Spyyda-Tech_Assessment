import json
import os
import random
import string
import hashlib
import bisect
import re

DATA_DIR = os.path.join(os.path.dirname(__file__), "data")
os.makedirs(DATA_DIR, exist_ok=True)

BOOKS_FILE = os.path.join(DATA_DIR, "books.json")
URLS_FILE = os.path.join(DATA_DIR, "urls.json")
HISTORY_FILE = os.path.join(DATA_DIR, "calc_history.json")

def load_json(path, default):
    if not os.path.exists(path):
        with open(path, "w") as f:
            json.dump(default, f, indent=2)
        return default
    with open(path, "r") as f:
        return json.load(f)

def save_json(path, data):
    with open(path, "w") as f:
        json.dump(data, f, indent=2)

# 1.Word Frequency 
def word_frequency_counter(paragraph):
    words = re.findall(r"[a-zA-Z0-9']+", paragraph.lower())
    freq = {}
    for w in words:
        freq[w] = freq.get(w, 0) + 1
    items = sorted(freq.items(), key=lambda kv: (-kv[1], kv[0]))
    return items

# 2.Balanced Brackets
def balanced_brackets(s):
    pairs = {')':'(', ']':'[', '}':'{'}
    stack = []
    for ch in s:
        if ch in "([{":
            stack.append(ch)
        elif ch in ")]}":
            if not stack or stack[-1] != pairs[ch]:
                return False
            stack.pop()
    return not stack

# 3.Library Management
def init_books():
    default = {"books": []}
    return load_json(BOOKS_FILE, default)

def add_book(title, author, copies=1):
    data = init_books()
    book_id = hashlib.sha1((title+author).encode()).hexdigest()[:8]
    book = {"id": book_id, "title": title, "author": author, "copies": copies, "borrowed": 0}
    data["books"].append(book)
    save_json(BOOKS_FILE, data)
    return book

def search_books(query):
    data = init_books()
    q = query.strip().lower()
    res = [
        b for b in data["books"]
        if q in b["title"].lower() or q in b["author"].lower() or q == b["id"].lower()
    ]
    return res

def borrow_book(book_id):
    data = init_books()
    for b in data["books"]:
        if b["id"] == book_id:
            if b["borrowed"] < b["copies"]:
                b["borrowed"] += 1
                save_json(BOOKS_FILE, data)
                return True, "Borrowed successfully."
            else:
                return False, "No available copies."
    return False, "Book ID not found."

def return_book(book_id):
    data = init_books()
    for b in data["books"]:
        if b["id"] == book_id:
            if b["borrowed"] > 0:
                b["borrowed"] -= 1
                save_json(BOOKS_FILE, data)
                return True, "Returned successfully."
            else:
                return False, "No borrowed copies to return."
    return False, "Book ID not found."

# 4.Longest Increasing Subsequence
def lis_length(arr):
    tails = []
    for x in arr:
        i = bisect.bisect_left(tails, x)
        if i == len(tails):
            tails.append(x)
        else:
            tails[i] = x
    return len(tails)

# 5.URL Shortener
def init_urls():
    default = {"map": {}}
    return load_json(URLS_FILE, default)

def _generate_code():
    alphabet = string.ascii_letters + string.digits
    return ''.join(random.choice(alphabet) for _ in range(6))

def shorten(url):
    data = init_urls()
    for attempt in range(1000):
        code = _generate_code()
        if code not in data["map"]:
            data["map"][code] = url
            save_json(URLS_FILE, data)
            return code
    raise RuntimeError("Unable to generate unique code. Try again later.")

def redirect(code):
    data = init_urls()
    return data["map"].get(code)

# 6.Calculator with History
def init_history():
    return load_json(HISTORY_FILE, {"history": []})

def calculate(expr):
    allowed = set("0123456789+-*/(). %")
    if not set(expr) <= allowed:
        raise ValueError("Expression contains invalid characters.")
    result = eval(expr, {"__builtins__": None}, {})
    hist = init_history()
    hist["history"].append({"expr": expr, "result": result})
    save_json(HISTORY_FILE, hist)
    return result

def get_history():
    return init_history()["history"]

def print_menu():
    print("----Coding Menu----")
    print("1) Word Frequency Counter")
    print("2) Balanced Brackets Validator")
    print("3) Library Management System")
    print("4) LIS Length")
    print("5) URL Shortener")
    print("6) Calculator with History")
    print("0) Exit")

def menu():
    while True:
        print_menu()
        choice = input("Choose option: ").strip()
        
        if choice == "0":
            print("Goodbye!")
            break
        
        elif choice == "1":
            p = input("Enter paragraph: ")
            items = word_frequency_counter(p)
            print("\nWord frequencies (descending):")
            for w, c in items:
                print(f"{w} - {c}")
        
        elif choice == "2":
            s = input("Enter string with brackets: ")
            print(balanced_brackets(s))
        
        elif choice == "3":
            print("\nLibrary Menu:")
            print(" a) Add book")
            print(" b) Search books")
            print(" c) Borrow book")
            print(" d) Return book")
            sub = input("Choose (a/b/c/d): ").strip().lower()

            if sub == "a":
                title = input("Title: ")
                author = input("Author: ")
                copies = int(input("Copies (number, default 1): ") or 1)
                book = add_book(title, author, copies)
                print("Added:", book)

            elif sub == "b":
                q = input("Search query (title/author/id): ")
                res = search_books(q)
                if res:
                    print(f"\nFound {len(res)} result(s):")
                    for b in res:
                        print(f"ID: {b['id']}, Title: {b['title']}, Author: {b['author']}, Copies: {b['copies']}, Borrowed: {b['borrowed']}")
                else:
                    print("No results.")

            elif sub == "c":
                bid = input("Book ID: ")
                ok, msg = borrow_book(bid)
                print(msg)

            elif sub == "d":
                bid = input("Book ID: ")
                ok, msg = return_book(bid)
                print(msg)
            
            else:
                print("Unknown option.")

        elif choice == "4":
            s = input("Enter integers separated by spaces: ")
            arr = list(map(int, s.split()))
            print("LIS length:", lis_length(arr))
            print("Note: Standard Longest Increasing Subsequence (LIS) used.")

        elif choice == "5":
            print("a) shorten URL\nb) redirect (get URL from code)")
            sub = input("Choose (a/b): ").strip().lower()
            if sub == "a":
                url = input("Enter URL: ").strip()
                code = shorten(url)
                print("Short code:", code)
            elif sub == "b":
                code = input("Enter code: ").strip()
                url = redirect(code)
                print("Original URL:", url)
            else:
                print("Unknown option.")

        elif choice == "6":
            print("Calculator: enter simple arithmetic expression (e.g. 2+3*4)")
            expr = input("Expr: ").strip()
            try:
                res = calculate(expr)
                print("Result:", res)
            except Exception as e:
                print("Error:", e)
            print("History:")
            for h in get_history():
                print(f"{h['expr']} = {h['result']}")
        
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    menu()