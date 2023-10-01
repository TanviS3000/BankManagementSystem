# Bank Management System - ReadMe.md

## Introduction:
The Bank Management System is a GUI application developed using Python's `tkinter` module, interfacing with a MySQL database. The application allows users to perform basic banking operations such as creating an account, depositing money, withdrawing money, and checking account balance.

## Features:
1. **Create Account**: Users can create a new bank account by providing their name and an initial balance.
2. **Deposit**: Users can deposit money into an account by entering the account ID and the deposit amount.
3. **Withdraw**: Users can withdraw money from an account by entering the account ID and the withdrawal amount.
4. **Check Balance**: Users can check the balance of an account by entering the account ID.

## Prerequisites:

### Software:
1. **Python**: Ensure you have Python installed.
2. **MySQL**: Ensure you have a MySQL server running.

### Python Libraries:
Ensure the following Python libraries are installed:
1. `tkinter` - For the GUI interface.
2. `mysql-connector` - To interface with the MySQL database.

You can install them using `pip`:

```bash
pip install mysql-connector-python
```

(Note: `tkinter` is included with most standard Python installations.)

## Setting Up:

### Database:
1. The application expects a MySQL database named `bank_db`.
2. Ensure your MySQL server is running and accessible using the user `root` with no password. If your setup uses different credentials or a password, modify the `create_connection` function accordingly.
3. Create a table named `accounts` with at least the following columns: `id`, `name`, and `balance`.

### Running the Application:
1. Save the provided Python script to a file named `BankManagementSystem.py`.
2. Open your terminal or command prompt.
3. Navigate to the directory where you saved the file.
4. Run the command:

```bash
python BankManagementSystem.py
```

## Usage:
1. **Creating an Account**:
    - Enter your name and the initial deposit amount in the "Create Account" section.
    - Click on "Create Account". You'll be provided an account ID.
2. **Depositing Money**:
    - Enter the account ID and the amount you wish to deposit in the "Deposit" section.
    - Click on "Deposit".
3. **Withdrawing Money**:
    - Enter the account ID and the amount you wish to withdraw in the "Withdraw" section.
    - Click on "Withdraw".
4. **Checking Balance**:
    - Enter the account ID in the "Check Balance" section.
    - Click on "Check Balance". Your balance will be displayed in a pop-up.

## Error Handling:
The application has robust error handling for:
- Database connection issues.
- Missing or incorrect user inputs.
- Failed database operations.

Always ensure the entered account ID is correct and that sufficient balance is available for withdrawals.

## Conclusion:
The Bank Management System offers an intuitive platform for basic banking operations. Its modular design allows easy integration of additional features, such as fund transfer between accounts, account statements, etc.
