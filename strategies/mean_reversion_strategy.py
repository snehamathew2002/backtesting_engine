class MeanReversionStrategy:
    def __init__(self, window=10):
        self.window = window

    def generate_signals(self, data):
        signals = []

        for i in range(len(data)):
            if i < self.window:
                signals.append(0)
                continue

            avg_price = data['Close'].iloc[i-self.window:i].mean()
            price = data['Close'].iloc[i]

            threshold = 0.02  # 2% threshold for mean reversion
            if price <  avg_price * (1 - threshold):
                signals.append(1)   # BUY
            elif price > avg_price * (1 + threshold):
                signals.append(-1)  # SELL
            else:
                signals.append(0)   # HOLD

        data['Signal'] = signals
        return data