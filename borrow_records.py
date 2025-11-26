# from db import get_connection
# from datetime import date

# def create_borrow_record(member_id, book_id, borrow_date=None, return_date=None, status="Borrowed"):
#     conn = get_connection()
#     cur = conn.cursor()
#     try:
#         if borrow_date is None:
#             borrow_date = date.today()
#         cur.execute(
#             "INSERT INTO borrow_records (member_id, book_id, borrow_date, return_date, status) "
#             "VALUES (%s, %s, %s, %s, %s) RETURNING id",
#             (member_id, book_id, borrow_date, return_date, status)
#         )
#         new_id = cur.fetchone()[0]

#         # Automatically reduce available_copies of the book
#         cur.execute(
#             "UPDATE books SET available_copies = available_copies - 1 WHERE id = %s",
#             (book_id,)
#         )

#         conn.commit()
#         return new_id
#     except Exception as e:
#         conn.rollback()
#         raise e
#     finally:
#         cur.close()
#         conn.close()


# def get_all_borrow_records():
#     conn = get_connection()
#     cur = conn.cursor()
#     cur.execute(
#         "SELECT id, member_id, book_id, borrow_date, return_date, status "
#         "FROM borrow_records ORDER BY id"
#     )
#     rows = cur.fetchall()
#     cur.close()
#     conn.close()
#     return rows

# def get_borrow_history_for_member(member_id):
#     conn = get_connection()
#     cur = conn.cursor()
#     cur.execute(
#         "SELECT id, book_id, borrow_date, return_date, status "
#         "FROM borrow_records WHERE member_id = %s ORDER BY borrow_date",
#         (member_id,)
#     )
#     rows = cur.fetchall()
#     cur.close()
#     conn.close()
#     return rows

# def mark_as_returned(record_id, return_date=None):
#     conn = get_connection()
#     cur = conn.cursor()
#     try:
#         if return_date is None:
#             return_date = date.today()
#         # Update the record
#         cur.execute(
#             "UPDATE borrow_records SET return_date = %s, status = %s WHERE id = %s",
#             (return_date, "Returned", record_id)
#         )

#         # Increase available_copies for the book
#         cur.execute(
#             "UPDATE books SET available_copies = available_copies + 1 "
#             "WHERE id = (SELECT book_id FROM borrow_records WHERE id = %s)",
#             (record_id,)
#         )

#         conn.commit()
#     except Exception as e:
#         conn.rollback()
#         raise e
#     finally:
#         cur.close()
#         conn.close()

# def update_borrow_record(record_id, member_id=None, book_id=None, borrow_date=None, return_date=None, status=None):
#     conn = get_connection()
#     cur = conn.cursor()
#     try:
#         # First fetch old values
#         cur.execute("SELECT member_id, book_id FROM borrow_records WHERE id = %s", (record_id,))
#         old = cur.fetchone()
#         old_member, old_book = old

#         updates = []
#         params = []
#         if member_id is not None:
#             updates.append("member_id = %s")
#             params.append(member_id)
#         if book_id is not None:
#             updates.append("book_id = %s")
#             params.append(book_id)
#         if borrow_date is not None:
#             updates.append("borrow_date = %s")
#             params.append(borrow_date)
#         if return_date is not None:
#             updates.append("return_date = %s")
#             params.append(return_date)
#         if status is not None:
#             updates.append("status = %s")
#             params.append(status)

#         params.append(record_id)
#         sql = f"UPDATE borrow_records SET {', '.join(updates)} WHERE id = %s"
#         cur.execute(sql, params)

#         # If book has changed, adjust available copies
#         if book_id is not None and book_id != old_book:
#             # give back one copy to the old book
#             cur.execute(
#                 "UPDATE books SET available_copies = available_copies + 1 WHERE id = %s",
#                 (old_book,)
#             )
#             # reduce one copy from the new book
#             cur.execute(
#                 "UPDATE books SET available_copies = available_copies - 1 WHERE id = %s",
#                 (book_id,)
#             )

#         conn.commit()
#     except Exception as e:
#         conn.rollback()
#         raise e
#     finally:
#         cur.close()
#         conn.close()


# def delete_borrow_record(record_id):
#     conn = get_connection()
#     cur = conn.cursor()
#     try:
#         # Before deleting, restore the book’s available copy
#         cur.execute(
#             "UPDATE books SET available_copies = available_copies + 1 "
#             "WHERE id = (SELECT book_id FROM borrow_records WHERE id = %s)",
#             (record_id,)
#         )

#         # Then delete the record
#         cur.execute("DELETE FROM borrow_records WHERE id = %s", (record_id,))
#         conn.commit()
#     except Exception as e:
#         conn.rollback()
#         raise e
#     finally:
#         cur.close()
#         conn.close()

# /mnt/data/borrow_records.py
from db import get_connection
from datetime import date

def create_borrow_record(member_id, book_id, borrow_date=None, return_date=None, status=None):
    conn = get_connection()
    cur = conn.cursor()
    try:
        # check book availability
        cur.execute("SELECT available_copies FROM books WHERE id = %s", (book_id,))
        row = cur.fetchone()
        if row is None:
            raise ValueError("Book not found.")
        available = row[0]
        if available <= 0:
            raise ValueError("No copies available for this book.")

        if borrow_date is None:
            borrow_date = date.today()

        # auto status if return_date provided
        if return_date is not None:
            final_status = "Returned"
        else:
            final_status = status or "Borrowed"

        cur.execute(
            "INSERT INTO borrow_records (member_id, book_id, borrow_date, return_date, status) "
            "VALUES (%s, %s, %s, %s, %s) RETURNING id",
            (member_id, book_id, borrow_date, return_date, final_status)
        )
        new_id = cur.fetchone()[0]

        # reduce available copies
        cur.execute(
            "UPDATE books SET available_copies = available_copies - 1 WHERE id = %s",
            (book_id,)
        )

        conn.commit()
        return new_id
    except Exception as e:
        conn.rollback()
        raise e
    finally:
        cur.close()
        conn.close()


def get_all_borrow_records():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute(
        "SELECT id, member_id, book_id, borrow_date, return_date, status "
        "FROM borrow_records ORDER BY id"
    )
    rows = cur.fetchall()
    cur.close()
    conn.close()
    return rows

def get_all_borrow_records_with_details():
    """
    Returns: (record_id, member_id, member_name, book_id, book_title, borrow_date, return_date, status)
    """
    conn = get_connection()
    cur = conn.cursor()
    cur.execute(
        "SELECT br.id, m.id, m.name, b.id, b.title, br.borrow_date, br.return_date, br.status "
        "FROM borrow_records br "
        "JOIN members m ON br.member_id = m.id "
        "JOIN books b ON br.book_id = b.id "
        "ORDER BY br.id"
    )
    rows = cur.fetchall()
    cur.close()
    conn.close()
    return rows

def get_borrow_history_for_member(member_id):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute(
        "SELECT id, book_id, borrow_date, return_date, status "
        "FROM borrow_records WHERE member_id = %s ORDER BY borrow_date",
        (member_id,)
    )
    rows = cur.fetchall()
    cur.close()
    conn.close()
    return rows

def get_borrow_count_per_member():
    """
    Returns list of tuples: (member_id, member_name, currently_borrowed_count)
    """
    conn = get_connection()
    cur = conn.cursor()
    cur.execute(
        "SELECT m.id, m.name, COUNT(br.id) AS borrowed_count "
        "FROM members m "
        "LEFT JOIN borrow_records br ON br.member_id = m.id AND br.status = %s "
        "GROUP BY m.id, m.name ORDER BY borrowed_count DESC",
        ("Borrowed",)
    )
    rows = cur.fetchall()
    cur.close()
    conn.close()
    return rows

def mark_as_returned(record_id, return_date=None):
    conn = get_connection()
    cur = conn.cursor()
    try:
        if return_date is None:
            return_date = date.today()
        # Update the record
        cur.execute(
            "UPDATE borrow_records SET return_date = %s, status = %s WHERE id = %s",
            (return_date, "Returned", record_id)
        )

        # Increase available_copies for the book
        cur.execute(
            "UPDATE books SET available_copies = available_copies + 1 "
            "WHERE id = (SELECT book_id FROM borrow_records WHERE id = %s)",
            (record_id,)
        )

        conn.commit()
    except Exception as e:
        conn.rollback()
        raise e
    finally:
        cur.close()
        conn.close()

def update_borrow_record(record_id, member_id=None, book_id=None, borrow_date=None, return_date=None, status=None):
    conn = get_connection()
    cur = conn.cursor()
    try:
        # First fetch old values
        cur.execute("SELECT member_id, book_id FROM borrow_records WHERE id = %s", (record_id,))
        old = cur.fetchone()
        if old is None:
            raise ValueError("Borrow record not found.")
        old_member, old_book = old

        updates = []
        params = []
        if member_id is not None:
            updates.append("member_id = %s")
            params.append(member_id)
        if book_id is not None:
            updates.append("book_id = %s")
            params.append(book_id)
        if borrow_date is not None:
            updates.append("borrow_date = %s")
            params.append(borrow_date)
        if return_date is not None:
            updates.append("return_date = %s")
            params.append(return_date)
            # if return_date is provided, auto-set status if not provided
            if status is None:
                status = "Returned"
        if status is not None:
            updates.append("status = %s")
            params.append(status)

        if updates:
            params.append(record_id)
            sql = f"UPDATE borrow_records SET {', '.join(updates)} WHERE id = %s"
            cur.execute(sql, params)

        # If book has changed, adjust available copies
        if book_id is not None and book_id != old_book:
            # give back one copy to the old book
            cur.execute(
                "UPDATE books SET available_copies = available_copies + 1 WHERE id = %s",
                (old_book,)
            )
            # reduce one copy from the new book, but check availability first
            cur.execute("SELECT available_copies FROM books WHERE id = %s", (book_id,))
            row = cur.fetchone()
            if row is None:
                raise ValueError("New book id not found.")
            if row[0] <= 0:
                raise ValueError("No copies available for the new book.")
            cur.execute(
                "UPDATE books SET available_copies = available_copies - 1 WHERE id = %s",
                (book_id,)
            )

        conn.commit()
    except Exception as e:
        conn.rollback()
        raise e
    finally:
        cur.close()
        conn.close()

def delete_borrow_record(record_id):
    conn = get_connection()
    cur = conn.cursor()
    try:
        # Before deleting, restore the book’s available copy only if the record is not already returned
        cur.execute("SELECT status FROM borrow_records WHERE id = %s", (record_id,))
        row = cur.fetchone()
        if row is None:
            raise ValueError("Record not found.")
        status = row[0]
        if status == "Borrowed":
            cur.execute(
                "UPDATE books SET available_copies = available_copies + 1 "
                "WHERE id = (SELECT book_id FROM borrow_records WHERE id = %s)",
                (record_id,)
            )

        # Then delete the record
        cur.execute("DELETE FROM borrow_records WHERE id = %s", (record_id,))
        conn.commit()
    except Exception as e:
        conn.rollback()
        raise e
    finally:
        cur.close()
        conn.close()
