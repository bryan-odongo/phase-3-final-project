class Account:
    def __init__(self, account_id, user_id, account_type, balance, created_at):
        self.account_id = account_id
        self.user_id = user_id
        self.account_type = account_type
        self.balance = balance
        self.created_at = created_at

    def check_balance(self):
        return self.balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            return True
        return False

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            return True
        return False
