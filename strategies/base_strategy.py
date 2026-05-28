"""Base strategy class for all strategies to inherit from."""

class BaseStrategy:
    """Abstract base class for trading strategies."""

    def __init__(self, name):
        self.name = name

    def calculate_signals(self, data):
        """Generate trading signals.

        Args:
            data: DataFrame with OHLCV data

        Returns:
            DataFrame with signal column (1=buy, -1=sell, 0=hold)
        """
        raise NotImplementedError("Subclasses must implement calculate_signals()")
