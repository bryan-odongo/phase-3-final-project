class Transfer:
    def __init__(
        self, transfer_id, from_account_id, to_account_id, amount, timestamp, details
    ):
        self.transfer_id = transfer_id
        self.from_account_id = from_account_id
        self.to_account_id = to_account_id
        self.amount = amount
        self.timestamp = timestamp
        self.details = details

    def __str__(self):
        return f"Transfer {self.transfer_id}: {self.amount} from {self.from_account_id} to {self.to_account_id} at {self.timestamp}"
