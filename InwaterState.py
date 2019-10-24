import State


class InWaterState(State):
    def eat(self):
        return "can't eat in the water"

    def find_food(self):
        return "plows the seabed with tusks, catching shellfish"

    def move(self):
        return "gracefully breaks the waves of the world's oceans"

    def dream(self):
        return "doesn't sleep or dream in water - it's too difficult"

