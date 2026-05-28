from results.plots.plot import plot_equity_curve, plot_stockPrice_VS_MovingAverage
from utils.performance import calculate_return, max_drawdown, sharpe_ratio


def print_results(result, title):
    print(result[['Date', 'Close', 'Signal', 'Portfolio']].tail())
    print("Total Return:", calculate_return(result))
    print(result['Signal'].value_counts())
    plot_equity_curve(result, title)
    print("Sharpe Ratio:", sharpe_ratio(result['Portfolio']))
    print("Max Drawdown:", max_drawdown(result['Portfolio']))
    plot_stockPrice_VS_MovingAverage(result, title)