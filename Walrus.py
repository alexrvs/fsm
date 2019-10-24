import State


class Walrus:
    def __init__(self, state: State):
        self._state = state

    def change_state(self, state: State):
        self._state = state

    def eat(self):
        self._execute('eat')

    def find_food(self):
        self._execute('find_food')

    def move(self):
        self._execute('move')

    def dream(self):
        self._execute('dream')

    def _execute(self, operation):
        try:
            func = getattr(self._state, operation)
            print("Walrus {}.".format(func()))
        except AttributeError:
            print("Walrus doesn't know how to do this.")