from models.transaction import Transaction


class ATM:
    def __init__(self, users, accounts):
        self.users = users
        self.accounts = accounts
        self.current_user = None
        self.current_account = None

    def authenticate_user(self, card_number, pin):
        for user in self.users:
            if user.card_number == card_number and user.validate_pin(pin):
                self.current_user = user
                return True
        return False

    def select_account(self, account_id):
        for account in self.accounts:
            if (
                account.account_id == account_id
                and account.user_id == self.current_user.user_id
            ):
                self.current_account = account
                return True
        return False

    def check_balance(self):
        if self.current_account:
            return self.current_account.check_balance()
        return "No account selected."

    def deposit(self, amount):
        if self.current_account:
            if self.current_account.deposit(amount):
                Transaction(
                    transaction_id=len(Transaction.all_transactions) + 1,
                    account_id=self.current_account.account_id,
                    transaction_type="Deposit",
                    amount=amount,
                    timestamp="2024-06-12 10:00:00",
                    details=f"Deposited {amount}",
                )
                return True
        return "No account selected."

    def withdraw(self, amount):
        if self.current_account:
            if self.current_account.withdraw(amount):
                Transaction(
                    transaction_id=len(Transaction.all_transactions) + 1,
                    account_id=self.current_account.account_id,
                    transaction_type="Withdraw",
                    amount=amount,
                    timestamp="2024-06-12 10:00:00",
                    details=f"Withdrew {amount}",
                )
                return True
        return "No account selected."

    def transfer(self, to_account_id, amount):
        if self.current_account:
            for account in self.accounts:
                if account.account_id == to_account_id:
                    if self.current_account.withdraw(amount):
                        account.deposit(amount)
                        Transaction(
                            transaction_id=len(Transaction.all_transactions) + 1,
                            account_id=self.current_account.account_id,
                            transaction_type="Transfer",
                            amount=amount,
                            timestamp="2024-06-12 10:00:00",
                            details=f"Transferred {amount} to account {to_account_id}",
                        )
                        return True
        return False

    def mini_statement(self):
        if self.current_account:
            # Retrieve last 5 transactions for simplicity
            transactions = [
                t
                for t in Transaction.all_transactions
                if t.account_id == self.current_account.account_id
            ][-5:]
            return transactions
        return "No account selected."
