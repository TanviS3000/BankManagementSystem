import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import mysql.connector
from mysql.connector import Error


def create_connection():
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password=" ",
            database="bank_db"
        )
        if connection.is_connected():
            return connection
    except Error as e:
        print(f"Error: {e}")
        return None


def execute_query(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
        return cursor.lastrowid  # Returns the ID of the last modified row
    except Error as e:
        print(f"The error '{e}' occurred")
        return None


def execute_read_query(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        result = cursor.fetchall()
        return result
    except Error as e:
        print(f"The error '{e}' occurred")
        return None


connection = create_connection()

# Initialize Tkinter window
window = tk.Tk()
window.title("Bank Management System")


def create_account():
    name = name_entry.get()
    balance = balance_entry.get()
    if not name or not balance:
        messagebox.showerror("Input Error", "All fields are required!")
        return

    query = f"INSERT INTO accounts (name, balance) VALUES ('{name}', {balance})"
    account_id = execute_query(connection, query)
    messagebox.showinfo("Success", f"Account created successfully! Your account ID is {account_id}")


def deposit():
    account_id = acc_id_entry_deposit.get()
    amount = amount_entry_deposit.get()
    if not account_id or not amount:
        messagebox.showerror("Input Error", "All fields are required!")
        return

    query = f"UPDATE accounts SET balance = balance + {amount} WHERE id = {account_id}"
    execute_query(connection, query)
    messagebox.showinfo("Success", "Amount deposited successfully!")


def withdraw():
    account_id = acc_id_entry_withdraw.get()
    amount = amount_entry_withdraw.get()
    if not account_id or not amount:
        messagebox.showerror("Input Error", "All fields are required!")
        return

    query = f"UPDATE accounts SET balance = balance - {amount} WHERE id = {account_id}"
    execute_query(connection, query)
    messagebox.showinfo("Success", "Amount withdrawn successfully!")


def check_balance():
    account_id = acc_id_entry_balance.get()
    if not account_id:
        messagebox.showerror("Input Error", "Account ID is required!")
        return

    query = f"SELECT balance FROM accounts WHERE id = {account_id}"
    balance = execute_read_query(connection, query)
    if balance:
        messagebox.showinfo("Balance", f"Your balance is: {balance[0][0]}")
    else:
        messagebox.showerror("Error", "Account not found")


# Create Account Tab
frame_create = ttk.Frame(window)
frame_create.grid(row=0, column=0, padx=10, pady=5, sticky="ew")

ttk.Label(frame_create, text="Name").grid(row=0, column=0)
name_entry = ttk.Entry(frame_create)
name_entry.grid(row=0, column=1)

ttk.Label(frame_create, text="Initial Balance").grid(row=1, column=0)
balance_entry = ttk.Entry(frame_create)
balance_entry.grid(row=1, column=1)

ttk.Button(frame_create, text="Create Account", command=create_account).grid(row=2, columnspan=2)

# Deposit Tab
frame_deposit = ttk.Frame(window)
frame_deposit.grid(row=1, column=0, padx=10, pady=5, sticky="ew")

ttk.Label(frame_deposit, text="Account ID").grid(row=0, column=0)
acc_id_entry_deposit = ttk.Entry(frame_deposit)
acc_id_entry_deposit.grid(row=0, column=1)

ttk.Label(frame_deposit, text="Amount").grid(row=1, column=0)
amount_entry_deposit = ttk.Entry(frame_deposit)
amount_entry_deposit.grid(row=1, column=1)

ttk.Button(frame_deposit, text="Deposit", command=deposit).grid(row=2, columnspan=2)

# Withdraw Tab
frame_withdraw = ttk.Frame(window)
frame_withdraw.grid(row=2, column=0, padx=10, pady=5, sticky="ew")

ttk.Label(frame_withdraw, text="Account ID").grid(row=0, column=0)
acc_id_entry_withdraw = ttk.Entry(frame_withdraw)
acc_id_entry_withdraw.grid(row=0, column=1)

ttk.Label(frame_withdraw, text="Amount").grid(row=1, column=0)
amount_entry_withdraw = ttk.Entry(frame_withdraw)
amount_entry_withdraw.grid(row=1, column=1)

ttk.Button(frame_withdraw, text="Withdraw", command=withdraw).grid(row=2, columnspan=2)

# Check Balance Tab
frame_balance = ttk.Frame(window)
frame_balance.grid(row=3, column=0, padx=10, pady=5, sticky="ew")

ttk.Label(frame_balance, text="Account ID").grid(row=0, column=0)
acc_id_entry_balance = ttk.Entry(frame_balance)
acc_id_entry_balance.grid(row=0, column=1)

ttk.Button(frame_balance, text="Check Balance", command=check_balance).grid(row=1, columnspan=2)

window.mainloop()
