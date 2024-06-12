from utils.database import Database


class Account:
    def __init__(self, account_id, user_id, account_type, balance, created_at):
        self.account_id = account_id
        self.user_id = user_id
        self.account_type = account_type
        self.balance = balance
        self.created_at = created_at

    @staticmethod
    def get_accounts_by_user_id(db, user_id):
        query = "SELECT * FROM accounts WHERE user_id = ?"
        results = db.fetch_all(query, (user_id,))
        return [Account(*result) for result in results]

    @staticmethod
    def get_account_by_id(db, account_id):
        query = "SELECT * FROM accounts WHERE account_id = ?"
        result = db.fetch_one(query, (account_id,))
        if result:
            return Account(*result)
        return None

    def check_balance(self):
        return self.balance

    def deposit(self, db, amount):
        if amount > 0:
            self.balance += amount
            query = "UPDATE accounts SET balance = ? WHERE account_id = ?"
            db.execute_query(query, (self.balance, self.account_id))
            return True
        return False

    def withdraw(self, db, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            query = "UPDATE accounts SET balance = ? WHERE account_id = ?"
            db.execute_query(query, (self.balance, self.account_id))
            return True
        return False
