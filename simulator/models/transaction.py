from utils.database import Database


class Transaction:
    def __init__(
        self, transaction_id, account_id, transaction_type, amount, timestamp, details
    ):
        self.transaction_id = transaction_id
        self.account_id = account_id
        self.transaction_type = transaction_type
        self.amount = amount
        self.timestamp = timestamp
        self.details = details

    @staticmethod
    def create_transaction(
        db, account_id, transaction_type, amount, timestamp, details
    ):
        query = """
        INSERT INTO transactions (account_id, transaction_type, amount, timestamp, details)
        VALUES (?, ?, ?, ?, ?)
        """
        db.execute_query(
            query, (account_id, transaction_type, amount, timestamp, details)
        )

    @staticmethod
    def get_transactions_by_account_id(db, account_id, limit=5):
        query = "SELECT * FROM transactions WHERE account_id = ? ORDER BY transaction_id DESC LIMIT ?"
        results = db.fetch_all(query, (account_id, limit))
        return [Transaction(*result) for result in results]

    def __str__(self):
        return f"Transaction {self.transaction_id}: {self.transaction_type} of {self.amount} at {self.timestamp}. Details: {self.details}"
