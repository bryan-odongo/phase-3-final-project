class Transaction:
    all_transactions = []

    def __init__(
        self, transaction_id, account_id, transaction_type, amount, timestamp, details
    ):
        self.transaction_id = transaction_id
        self.account_id = account_id
        self.transaction_type = transaction_type
        self.amount = amount
        self.timestamp = timestamp
        self.details = details
        Transaction.all_transactions.append(self)

    def __str__(self):
        return f"Transaction {self.transaction_id}: {self.transaction_type} of {self.amount} at {self.timestamp}. Details: {self.details}"

    @classmethod
    def get_all_transactions(cls):
        return cls.all_transactions
