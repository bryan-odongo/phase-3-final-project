from models.transaction import Transaction
from models.account import Account
from models.user import User


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

    def transfer(self, to_account_id, amount):
        if self.current_account:
            to_account = Account.get_account_by_id(self.db, to_account_id)
            if to_account:
                if self.current_account.withdraw(self.db, amount):
                    to_account.deposit(self.db, amount)
                    Transaction.create_transaction(
                        self.db,
                        self.current_account.account_id,
                        "Transfer",
                        amount,
                        "2024-06-12 10:00:00",
                        f"Transferred {amount} to account {to_account_id}",
                    )
                    return True
        return False

    def mini_statement(self):
        if self.current_account:
            transactions = Transaction.get_transactions_by_account_id(
                self.db, self.current_account.account_id
            )
            return [str(transaction) for transaction in transactions]
        return "No account selected."
