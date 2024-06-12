# ATM Simulator

The ATM Simulator is a software application designed to mimic the basic functionalities of an ATM. This project provides users with a 
realistic experience of using an ATM for various banking transactions. It aims to simulate real-world scenarios, allowing users to practice and 
understand the operations of an ATM without the need for an actual banking interface.

![image](https://github.com/bryan-odongo/phase-3-final-project/assets/152975669/0be48262-cce4-4297-abfb-15fb91a03ed5)


## Functionalities of the Project

### User Authentication
- **Login:** Users can log in using a card number and a secure PIN.
- **PIN Validation:** Ensures that the entered PIN is correct for the given card number.

### Account Management
- **Check Balance:** Users can view their current account balance.
- **Account Details:** Displays basic account information and transaction history.

### Transactions
![image](https://github.com/bryan-odongo/phase-3-final-project/assets/152975669/35b6a756-7f97-418a-b088-d96be2d46ffb)

- **Withdraw Cash:** Users can withdraw a specified amount of cash from their account.
- **Deposit Cash:** Users can deposit cash into their account.
- **Transfer Funds:** Users can transfer funds between different accounts.
- **Mini Statement:** Provides a summary of recent transactions.

### Transaction Receipts
- **Print Receipt:** Option to print a receipt for each transaction.

### User Interface
![image](https://github.com/bryan-odongo/phase-3-final-project/assets/152975669/d897019e-5fcb-4e23-8ca4-942aaab91250)


- **Command Line Interface (CLI):** Simulates a touchscreen interface for user interactions.
- **Multi-Language Support:** Provides support for multiple languages to cater to diverse users.
- **Error Messages:** Displays appropriate error messages and guidance.

## Folder Structure

The project follows a structured folder organization:

```
├── simulator
│   ├── atm_simulator.db
│   ├── cli
│   │   ├── __init__.py
│   │   └── interface.py
│   ├── main.py
│   ├── models
│   │   ├── __init__.py
│   │   ├── account.py
│   │   ├── receipt.py
│   │   ├── transaction.py
│   │   ├── transfer.py
│   │   └── user.py
│   ├── services
│   │   ├── __init__.py
│   │   ├── atm.py
│   │   └── authentication.py
│   └── utils
│       ├── __init__.py
│       ├── database.py
│       └── logger.py
└── tests
```

## Usage

To run the ATM simulator, execute the `main.py` file:

```bash
python main.py
```

Follow the prompts on the command line interface to perform various banking transactions.

## Dependencies

The project relies on the following dependencies:
- Python 3.10.12
- SQLite (for database operations)

Ensure you have these dependencies installed on your system before running the simulator.

## Contributing

Contributions are welcome! If you have any suggestions, bug reports, or feature requests, please open an issue or submit a pull request on the GitHub repository.

## License

This project is licensed under the [MIT License](LICENSE).

