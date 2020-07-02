from random import randrange, shuffle


class PasswordUtils:
    @staticmethod
    def generate_password(length: int = 8) -> str:
        string_lower = "abcdefghijklmnopqrstuvwxyz"
        number = "0123456789"
        password = ""
        character = ""
        while len(password) < length:
            entity1 = randrange(0, len(string_lower))
            entity3 = randrange(0, len(number))
            character += string_lower[entity1]
            character += number[entity3]
            password = character
        password_to_list = list(password)
        shuffle(password_to_list)
        return ''.join(password_to_list)
