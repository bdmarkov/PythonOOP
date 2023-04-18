

class Profile:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    @property
    def username(self):
        return self.__username

    @username.setter
    def username(self, value):
        if len(value) < 5 or len(value) >  15:
            raise ValueError("The username must be between 5 and 15 characters.")
        self.__username = value

    @property
    def password(self):
        return self.__password

    @password.setter
    def password(self, value):
        if self.len_pass(value) and self.upper(value) and self.digit(value):
            self.__password = value
            return
        raise ValueError("The password must be 8 or more characters with at least 1 digit and 1 uppercase letter.")


    def len_pass(self, password):
        return len(password) >= 8

    def upper(self, password):
        uppers = [el for el in password if el.isupper()]
        return True if uppers else False

    def digit(self, password):
        digits = [el for el in password if el.isdigit()]
        return True if digits else False

    def __str__(self):
        return f'You have a profile with username: "{self.username}" and password: {"*" * len(self.password)}'

correct_profile = Profile("Username", "Passw0rd")
print(correct_profile)


