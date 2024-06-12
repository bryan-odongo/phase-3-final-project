class TransactionReceipt:
    def __init__(self, receipt_id, transaction_id, printed_at, details):
        self.receipt_id = receipt_id
        self.transaction_id = transaction_id
        self.printed_at = printed_at
        self.details = details

    def print_receipt(self):
        return f"Receipt {self.receipt_id}: Transaction {self.transaction_id} printed at {self.printed_at}\nDetails: {self.details}"
