class PasswordManager:
    def __init__(self):
        self.user = None
        self.__password = None

    def set_password(self, password):
        if self.__password:
            raise ValueError('Password is already set.')

        self.__password = password

    def check_password(self, password):
        if password != self.__password:
            raise ValueError('Password incorrect!')

        return True

    def change_password(self, old_password, new_password):
        if not old_password or not new_password:
            raise ValueError('Not all required values provided!')

        if old_password != self.__password:
            raise ValueError('Incorrect password!')

        self.set_password(new_password)




