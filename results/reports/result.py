from results.plots.plot import plot_equity_curve
from utils.performance import calculate_return


def print_results(result, title):
    print(result[['Date', 'Close', 'Signal', 'Portfolio']].tail())
    print("Total Return:", calculate_return(result))
    print(result['Signal'].value_counts())
    plot_equity_curve(result, title)