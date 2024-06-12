class CLIInterface:
    def __init__(self, atm):
        self.atm = atm

    def print_receipt_menu(self):
        receipt_id = int(input("Enter receipt ID: "))
        self.atm.print_receipt(receipt_id)

    def run(self):
        while True:
            print("-" * 64)
            print("\nWelcome to the ATM Simulator")
            print("-" * 64, end="\n")
            print("1. Login")
            print("2. Exit")
            print("-" * 64)
            choice = input("Enter choice (1 or 2): ")
            print("-" * 64, end="\n")
            if choice == "1":
                card_number = input("Enter your card number: ")
                pin = input("Enter your PIN: ")
                if self.atm.authenticate_user(card_number, pin):
                    print("-" * 64, end="\n")
                    self.user_menu()

                else:
                    print("Authentication failed. Try again.")
            elif choice == "2":
                print("Goodbye!")
                break
            else:
                print("Invalid choice. Try again.")

    def user_menu(self):
        while True:
            print("\n1. Select Account")
            print("2. Check Balance")
            print("3. Deposit")
            print("4. Withdraw")
            print("5. Transfer")
            print("6. Mini Statement")
            print("7. Print Receipt")
            print("8. Logout")
            print("-" * 64, end="\n")
            choice = input("Enter choice: ")

            if choice == "1":
                account_id = int(input("Enter account ID (1 Saving or 2 Checking): "))
                if self.atm.select_account(account_id):
                    print(
                        f"{'Checkings' if choice == 1 else 'Savings'} Account selected."
                    )
                    print("-" * 64, end="\n")
                else:
                    print("Account selection failed.")
            elif choice == "2":
                print("Current balance:", self.atm.check_balance())
                print("-" * 64, end="\n")
            elif choice == "3":
                amount = float(input("Enter amount to deposit: "))
                if self.atm.deposit(amount):
                    print("Deposit successful.")
                    print("-" * 64, end="\n")
                else:
                    print("Deposit failed.")
            elif choice == "4":
                amount = float(input("Enter amount to withdraw: "))
                if self.atm.withdraw(amount):
                    print("Withdrawal successful.")
                    print("-" * 64, end="\n")
                else:
                    print("Withdrawal failed.")
            elif choice == "5":
                from_account_id = int(input("Enter your account ID: "))
                to_account_id = int(input("Enter recipient account ID: "))
                amount = float(input("Enter amount to transfer: "))
                success, message = self.atm.transfer(
                    from_account_id, to_account_id, amount
                )
                print(message)
                print("-" * 64, end="\n")
            elif choice == "6":
                mini_statement = self.atm.mini_statement()
                if mini_statement != "No account selected.":
                    print("Mini statement:")
                    print("-" * 64, end="\n")
                    for transaction in mini_statement:
                        print(transaction)
                    print("-" * 64, end="\n")
                else:
                    print(mini_statement)
            elif choice == "7":
                self.print_receipt_menu()
            elif choice == "8":
                self.atm.current_user = None
                self.atm.current_account = None
                print("Logged out.")
                break
            else:
                print("Invalid choice. Try again.")
