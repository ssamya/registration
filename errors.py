class Errors(Exception):
    pass


class EmptyLoginError(Errors):
    def __str__(self):
        return "Login cannot be empty. Try again"


class EmptyPasswordError(Errors):
    def __str__(self):
        return "Password cannot be empty"


class EmptyEmailError(Errors):
    def __str__(self):
        return "Email cannot be empty"


class InvalidEmailError(Errors):
    def __str__(self):
        return "Incorrect email"

