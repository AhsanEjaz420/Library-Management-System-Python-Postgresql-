# import tkinter as tk
# from tkinter import ttk, messagebox

# # Import your business logic (CRUD functions)
# from models.members import create_member, get_all_members, get_member_by_id
# from models.books import create_book, get_all_books, get_book_by_id

# class LibraryApp(tk.Tk):
#     def __init__(self):
#         super().__init__()
#         self.title("Library Management System")

#         # Create notebook (tabs)
#         self.notebook = ttk.Notebook(self)
#         self.notebook.pack(padx=10, pady=10, fill="both", expand=True)

#         self.member_frame = ttk.Frame(self.notebook)
#         self.book_frame = ttk.Frame(self.notebook)

#         self.notebook.add(self.member_frame, text="Members")
#         self.notebook.add(self.book_frame, text="Books")

#         self._build_member_tab()
#         self._build_book_tab()

#         self.status_label = tk.Label(self, text="", fg="green")
#         self.status_label.pack(pady=5)

#     def _build_member_tab(self):
#         frame = self.member_frame

#         # Add Member form
#         ttk.Label(frame, text="Name:").grid(row=0, column=0, sticky="e")
#         self.name_entry = ttk.Entry(frame)
#         self.name_entry.grid(row=0, column=1)

#         ttk.Label(frame, text="Phone:").grid(row=1, column=0, sticky="e")
#         self.phone_entry = ttk.Entry(frame)
#         self.phone_entry.grid(row=1, column=1)

#         ttk.Label(frame, text="Email:").grid(row=2, column=0, sticky="e")
#         self.email_entry = ttk.Entry(frame)
#         self.email_entry.grid(row=2, column=1)

#         add_btn = ttk.Button(frame, text="Add Member", command=self.add_member)
#         add_btn.grid(row=3, column=0, columnspan=2, pady=5)

#         # View all members
#         view_all_btn = ttk.Button(frame, text="View All Members", command=self.view_all_members)
#         view_all_btn.grid(row=4, column=0, columnspan=2, pady=(10, 5))

#         self.members_list = tk.Listbox(frame, height=8, width=50)
#         self.members_list.grid(row=5, column=0, columnspan=2, pady=5)

#         # View by ID
#         ttk.Label(frame, text="Member ID:").grid(row=6, column=0, sticky="e")
#         self.member_id_entry = ttk.Entry(frame)
#         self.member_id_entry.grid(row=6, column=1)

#         view_btn = ttk.Button(frame, text="View Member", command=self.view_member_by_id)
#         view_btn.grid(row=7, column=0, columnspan=2, pady=5)

#     def _build_book_tab(self):
#         frame = self.book_frame

#         # Add Book form
#         ttk.Label(frame, text="Title:").grid(row=0, column=0, sticky="e")
#         self.title_entry = ttk.Entry(frame)
#         self.title_entry.grid(row=0, column=1)

#         ttk.Label(frame, text="Author:").grid(row=1, column=0, sticky="e")
#         self.author_entry = ttk.Entry(frame)
#         self.author_entry.grid(row=1, column=1)

#         ttk.Label(frame, text="Category:").grid(row=2, column=0, sticky="e")
#         self.category_entry = ttk.Entry(frame)
#         self.category_entry.grid(row=2, column=1)

#         ttk.Label(frame, text="Total Copies:").grid(row=3, column=0, sticky="e")
#         self.total_entry = ttk.Entry(frame)
#         self.total_entry.grid(row=3, column=1)

#         ttk.Label(frame, text="Available Copies:").grid(row=4, column=0, sticky="e")
#         self.available_entry = ttk.Entry(frame)
#         self.available_entry.grid(row=4, column=1)

#         add_btn = ttk.Button(frame, text="Add Book", command=self.add_book)
#         add_btn.grid(row=5, column=0, columnspan=2, pady=5)

#         view_all_btn = ttk.Button(frame, text="View All Books", command=self.view_all_books)
#         view_all_btn.grid(row=6, column=0, columnspan=2, pady=(10, 5))

#         self.books_list = tk.Listbox(frame, height=8, width=60)
#         self.books_list.grid(row=7, column=0, columnspan=2, pady=5)

#         ttk.Label(frame, text="Book ID:").grid(row=8, column=0, sticky="e")
#         self.book_id_entry = ttk.Entry(frame)
#         self.book_id_entry.grid(row=8, column=1)

#         view_btn = ttk.Button(frame, text="View Book", command=self.view_book_by_id)
#         view_btn.grid(row=9, column=0, columnspan=2, pady=5)

#     # --- Event Handlers ---
#     def add_member(self):
#         name = self.name_entry.get()
#         phone = self.phone_entry.get()
#         email = self.email_entry.get()
#         try:
#             member_id = create_member(name, phone, email)
#             self.status_label.config(text=f"Member added with ID: {member_id}", fg="green")
#             self.name_entry.delete(0, tk.END)
#             self.phone_entry.delete(0, tk.END)
#             self.email_entry.delete(0, tk.END)
#         except Exception as e:
#             messagebox.showerror("Error", str(e))
#             self.status_label.config(text="Failed to add member", fg="red")

#     def view_all_members(self):
#         self.members_list.delete(0, tk.END)
#         for m in get_all_members():
#             self.members_list.insert(tk.END, str(m))

#     def view_member_by_id(self):
#         mid = self.member_id_entry.get()
#         try:
#             member = get_member_by_id(int(mid))
#             self.members_list.delete(0, tk.END)
#             self.members_list.insert(tk.END, str(member))
#         except Exception as e:
#             messagebox.showerror("Error", str(e))

#     def add_book(self):
#         title = self.title_entry.get()
#         author = self.author_entry.get()
#         category = self.category_entry.get()
#         total = self.total_entry.get()
#         available = self.available_entry.get()
#         try:
#             book_id = create_book(title, author, category, int(total), int(available))
#             self.status_label.config(text=f"Book added with ID: {book_id}", fg="green")
#             self.title_entry.delete(0, tk.END)
#             self.author_entry.delete(0, tk.END)
#             self.category_entry.delete(0, tk.END)
#             self.total_entry.delete(0, tk.END)
#             self.available_entry.delete(0, tk.END)
#         except Exception as e:
#             messagebox.showerror("Error", str(e))
#             self.status_label.config(text="Failed to add book", fg="red")

#     def view_all_books(self):
#         self.books_list.delete(0, tk.END)
#         for b in get_all_books():
#             self.books_list.insert(tk.END, str(b))

#     def view_book_by_id(self):
#         bid = self.book_id_entry.get()
#         try:
#             book = get_book_by_id(int(bid))
#             self.books_list.delete(0, tk.END)
#             self.books_list.insert(tk.END, str(book))
#         except Exception as e:
#             messagebox.showerror("Error", str(e))


# if __name__ == "__main__":
#     app = LibraryApp()
#     app.mainloop()

# /mnt/data/main_gui.py
import tkinter as tk
from tkinter import ttk, messagebox, simpledialog
from datetime import datetime

# Import model functions (assumes these modules are in project root)
from models.members import (
    create_member, get_all_members, get_member_by_id,
    update_member, delete_member
)
from models.books import (
    create_book, get_all_books, get_book_by_id,
    update_book, update_available_copies, delete_book
)
from models.borrow_records import (
    create_borrow_record, get_all_borrow_records_with_details,
    get_all_borrow_records, get_borrow_history_for_member,
    mark_as_returned, update_borrow_record, delete_borrow_record,
    get_borrow_count_per_member
)


class LibraryGUI(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Library Management — GUI")
        self.geometry("1000x650")
        self._build_ui()

    def _build_ui(self):
        notebook = ttk.Notebook(self)
        notebook.pack(fill="both", expand=True, padx=8, pady=8)

        self.members_tab = ttk.Frame(notebook)
        self.books_tab = ttk.Frame(notebook)
        self.borrow_tab = ttk.Frame(notebook)
        self.reports_tab = ttk.Frame(notebook)

        notebook.add(self.members_tab, text="Members")
        notebook.add(self.books_tab, text="Books")
        notebook.add(self.borrow_tab, text="Borrowing")
        notebook.add(self.reports_tab, text="Reports")

        self._build_members_tab()
        self._build_books_tab()
        self._build_borrow_tab()
        self._build_reports_tab()

    # ---------------- Members Tab ----------------
    def _build_members_tab(self):
        frame = self.members_tab

        form = ttk.LabelFrame(frame, text="Add / Update Member")
        form.pack(fill="x", padx=8, pady=6)

        ttk.Label(form, text="Name").grid(row=0, column=0, sticky="e", padx=4, pady=4)
        self.m_name = ttk.Entry(form, width=30)
        self.m_name.grid(row=0, column=1, padx=4, pady=4)

        ttk.Label(form, text="Phone").grid(row=1, column=0, sticky="e", padx=4, pady=4)
        self.m_phone = ttk.Entry(form, width=30)
        self.m_phone.grid(row=1, column=1, padx=4, pady=4)

        ttk.Label(form, text="Email").grid(row=2, column=0, sticky="e", padx=4, pady=4)
        self.m_email = ttk.Entry(form, width=30)
        self.m_email.grid(row=2, column=1, padx=4, pady=4)

        btn_frame = ttk.Frame(form)
        btn_frame.grid(row=3, column=0, columnspan=2, pady=6)

        ttk.Button(btn_frame, text="Add Member", command=self.add_member).pack(side="left", padx=6)
        ttk.Button(btn_frame, text="Update Selected", command=self.update_member_cli).pack(side="left", padx=6)
        ttk.Button(btn_frame, text="Delete Selected", command=self.delete_member_cli).pack(side="left", padx=6)
        ttk.Button(btn_frame, text="Refresh", command=self.reload_members).pack(side="left", padx=6)

        # Members list
        tree_frame = ttk.LabelFrame(frame, text="Members List")
        tree_frame.pack(fill="both", expand=True, padx=8, pady=6)

        cols = ("id", "name", "phone", "email")
        self.members_tree = ttk.Treeview(tree_frame, columns=cols, show="headings", selectmode="browse")
        for c in cols:
            self.members_tree.heading(c, text=c.title())
            self.members_tree.column(c, width=150, anchor="w")
        self.members_tree.pack(fill="both", expand=True, padx=4, pady=4)
        self.members_tree.bind("<<TreeviewSelect>>", self.on_member_select)

        self.reload_members()

    def add_member(self):
        name = self.m_name.get().strip()
        phone = self.m_phone.get().strip()
        email = self.m_email.get().strip()
        if not name:
            messagebox.showwarning("Validation", "Name is required.")
            return
        try:
            mid = create_member(name, phone, email)
            messagebox.showinfo("Success", f"Member created with ID {mid}")
            self.m_name.delete(0, tk.END)
            self.m_phone.delete(0, tk.END)
            self.m_email.delete(0, tk.END)
            self.reload_members()
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def reload_members(self):
        for r in self.members_tree.get_children():
            self.members_tree.delete(r)
        try:
            for m in get_all_members():
                # m expected as tuple (id, name, phone, email)
                self.members_tree.insert("", tk.END, values=m)
        except Exception as e:
            messagebox.showerror("Error loading members", str(e))

    def on_member_select(self, event):
        sel = self.members_tree.selection()
        if not sel:
            return
        vals = self.members_tree.item(sel[0], "values")
        # Fill form with selected
        self.m_name.delete(0, tk.END); self.m_name.insert(0, vals[1])
        self.m_phone.delete(0, tk.END); self.m_phone.insert(0, vals[2])
        self.m_email.delete(0, tk.END); self.m_email.insert(0, vals[3])

    def update_member_cli(self):
        sel = self.members_tree.selection()
        if not sel:
            messagebox.showwarning("Selection", "Select a member to update.")
            return
        member_id = int(self.members_tree.item(sel[0], "values")[0])
        name = self.m_name.get().strip() or None
        phone = self.m_phone.get().strip() or None
        email = self.m_email.get().strip() or None
        try:
            update_member(member_id, name=name, phone=phone, email=email)
            messagebox.showinfo("Success", "Member updated.")
            self.reload_members()
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def delete_member_cli(self):
        sel = self.members_tree.selection()
        if not sel:
            messagebox.showwarning("Selection", "Select a member to delete.")
            return
        member_id = int(self.members_tree.item(sel[0], "values")[0])
        if not messagebox.askyesno("Confirm", f"Delete member ID {member_id}?"):
            return
        try:
            delete_member(member_id)
            messagebox.showinfo("Deleted", "Member deleted.")
            self.reload_members()
        except Exception as e:
            messagebox.showerror("Error", str(e))

    # ---------------- Books Tab ----------------
    def _build_books_tab(self):
        frame = self.books_tab

        form = ttk.LabelFrame(frame, text="Add / Update Book")
        form.pack(fill="x", padx=8, pady=6)

        ttk.Label(form, text="Title").grid(row=0, column=0, sticky="e", padx=4, pady=4)
        self.b_title = ttk.Entry(form, width=35)
        self.b_title.grid(row=0, column=1, padx=4, pady=4)

        ttk.Label(form, text="Author").grid(row=1, column=0, sticky="e", padx=4, pady=4)
        self.b_author = ttk.Entry(form, width=35)
        self.b_author.grid(row=1, column=1, padx=4, pady=4)

        ttk.Label(form, text="Category").grid(row=2, column=0, sticky="e", padx=4, pady=4)
        self.b_category = ttk.Entry(form, width=35)
        self.b_category.grid(row=2, column=1, padx=4, pady=4)

        ttk.Label(form, text="Total Copies").grid(row=0, column=2, sticky="e", padx=4, pady=4)
        self.b_total = ttk.Entry(form, width=10)
        self.b_total.grid(row=0, column=3, padx=4, pady=4)

        ttk.Label(form, text="Available Copies").grid(row=1, column=2, sticky="e", padx=4, pady=4)
        self.b_available = ttk.Entry(form, width=10)
        self.b_available.grid(row=1, column=3, padx=4, pady=4)

        btn_frame = ttk.Frame(form)
        btn_frame.grid(row=3, column=0, columnspan=4, pady=6)

        ttk.Button(btn_frame, text="Add Book", command=self.add_book).pack(side="left", padx=6)
        ttk.Button(btn_frame, text="Update Selected", command=self.update_book_cli).pack(side="left", padx=6)
        ttk.Button(btn_frame, text="Update Available Copies", command=self.update_book_available_cli).pack(side="left", padx=6)
        ttk.Button(btn_frame, text="Delete Selected", command=self.delete_book_cli).pack(side="left", padx=6)
        ttk.Button(btn_frame, text="Refresh", command=self.reload_books).pack(side="left", padx=6)

        # Books list
        tree_frame = ttk.LabelFrame(frame, text="Books List")
        tree_frame.pack(fill="both", expand=True, padx=8, pady=6)

        cols = ("id", "title", "author", "category", "total", "available")
        self.books_tree = ttk.Treeview(tree_frame, columns=cols, show="headings", selectmode="browse")
        headings = ["ID", "Title", "Author", "Category", "Total Copies", "Available Copies"]
        for c, h in zip(cols, headings):
            self.books_tree.heading(c, text=h)
            if c in ("title",):
                self.books_tree.column(c, width=300, anchor="w")
            else:
                self.books_tree.column(c, width=100, anchor="w")
        self.books_tree.pack(fill="both", expand=True, padx=4, pady=4)
        self.books_tree.bind("<<TreeviewSelect>>", self.on_book_select)

        self.reload_books()

    def add_book(self):
        title = self.b_title.get().strip()
        author = self.b_author.get().strip()
        category = self.b_category.get().strip()
        total = self.b_total.get().strip()
        available = self.b_available.get().strip()

        if not title:
            messagebox.showwarning("Validation", "Title is required.")
            return
        try:
            total_i = int(total) if total else 1
            avail_i = int(available) if available else total_i
        except ValueError:
            messagebox.showwarning("Validation", "Total and Available must be integers.")
            return

        try:
            bid = create_book(title, author, category, total_i, avail_i)
            messagebox.showinfo("Success", f"Book created with ID {bid}")
            self.clear_book_form()
            self.reload_books()
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def reload_books(self):
        for r in self.books_tree.get_children():
            self.books_tree.delete(r)
        try:
            for b in get_all_books():
                # (id, title, author, category, total_copies, available_copies)
                self.books_tree.insert("", tk.END, values=b)
        except Exception as e:
            messagebox.showerror("Error loading books", str(e))

    def on_book_select(self, event):
        sel = self.books_tree.selection()
        if not sel:
            return
        vals = self.books_tree.item(sel[0], "values")
        self.b_title.delete(0, tk.END); self.b_title.insert(0, vals[1])
        self.b_author.delete(0, tk.END); self.b_author.insert(0, vals[2])
        self.b_category.delete(0, tk.END); self.b_category.insert(0, vals[3])
        self.b_total.delete(0, tk.END); self.b_total.insert(0, vals[4])
        self.b_available.delete(0, tk.END); self.b_available.insert(0, vals[5])

    def clear_book_form(self):
        self.b_title.delete(0, tk.END)
        self.b_author.delete(0, tk.END)
        self.b_category.delete(0, tk.END)
        self.b_total.delete(0, tk.END)
        self.b_available.delete(0, tk.END)

    def update_book_cli(self):
        sel = self.books_tree.selection()
        if not sel:
            messagebox.showwarning("Selection", "Select a book to update.")
            return
        book_id = int(self.books_tree.item(sel[0], "values")[0])
        title = self.b_title.get().strip() or None
        author = self.b_author.get().strip() or None
        category = self.b_category.get().strip() or None
        try:
            update_book(book_id, title=title, author=author, category=category)
            messagebox.showinfo("Success", "Book updated.")
            self.reload_books()
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def update_book_available_cli(self):
        sel = self.books_tree.selection()
        if not sel:
            messagebox.showwarning("Selection", "Select a book to update available copies.")
            return
        book_id = int(self.books_tree.item(sel[0], "values")[0])
        new_avail = simpledialog.askstring("Available Copies", "Enter new available copies (integer):", parent=self)
        if new_avail is None:
            return
        try:
            new_avail_i = int(new_avail)
            update_available_copies(book_id, new_avail_i)
            messagebox.showinfo("Success", "Available copies updated.")
            self.reload_books()
        except ValueError:
            messagebox.showwarning("Validation", "Enter a valid integer.")
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def delete_book_cli(self):
        sel = self.books_tree.selection()
        if not sel:
            messagebox.showwarning("Selection", "Select a book to delete.")
            return
        book_id = int(self.books_tree.item(sel[0], "values")[0])
        if not messagebox.askyesno("Confirm", f"Delete book ID {book_id}?"):
            return
        try:
            delete_book(book_id)
            messagebox.showinfo("Deleted", "Book deleted.")
            self.reload_books()
        except Exception as e:
            messagebox.showerror("Error", str(e))

    # ---------------- Borrow Tab ----------------
    def _build_borrow_tab(self):
        frame = self.borrow_tab

        form = ttk.LabelFrame(frame, text="Borrow / Return / Update Borrow")
        form.pack(fill="x", padx=8, pady=6)

        ttk.Label(form, text="Member ID").grid(row=0, column=0, padx=4, pady=4, sticky="e")
        self.br_member = ttk.Entry(form, width=12)
        self.br_member.grid(row=0, column=1, padx=4, pady=4)

        ttk.Label(form, text="Book ID").grid(row=0, column=2, padx=4, pady=4, sticky="e")
        self.br_book = ttk.Entry(form, width=12)
        self.br_book.grid(row=0, column=3, padx=4, pady=4)

        ttk.Button(form, text="Borrow Book", command=self.borrow_book_cli).grid(row=0, column=4, padx=8, pady=4)
        ttk.Button(form, text="Mark Selected Returned", command=self.mark_selected_returned).grid(row=0, column=5, padx=8, pady=4)
        ttk.Button(form, text="Refresh", command=self.reload_borrows).grid(row=0, column=6, padx=8, pady=4)

        ttk.Label(form, text="Record ID (for update/delete)").grid(row=1, column=0, padx=4, pady=6, sticky="e")
        self.br_record_id = ttk.Entry(form, width=12)
        self.br_record_id.grid(row=1, column=1, padx=4, pady=6)

        ttk.Button(form, text="Update Borrow", command=self.update_borrow_cli).grid(row=1, column=2, padx=6)
        ttk.Button(form, text="Delete Borrow", command=self.delete_borrow_cli).grid(row=1, column=3, padx=6)
        ttk.Button(form, text="Member History", command=self.open_member_history).grid(row=1, column=4, padx=6)

        # Borrow records list (joined details)
        tree_frame = ttk.LabelFrame(frame, text="Borrow Records (with Member & Book details)")
        tree_frame.pack(fill="both", expand=True, padx=8, pady=6)

        cols = ("record_id", "member_id", "member_name", "book_id", "book_title", "borrow_date", "return_date", "status")
        self.borrow_tree = ttk.Treeview(tree_frame, columns=cols, show="headings", selectmode="browse")
        headings = ["Record ID", "Member ID", "Member Name", "Book ID", "Book Title", "Borrow Date", "Return Date", "Status"]
        for c, h in zip(cols, headings):
            self.borrow_tree.heading(c, text=h)
            if c in ("member_name", "book_title"):
                self.borrow_tree.column(c, width=240, anchor="w")
            else:
                self.borrow_tree.column(c, width=110, anchor="w")
        self.borrow_tree.pack(fill="both", expand=True, padx=4, pady=4)
        self.borrow_tree.bind("<<TreeviewSelect>>", self.on_borrow_select)

        self.reload_borrows()

    def borrow_book_cli(self):
        mid = self.br_member.get().strip()
        bid = self.br_book.get().strip()
        if not (mid.isdigit() and bid.isdigit()):
            messagebox.showwarning("Validation", "Member ID and Book ID must be integers.")
            return
        try:
            rid = create_borrow_record(int(mid), int(bid))
            messagebox.showinfo("Success", f"Borrow record created ID {rid}")
            self.br_member.delete(0, tk.END)
            self.br_book.delete(0, tk.END)
            self.reload_borrows()
            self.reload_books()
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def reload_borrows(self):
        for r in self.borrow_tree.get_children():
            self.borrow_tree.delete(r)
        try:
            for rec in get_all_borrow_records_with_details():
                # rec: (record_id, member_id, member_name, book_id, book_title, borrow_date, return_date, status)
                self.borrow_tree.insert("", tk.END, values=rec)
        except Exception as e:
            messagebox.showerror("Error loading borrow records", str(e))

    def on_borrow_select(self, event):
        sel = self.borrow_tree.selection()
        if not sel:
            return
        vals = self.borrow_tree.item(sel[0], "values")
        # Fill record id entry and optionally show details
        self.br_record_id.delete(0, tk.END)
        self.br_record_id.insert(0, vals[0])

    def mark_selected_returned(self):
        sel = self.borrow_tree.selection()
        if not sel:
            messagebox.showwarning("Selection", "Select a borrow record to mark returned.")
            return
        record_id = int(self.borrow_tree.item(sel[0], "values")[0])
        if not messagebox.askyesno("Confirm", f"Mark record {record_id} as returned?"):
            return
        try:
            mark_as_returned(record_id)
            messagebox.showinfo("Success", "Marked as returned.")
            self.reload_borrows()
            self.reload_books()
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def open_member_history(self):
        mid = simpledialog.askstring("Member History", "Enter Member ID:", parent=self)
        if mid is None or not mid.isdigit():
            return
        mid_i = int(mid)
        try:
            rows = get_borrow_history_for_member(mid_i)
        except Exception as e:
            messagebox.showerror("Error", str(e))
            return

        # open small window with history tree
        w = tk.Toplevel(self)
        w.title(f"Borrow History — Member {mid_i}")
        cols = ("id", "book_id", "borrow_date", "return_date", "status")
        tree = ttk.Treeview(w, columns=cols, show="headings")
        for c in cols:
            tree.heading(c, text=c.title())
            tree.column(c, width=140, anchor="w")
        for r in rows:
            tree.insert("", tk.END, values=r)
        tree.pack(fill="both", expand=True, padx=8, pady=8)

    def update_borrow_cli(self):
        rid_val = self.br_record_id.get().strip()
        if not rid_val.isdigit():
            messagebox.showwarning("Validation", "Enter a valid Record ID to update.")
            return
        rid = int(rid_val)
        # prompt for fields to change
        new_mid = simpledialog.askstring("Update Borrow", "New Member ID (leave blank to skip):", parent=self)
        new_bid = simpledialog.askstring("Update Borrow", "New Book ID (leave blank to skip):", parent=self)
        new_borrow_date = simpledialog.askstring("Update Borrow", "New borrow date YYYY-MM-DD (leave blank to skip):", parent=self)
        new_return_date = simpledialog.askstring("Update Borrow", "New return date YYYY-MM-DD (leave blank to skip):", parent=self)
        new_status = simpledialog.askstring("Update Borrow", "New status (Borrowed/Returned) (leave blank to auto-set):", parent=self)

        def parse_int_or_none(s):
            return int(s) if s and s.isdigit() else None

        try:
            update_borrow_record(
                rid,
                member_id=parse_int_or_none(new_mid),
                book_id=parse_int_or_none(new_bid),
                borrow_date=new_borrow_date or None,
                return_date=new_return_date or None,
                status=new_status or None
            )
            messagebox.showinfo("Success", "Borrow record updated.")
            self.reload_borrows()
            self.reload_books()
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def delete_borrow_cli(self):
        rid_val = self.br_record_id.get().strip()
        if not rid_val.isdigit():
            messagebox.showwarning("Validation", "Enter a valid Record ID to delete.")
            return
        rid = int(rid_val)
        if not messagebox.askyesno("Confirm", f"Delete borrow record {rid}?"):
            return
        try:
            delete_borrow_record(rid)
            messagebox.showinfo("Deleted", "Borrow record deleted.")
            self.reload_borrows()
            self.reload_books()
        except Exception as e:
            messagebox.showerror("Error", str(e))

    # ---------------- Reports Tab ----------------
    def _build_reports_tab(self):
        frame = self.reports_tab

        ttk.Button(frame, text="Refresh Reports", command=self.reload_reports).pack(pady=8)

        # Borrow counts per member
        bor_frame = ttk.LabelFrame(frame, text="Currently Borrowed Count per Member")
        bor_frame.pack(fill="both", expand=True, padx=8, pady=6)

        cols = ("member_id", "member_name", "borrowed_count")
        self.borrowcount_tree = ttk.Treeview(bor_frame, columns=cols, show="headings")
        headings = ["Member ID", "Member Name", "Currently Borrowed"]
        for c, h in zip(cols, headings):
            self.borrowcount_tree.heading(c, text=h)
            self.borrowcount_tree.column(c, width=200, anchor="w")
        self.borrowcount_tree.pack(fill="both", expand=True, padx=4, pady=4)

        # Quick raw list of borrow records
        raw_frame = ttk.LabelFrame(frame, text="Raw Borrow Records (preview)")
        raw_frame.pack(fill="both", expand=True, padx=8, pady=6)

        cols2 = ("id", "member_id", "book_id", "borrow_date", "return_date", "status")
        self.rawborrow_tree = ttk.Treeview(raw_frame, columns=cols2, show="headings")
        for c in cols2:
            self.rawborrow_tree.heading(c, text=c.title())
            self.rawborrow_tree.column(c, width=130, anchor="w")
        self.rawborrow_tree.pack(fill="both", expand=True, padx=4, pady=4)

        self.reload_reports()

    def reload_reports(self):
        # borrow counts
        for r in self.borrowcount_tree.get_children():
            self.borrowcount_tree.delete(r)
        for r in self.rawborrow_tree.get_children():
            self.rawborrow_tree.delete(r)

        try:
            for row in get_borrow_count_per_member():
                # (member_id, member_name, borrowed_count)
                self.borrowcount_tree.insert("", tk.END, values=row)
            for row in get_all_borrow_records():
                self.rawborrow_tree.insert("", tk.END, values=row)
        except Exception as e:
            messagebox.showerror("Error loading reports", str(e))

# Entry point
if __name__ == "__main__":
    app = LibraryGUI()
    app.mainloop()
