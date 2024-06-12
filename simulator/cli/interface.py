class CLIInterface:
    def __init__(self, atm):
        self.atm = atm

    def run(self):
        while True:
            print("\nWelcome to the ATM Simulator")
            print("1. Login")
            print("2. Exit")
            choice = input("Enter choice: ")

            if choice == "1":
                card_number = input("Enter your card number: ")
                pin = input("Enter your PIN: ")
                if self.atm.authenticate_user(card_number, pin):
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
            print("7. Logout")
            choice = input("Enter choice: ")

            if choice == "1":
                account_id = int(input("Enter account ID: "))
                if self.atm.select_account(account_id):
                    print("Account selected.")
                else:
                    print("Account selection failed.")
            elif choice == "2":
                print("Current balance:", self.atm.check_balance())
            elif choice == "3":
                amount = float(input("Enter amount to deposit: "))
                if self.atm.deposit(amount):
                    print("Deposit successful.")
                else:
                    print("Deposit failed.")
            elif choice == "4":
                amount = float(input("Enter amount to withdraw: "))
                if self.atm.withdraw(amount):
                    print("Withdrawal successful.")
                else:
                    print("Withdrawal failed.")
            elif choice == "5":
                to_account_id = int(input("Enter target account ID: "))
                amount = float(input("Enter amount to transfer: "))
                if self.atm.transfer(to_account_id, amount):
                    print("Transfer successful.")
                else:
                    print("Transfer failed.")
            elif choice == "6":
                print("Mini statement:", self.atm.mini_statement())
            elif choice == "7":
                self.atm.current_user = None
                self.atm.current_account = None
                print("Logged out.")
                break
            else:
                print("Invalid choice. Try again.")
