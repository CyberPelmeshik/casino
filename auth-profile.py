class User:
    def __init__(self, username, email):
        self.username = username
        self.email = email
        self.is_verified = False

    def verify_email(self):
        self.is_verified = True

    def __str__(self):
        return f"User(username={self.username}, email={self.email}, verified={self.is_verified})"