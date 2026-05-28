import matplotlib.pyplot as plt

def plot_equity_curve(result, strategy_name):
    plt.plot(result['Date'], result['Portfolio'])
    plt.title(f"Equity Curve - {strategy_name}")
    plt.xlabel("Date")
    plt.ylabel("Portfolio Value")
    plt.xticks(rotation=45)
    plt.show()

def plot_stockPrice_VS_MovingAverage(result, strategy_name):
    plt.figure(figsize=(12,6))

    plt.plot(result['Date'], result['Close'], label='Close Price')
    plt.plot(result['Date'], result['MovingAverage'], label='Moving Average')

    plt.title(f"Stock Price vs Moving Average - {strategy_name}")
    plt.xlabel("Date")
    plt.ylabel("Price")

    plt.legend()
    plt.xticks(rotation=45)
    plt.grid()

    plt.show()