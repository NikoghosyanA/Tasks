# 1

class LampRow:
    def __init__(self):
        self.__state = "0" * 8

    @property
    def state(self):
        return self.__state

    @state.setter
    def state(self, value):
        if len(value) == 8:
            self.__state = value
        else:
            self.__state = "0" * 8

    def show(self):
        print("".join("-" if char == "0" else "*" for char in self.__state))

# 2


class LampRow:
    def __init__(self, num_lamps):
        self.num_lamps = num_lamps
        self.__state = "0" * num_lamps

    @property
    def state(self):
        return self.__state

    @state.setter
    def state(self, value):
        if len(value) == self.num_lamps:
            self.__state = value
        else:
            self.__state = "0" * self.num_lamps
            print("error: invalid state string length")

    def show(self):
        print("".join("-" if char == "0" else "*" for char in self.__state))
