"""Модуль игры Рулетка."""

import random

class RouletteGame:
    """Реализует упрощенную механику рулетки."""

    def spin(self) -> int:
        """Запускает вращение рулетки.

        Returns:
            Выпавшее число от 0 до 36.
        """
        return random.randint(0, 36)

    def place_bet(self, bet_number: int) -> str:
        """Размещает ставку на число и возвращает результат игры.

        Args:
            bet_number: Число, выбранное игроком.

        Returns:
            Строка с сообщением о выигрыше или проигрыше.
        """
        result = self.spin()
        if bet_number == result:
            return f"Win! Number выпадения: {result}"
        return f"Lose. Number выпадения: {result}"