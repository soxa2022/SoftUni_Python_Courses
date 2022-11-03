class Account:

    def __init__(self, id_number: int, balance: int,pin: int):
        self.__id = id_number
        self.__pin = pin
        self.balance = balance

    def get_id(self, pin):
        if not pin == self.__pin:
            return "Wrong pin"
        return self.__id

    def change_pin(self, old_pin, new_pin):
        if not old_pin == self.__pin:
            return "Wrong pin"
        self.__pin = new_pin
        return "Pin changed"