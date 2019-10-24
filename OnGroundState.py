import State


class OnGroundState(State):
    def eat(self):
        return "pours out the extracted shellfish on its belly and starts slowly eating it"

    def find_food(self):
        return "finds not fresh, but quite editable whale carcass that has been thrown to the shore"

    def move(self):
        return "awkwardly crawls along the shoreline"

    def dream(self):
        return "stops for a moment dreaming of one familiar female"
