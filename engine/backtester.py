class Backtester:
    def __init__(self, initial_cash=10000):
        self.cash = initial_cash
        self.position = 0
        self.portfolio_value = []

    def run(self, data):
        for i in range(len(data)):
            price = data['Close'][i]
            signal = data['Signal'][i]

            # BUY signal
            if signal == 1 and self.cash > 0:
                self.position = self.cash / price
                self.cash = 0

            # SELL signal
            elif signal == -1 and self.position > 0:
                self.cash = self.position * price
                self.position = 0

            total_value = self.cash + self.position * price
            self.portfolio_value.append(total_value)

        data['Portfolio'] = self.portfolio_value
        return data