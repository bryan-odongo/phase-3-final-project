from services.atm import ATM
from cli.interface import CLIInterface
from utils.database import Database


def main():
    # Initialize Database
    db = Database("atm_simulator.db")

    # Initialize ATM
    atm = ATM(db)

    # Initialize CLI Interface
    cli = CLIInterface(atm)
    cli.run()

    # Close Database Connection
    db.close()


if __name__ == "__main__":
    main()
