from utils.database import Database


class User:
    def __init__(self, user_id, card_number, pin, name, language):
        self.user_id = user_id
        self.card_number = card_number
        self.pin = pin
        self.name = name
        self.language = language

    @staticmethod
    def get_user_by_card_number(db, card_number):
        query = "SELECT * FROM users WHERE card_number = ?"
        result = db.fetch_one(query, (card_number,))
        if result:
            return User(*result)
        return None

    def validate_pin(self, input_pin):
        return self.pin == input_pin
