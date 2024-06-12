from cli.interface import CLIInterface
from models.user import User
from models.account import Account
from services.atm import ATM


def main():
    # Create sample data
    user1 = User(1, "1234567890123456", "1234", "Alice", "EN")
    user2 = User(2, "2345678901234567", "5678", "Bob", "EN")

    account1 = Account(1, 1, "Checking", 1000.00, "2023-01-01 10:00:00")
    account2 = Account(2, 2, "Savings", 5000.00, "2023-01-01 10:00:00")

    users = [user1, user2]
    accounts = [account1, account2]

    # Initialize ATM
    atm = ATM(users, accounts)

    # Initialize CLI Interface
    cli = CLIInterface(atm)
    cli.run()


if __name__ == "__main__":
    main()
