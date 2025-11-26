# from db import get_connection

# def create_member(name, phone, email):
#     conn = get_connection()
#     cur = conn.cursor()
#     try:
#         cur.execute(
#             "INSERT INTO members (name, phone, email) VALUES (%s, %s, %s) RETURNING id",
#             (name, phone, email)
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

# def get_all_members():
#     conn = get_connection()
#     cur = conn.cursor()
#     cur.execute("SELECT id, name, phone, email FROM members ORDER BY id")
#     rows = cur.fetchall()
#     cur.close()
#     conn.close()
#     return rows

# def get_member_by_id(member_id):
#     conn = get_connection()
#     cur = conn.cursor()
#     cur.execute("SELECT id, name, phone, email FROM members WHERE id = %s", (member_id,))
#     row = cur.fetchone()
#     cur.close()
#     conn.close()
#     return row

# def update_member(member_id, name=None, phone=None, email=None):
#     conn = get_connection()
#     cur = conn.cursor()
#     try:
#         updates = []
#         params = []
#         if name is not None:
#             updates.append("name = %s")
#             params.append(name)
#         if phone is not None:
#             updates.append("phone = %s")
#             params.append(phone)
#         if email is not None:
#             updates.append("email = %s")
#             params.append(email)
#         params.append(member_id)

#         sql = f"UPDATE members SET {', '.join(updates)} WHERE id = %s"
#         cur.execute(sql, params)
#         conn.commit()
#     except Exception as e:
#         conn.rollback()
#         raise e
#     finally:
#         cur.close()
#         conn.close()

# def delete_member(member_id):
#     conn = get_connection()
#     cur = conn.cursor()
#     try:
#         cur.execute("DELETE FROM members WHERE id = %s", (member_id,))
#         conn.commit()
#     except Exception as e:
#         conn.rollback()
#         raise e
#     finally:
#         cur.close()
#         conn.close()

# /mnt/data/members.py
from db import get_connection

def create_member(name, phone, email):
    conn = get_connection()
    cur = conn.cursor()
    try:
        # Prevent duplicate email
        if email:
            cur.execute("SELECT id FROM members WHERE email = %s", (email,))
            if cur.fetchone() is not None:
                raise ValueError(f"Email '{email}' is already registered.")

        cur.execute(
            "INSERT INTO members (name, phone, email) VALUES (%s, %s, %s) RETURNING id",
            (name, phone, email)
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

def get_all_members():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT id, name, phone, email FROM members ORDER BY id")
    rows = cur.fetchall()
    cur.close()
    conn.close()
    return rows

def get_member_by_id(member_id):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT id, name, phone, email FROM members WHERE id = %s", (member_id,))
    row = cur.fetchone()
    cur.close()
    conn.close()
    return row

def update_member(member_id, name=None, phone=None, email=None):
    conn = get_connection()
    cur = conn.cursor()
    try:
        updates = []
        params = []
        if name is not None:
            updates.append("name = %s")
            params.append(name)
        if phone is not None:
            updates.append("phone = %s")
            params.append(phone)
        if email is not None:
            # check duplicate email (exclude current member)
            cur.execute("SELECT id FROM members WHERE email = %s AND id <> %s", (email, member_id))
            if cur.fetchone():
                raise ValueError(f"Email '{email}' is already used by another member.")
            updates.append("email = %s")
            params.append(email)
        if not updates:
            return  # nothing to do
        params.append(member_id)

        sql = f"UPDATE members SET {', '.join(updates)} WHERE id = %s"
        cur.execute(sql, params)
        conn.commit()
    except Exception as e:
        conn.rollback()
        raise e
    finally:
        cur.close()
        conn.close()

def delete_member(member_id):
    conn = get_connection()
    cur = conn.cursor()
    try:
        cur.execute("DELETE FROM members WHERE id = %s", (member_id,))
        conn.commit()
    except Exception as e:
        conn.rollback()
        raise e
    finally:
        cur.close()
        conn.close()
