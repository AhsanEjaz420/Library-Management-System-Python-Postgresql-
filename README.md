# Library-Management-System-Python-Postgresql-
A basic Python–PostgreSQL Library Management System with a Tkinter GUI to manage members, books, and borrow records.
# Library Management System

This is a simple Library Management System built using **Python**, **Tkinter**, and **PostgreSQL**.  
It allows you to manage **members**, **books**, and **borrow/return records** through a basic graphical interface.

## Features
- Add and view library members
- Add and view books
- Borrow and return books
- Automatic update of available book copies
- Simple Tkinter-based GUI

## Technologies Used
- Python 3
- PostgreSQL
- psycopg2
- Tkinter
- python-dotenv

## Project Structure
- `main_gui.py` — Tkinter application
- `db.py` — Database connection setup
- `members.py` — CRUD operations for members
- `books.py` — CRUD operations for books
- `borrow_records.py` — Borrow/return management

## Setup Instructions
1. Install required Python packages:
2. 2. Create a PostgreSQL database:
3. Add your DB credentials to a `.env` file:
4. Create the necessary tables in PostgreSQL (members, books, borrow_records).

5. Run the application:
6. ## License
This project is free to use for learning and development purposes.
