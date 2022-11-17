import re
from entities.user import User


class UserInputError(Exception):
    pass


class AuthenticationError(Exception):
    pass


class UserService:
    def __init__(self, user_repository):
        self._user_repository = user_repository

    def check_credentials(self, username, password):
        if not username or not password:
            raise UserInputError("Username and password are required")

        user = self._user_repository.find_by_username(username)

        if not user or user.password != password:
            raise AuthenticationError("Invalid username or password")

        return user

    def create_user(self, username, password):
        self.validate(username, password)

        user = self._user_repository.create(
            User(username, password)
        )

        return user

    def validate(self, username, password):
        if not username or not password:
            raise UserInputError("Username and password are required")

        if self._user_repository.find_by_username(username):
            raise UserInputError(f"Username is not available.")
        
        if not re.match("^[a-z]+$", username):
            raise UserInputError("Username must consist only symbols from [a-z].")

        if len(username) < 3:
            raise UserInputError("Username must have min lenght of 3.")

        if re.match("^[a-z]+$", password):
            raise UserInputError("Password must not consist only of symbols from [a-z].")
        
        if len(password) < 8:
            raise UserInputError("Password must have min lenght of 8.")
        

