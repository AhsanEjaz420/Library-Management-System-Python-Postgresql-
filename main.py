# # main.py

# from models.members import create_member, get_all_members, get_member_by_id
# from models.books import create_book, get_all_books, get_book_by_id
# # (You can import borrow_records later when you implement those)

# def print_menu():
#     print("\n=== Library Management Menu ===")
#     print("1. Add Member")
#     print("2. View All Members")
#     print("3. View Member by ID")
#     print("4. Add Book")
#     print("5. View All Books")
#     print("6. View Book by ID")
#     print("0. Exit")

# def main():
#     while True:
#         print_menu()
#         choice = input("Enter your choice: ").strip()

#         if choice == "1":
#             name = input("Name: ")
#             phone = input("Phone: ")
#             email = input("Email: ")
#             member_id = create_member(name, phone, email)
#             print(f"Member added with ID: {member_id}")

#         elif choice == "2":
#             members = get_all_members()
#             for m in members:
#                 print(m)

#         elif choice == "3":
#             mid = input("Enter Member ID: ")
#             member = get_member_by_id(mid)
#             print(member)

#         elif choice == "4":
#             title = input("Book Title: ")
#             author = input("Author: ")
#             category = input("Category: ")
#             total = int(input("Total Copies: "))
#             available = int(input("Available Copies: "))
#             book_id = create_book(title, author, category, total, available)
#             print(f"Book added with ID: {book_id}")

#         elif choice == "5":
#             books = get_all_books()
#             for b in books:
#                 print(b)

#         elif choice == "6":
#             bid = input("Enter Book ID: ")
#             book = get_book_by_id(bid)
#             print(book)

#         elif choice == "0":
#             print("Exiting…")
#             break

#         else:
#             print("Invalid choice. Please try again.")

# if __name__ == "__main__":
#     main()

# /mnt/data/main.py
import sys
from datetime import datetime

from models.members import create_member, get_all_members, get_member_by_id, update_member, delete_member
from models.books import create_book, get_all_books, get_book_by_id, update_book, update_available_copies, delete_book
from models.borrow_records import (
    create_borrow_record,
    get_all_borrow_records_with_details,
    get_all_borrow_records,
    get_borrow_history_for_member,
    mark_as_returned,
    update_borrow_record,
    delete_borrow_record,
    get_borrow_count_per_member
)

def prompt_int(prompt):
    v = input(prompt).strip()
    return int(v) if v and v.isdigit() else None

def add_member():
    name = input("Name: ").strip()
    phone = input("Phone: ").strip()
    email = input("Email: ").strip()
    try:
        mid = create_member(name, phone, email)
        print("Member added. ID:", mid)
    except Exception as e:
        print("Error:", e)

def add_book():
    title = input("Title: ").strip()
    author = input("Author: ").strip()
    category = input("Category: ").strip()
    total = input("Total copies (int): ").strip()
    available = input("Available copies (int): ").strip()
    try:
        bid = create_book(title, author, category, int(total), int(available))
        print("Book added. ID:", bid)
    except Exception as e:
        print("Error:", e)

def create_borrow():
    mid = prompt_int("Member ID: ")
    bid = prompt_int("Book ID: ")
    if mid is None or bid is None:
        print("Invalid IDs.")
        return
    try:
        rid = create_borrow_record(mid, bid)
        print("Borrow created. Record ID:", rid)
    except Exception as e:
        print("Error:", e)

def view_all_borrows_details():
    rows = get_all_borrow_records_with_details()
    print("ID | MemberID | MemberName | BookID | BookTitle | BorrowDate | ReturnDate | Status")
    for r in rows:
        print(r)

def view_all_borrows():
    rows = get_all_borrow_records()
    for r in rows:
        print(r)

def view_member_history():
    mid = prompt_int("Member ID: ")
    if mid is None:
        print("Invalid ID.")
        return
    rows = get_borrow_history_for_member(mid)
    for r in rows:
        print(r)

def mark_returned():
    rid = prompt_int("Borrow Record ID to mark returned: ")
    if rid is None:
        print("Invalid ID.")
        return
    try:
        mark_as_returned(rid)
        print("Marked returned.")
    except Exception as e:
        print("Error:", e)

def update_member_cli():
    mid = prompt_int("Member ID to update: ")
    if mid is None:
        print("Invalid ID.")
        return
    name = input("New name (leave blank to skip): ").strip() or None
    phone = input("New phone (leave blank to skip): ").strip() or None
    email = input("New email (leave blank to skip): ").strip() or None
    try:
        update_member(mid, name=name, phone=phone, email=email)
        print("Member updated.")
    except Exception as e:
        print("Error:", e)

def delete_member_cli():
    mid = prompt_int("Member ID to delete: ")
    if mid is None:
        print("Invalid ID.")
        return
    try:
        delete_member(mid)
        print("Member deleted.")
    except Exception as e:
        print("Error:", e)

def update_book_cli():
    bid = prompt_int("Book ID to update: ")
    if bid is None:
        print("Invalid ID.")
        return
    title = input("New title (leave blank to skip): ").strip() or None
    author = input("New author (leave blank to skip): ").strip() or None
    category = input("New category (leave blank to skip): ").strip() or None
    try:
        update_book(bid, title=title, author=author, category=category)
        print("Book updated.")
    except Exception as e:
        print("Error:", e)

def update_book_copies_cli():
    bid = prompt_int("Book ID: ")
    if bid is None:
        print("Invalid ID.")
        return
    new_avail = input("New available copies (int): ").strip()
    try:
        update_available_copies(bid, int(new_avail))
        print("Updated available copies.")
    except Exception as e:
        print("Error:", e)

def delete_book_cli():
    bid = prompt_int("Book ID to delete: ")
    if bid is None:
        print("Invalid ID.")
        return
    try:
        delete_book(bid)
        print("Book deleted.")
    except Exception as e:
        print("Error:", e)

def update_borrow_cli():
    rid = prompt_int("Borrow record ID to update: ")
    if rid is None:
        print("Invalid ID.")
        return
    mid = prompt_int("New member ID (leave blank to skip): ")
    bid = prompt_int("New book ID (leave blank to skip): ")
    borrow_date = input("New borrow date (YYYY-MM-DD) leave blank to skip: ").strip() or None
    return_date = input("New return date (YYYY-MM-DD) leave blank to skip: ").strip() or None
    status = input("New status (Borrowed/Returned) leave blank to auto-set: ").strip() or None
    try:
        update_borrow_record(
            rid,
            member_id=mid,
            book_id=bid,
            borrow_date=borrow_date if borrow_date else None,
            return_date=return_date if return_date else None,
            status=status
        )
        print("Borrow record updated.")
    except Exception as e:
        print("Error:", e)

def delete_borrow_cli():
    rid = prompt_int("Borrow record ID to delete: ")
    if rid is None:
        print("Invalid ID.")
        return
    try:
        delete_borrow_record(rid)
        print("Borrow record deleted.")
    except Exception as e:
        print("Error:", e)

def show_borrow_count_per_member():
    rows = get_borrow_count_per_member()
    print("MemberID | MemberName | CurrentlyBorrowed")
    for r in rows:
        print(r)

def menu():
    actions = {
        "1": ("Add member", add_member),
        "2": ("Add book", add_book),
        "3": ("Create borrow record", create_borrow),
        "4": ("View all borrow records (details)", view_all_borrows_details),
        "5": ("View all borrow records (raw)", view_all_borrows),
        "6": ("View member borrow history", view_member_history),
        "7": ("Mark book returned", mark_returned),
        "8": ("Update member", update_member_cli),
        "9": ("Delete member", delete_member_cli),
        "10": ("Update book info", update_book_cli),
        "11": ("Update book available copies", update_book_copies_cli),
        "12": ("Delete book", delete_book_cli),
        "13": ("Update borrow record", update_borrow_cli),
        "14": ("Delete borrow record", delete_borrow_cli),
        "15": ("Show number of books currently borrowed per member", show_borrow_count_per_member),
        "0": ("Exit", lambda: sys.exit(0))
    }

    while True:
        print("\n--- Library Management ---")
        for k, v in actions.items():
            print(f"{k}. {v[0]}")
        choice = input("Choose: ").strip()
        action = actions.get(choice)
        if action:
            try:
                action[1]()
            except Exception as e:
                print("Error during operation:", e)
        else:
            print("Invalid option.")

if __name__ == "__main__":
    menu()
