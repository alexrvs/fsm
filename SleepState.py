import State


class SleepState(State):
    def eat(self):
        return "can't it while sleeping"

    def find_food(self):
        return "looking for food, but only in its dreams"

    def move(self):
        return "can't move while sleeping"

    def dream(self):
        return "sleeps and sees a wonderful dream"

