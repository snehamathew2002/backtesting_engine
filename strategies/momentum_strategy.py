class MomentumStrategy:
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

            if price > avg_price:
                signals.append(1)   # BUY
            else:
                signals.append(-1)  # SELL

        data['Signal'] = signals
        return data