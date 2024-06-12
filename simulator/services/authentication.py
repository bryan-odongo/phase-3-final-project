class AuthenticationService:
    def __init__(self, users):
        self.users = users

    def authenticate(self, card_number, pin):
        for user in self.users:
            if user.card_number == card_number and user.validate_pin(pin):
                return user
        return None
