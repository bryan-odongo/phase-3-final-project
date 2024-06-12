class TransactionReceipt:
    def __init__(self, receipt_id, transaction_id, printed_at, details):
        self.receipt_id = receipt_id
        self.transaction_id = transaction_id
        self.printed_at = printed_at
        self.details = details

    @staticmethod
    def create_receipt(db, transaction_id, details):
        query = """
        INSERT INTO TransactionReceipts (transaction_id, details)
        VALUES (?, ?)
        """
        db.execute_query(query, (transaction_id, details))

    @staticmethod
    def print_receipt(db, receipt_id):
        receipt = db.fetch_one(
            "SELECT * FROM TransactionReceipts WHERE receipt_id = ?", (receipt_id,)
        )
        if receipt:
            print(f"Receipt ID: {receipt['receipt_id']}")
            print(f"Transaction ID: {receipt['transaction_id']}")
            print(f"Printed At: {receipt['printed_at']}")
            print(f"Details: {receipt['details']}")
        else:
            print("Receipt not found.")
