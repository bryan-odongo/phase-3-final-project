import datetime
from models.transaction import Transaction
from models.account import Account
from models.user import User
from models.transfer import Transfer
from models.receipt import TransactionReceipt


class ATM:
    def __init__(self, db):
        self.db = db
        self.current_user = None
        self.current_account = None

    def authenticate_user(self, card_number, pin):
        user = User.get_user_by_card_number(self.db, card_number)
        if user and user.validate_pin(pin):
            self.current_user = user
            return True
        return False

    def select_account(self, account_id):
        account = Account.get_account_by_id(self.db, account_id)
        if account and account.user_id == self.current_user.user_id:
            self.current_account = account
            return True
        return False

    def check_balance(self):
        if self.current_account:
            return self.current_account.check_balance()
        return "No account selected."

    def deposit(self, amount):
        if self.current_account:
            if self.current_account.deposit(self.db, amount):
                Transaction.create_transaction(
                    self.db,
                    self.current_account.account_id,
                    "Deposit",
                    amount,
                    "2024-06-12 10:00:00",
                    f"Deposited {amount}",
                )
                return True
        return "No account selected."

    def withdraw(self, amount):
        if self.current_account:
            if self.current_account.withdraw(self.db, amount):
                Transaction.create_transaction(
                    self.db,
                    self.current_account.account_id,
                    "Withdraw",
                    amount,
                    "2024-06-12 10:00:00",
                    f"Withdrew {amount}",
                )
                return True
        return "No account selected."

    def transfer(self, from_account_id, to_account_id, amount):
        # Check if accounts exist
        from_account = self.db.fetch_one(
            "SELECT * FROM accounts WHERE account_id = ?", (from_account_id,)
        )
        to_account = self.db.fetch_one(
            "SELECT * FROM accounts WHERE account_id = ?", (to_account_id,)
        )

        if not from_account or not to_account:
            return False, "One or both accounts do not exist."

        # Check if the from account has enough balance
        from_account_balance = from_account[3]  # Balance is at index 3
        if from_account_balance < amount:
            return False, "Insufficient funds in the source account."

        # Perform the transfer
        new_from_balance = from_account_balance - amount
        new_to_balance = to_account[3] + amount  # Balance is at index 3

        # Update balances
        self.db.execute_query(
            "UPDATE accounts SET balance = ? WHERE account_id = ?",
            (new_from_balance, from_account_id),
        )
        self.db.execute_query(
            "UPDATE accounts SET balance = ? WHERE account_id = ?",
            (new_to_balance, to_account_id),
        )

        # Record the transfer
        timestamp = datetime.datetime.now().isoformat()
        details = f"Transfer from account {from_account_id} to account {to_account_id}"
        Transfer.create_transfer(
            self.db, from_account_id, to_account_id, amount, timestamp, details
        )

        # Record transactions
        Transaction.create_transaction(
            self.db, from_account_id, "Transfer Out", amount, timestamp, details
        )
        Transaction.create_transaction(
            self.db, to_account_id, "Transfer In", amount, timestamp, details
        )

        return True, "Transfer successful."

    def mini_statement(self):
        if self.current_account:
            transactions = Transaction.get_transactions_by_account_id(
                self.db, self.current_account.account_id
            )
            return [str(transaction) for transaction in transactions]
        return "No account selected."

    def print_receipt(self, receipt_id):
        TransactionReceipt.print_receipt(self.db, receipt_id)
