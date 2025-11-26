# from db import get_connection

# def create_book(title, author, category, total_copies, available_copies):
#     conn = get_connection()
#     cur = conn.cursor()
#     try:
#         cur.execute(
#             "INSERT INTO books (title, author, category, total_copies, available_copies) "
#             "VALUES (%s, %s, %s, %s, %s) RETURNING id",
#             (title, author, category, total_copies, available_copies)
#         )
#         new_id = cur.fetchone()[0]
#         conn.commit()
#         return new_id
#     except Exception as e:
#         conn.rollback()
#         raise e
#     finally:
#         cur.close()
#         conn.close()

# def get_all_books():
#     conn = get_connection()
#     cur = conn.cursor()
#     cur.execute("SELECT id, title, author, category, total_copies, available_copies FROM books ORDER BY id")
#     rows = cur.fetchall()
#     cur.close()
#     conn.close()
#     return rows

# def get_book_by_id(book_id):
#     conn = get_connection()
#     cur = conn.cursor()
#     cur.execute(
#         "SELECT id, title, author, category, total_copies, available_copies FROM books WHERE id = %s",
#         (book_id,)
#     )
#     row = cur.fetchone()
#     cur.close()
#     conn.close()
#     return row

# def update_book(book_id, title=None, author=None, category=None):
#     conn = get_connection()
#     cur = conn.cursor()
#     try:
#         updates = []
#         params = []
#         if title is not None:
#             updates.append("title = %s")
#             params.append(title)
#         if author is not None:
#             updates.append("author = %s")
#             params.append(author)
#         if category is not None:
#             updates.append("category = %s")
#             params.append(category)
#         params.append(book_id)

#         sql = f"UPDATE books SET {', '.join(updates)} WHERE id = %s"
#         cur.execute(sql, params)
#         conn.commit()
#     except Exception as e:
#         conn.rollback()
#         raise e
#     finally:
#         cur.close()
#         conn.close()

# def update_available_copies(book_id, new_available):
#     conn = get_connection()
#     cur = conn.cursor()
#     try:
#         cur.execute(
#             "UPDATE books SET available_copies = %s WHERE id = %s",
#             (new_available, book_id)
#         )
#         conn.commit()
#     except Exception as e:
#         conn.rollback()
#         raise e
#     finally:
#         cur.close()
#         conn.close()

# def delete_book(book_id):
#     conn = get_connection()
#     cur = conn.cursor()
#     try:
#         cur.execute("DELETE FROM books WHERE id = %s", (book_id,))
#         conn.commit()
#     except Exception as e:
#         conn.rollback()
#         raise e
#     finally:
#         cur.close()
#         conn.close()

# /mnt/data/books.py
from db import get_connection

def create_book(title, author, category, total_copies, available_copies):
    conn = get_connection()
    cur = conn.cursor()
    try:
        cur.execute(
            "INSERT INTO books (title, author, category, total_copies, available_copies) "
            "VALUES (%s, %s, %s, %s, %s) RETURNING id",
            (title, author, category, total_copies, available_copies)
        )
        new_id = cur.fetchone()[0]
        conn.commit()
        return new_id
    except Exception as e:
        conn.rollback()
        raise e
    finally:
        cur.close()
        conn.close()

def get_all_books():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT id, title, author, category, total_copies, available_copies FROM books ORDER BY id")
    rows = cur.fetchall()
    cur.close()
    conn.close()
    return rows

def get_book_by_id(book_id):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute(
        "SELECT id, title, author, category, total_copies, available_copies FROM books WHERE id = %s",
        (book_id,)
    )
    row = cur.fetchone()
    cur.close()
    conn.close()
    return row

def update_book(book_id, title=None, author=None, category=None):
    conn = get_connection()
    cur = conn.cursor()
    try:
        updates = []
        params = []
        if title is not None:
            updates.append("title = %s")
            params.append(title)
        if author is not None:
            updates.append("author = %s")
            params.append(author)
        if category is not None:
            updates.append("category = %s")
            params.append(category)
        if not updates:
            return
        params.append(book_id)

        sql = f"UPDATE books SET {', '.join(updates)} WHERE id = %s"
        cur.execute(sql, params)
        conn.commit()
    except Exception as e:
        conn.rollback()
        raise e
    finally:
        cur.close()
        conn.close()

def update_available_copies(book_id, new_available):
    conn = get_connection()
    cur = conn.cursor()
    try:
        cur.execute(
            "UPDATE books SET available_copies = %s WHERE id = %s",
            (new_available, book_id)
        )
        conn.commit()
    except Exception as e:
        conn.rollback()
        raise e
    finally:
        cur.close()
        conn.close()

def delete_book(book_id):
    conn = get_connection()
    cur = conn.cursor()
    try:
        # Prevent deleting if there are currently borrowed copies of this book
        cur.execute(
            "SELECT COUNT(*) FROM borrow_records WHERE book_id = %s AND status = %s",
            (book_id, "Borrowed")
        )
        count = cur.fetchone()[0]
        if count > 0:
            raise ValueError("Cannot delete book: there are active borrow records for this book.")
        cur.execute("DELETE FROM books WHERE id = %s", (book_id,))
        conn.commit()
    except Exception as e:
        conn.rollback()
        raise e
    finally:
        cur.close()
        conn.close()
