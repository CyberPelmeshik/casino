import random

class RouletteGame:
    def spin(self):
        return random.randint(0, 36)

    def place_bet(self, bet_number):
        result = self.spin()
        if bet_number == result:
            return f"Win! Number выпадения: {result}"
        return f"Lose. Number выпадения: {result}"