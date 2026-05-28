from engine import backtester
from engine.backtester import Backtester
from results.plots.plot import plot_equity_curve
from results.reports.result import print_results
from strategies.mean_reversion_strategy import MeanReversionStrategy
from strategies.momentum_strategy import MomentumStrategy
from utils.data_loader import load_data
from utils.performance import calculate_return

data = load_data("data/raw/sample_data.csv")

momentum_strategy = MomentumStrategy(window=10)
momentum_data = momentum_strategy.generate_signals(data.copy())

backtester1 = Backtester()
result1 = backtester1.run(momentum_data)
print_results(result1, "Equity Curve - Momentum Strategy")

mean_reversion_strategy = MeanReversionStrategy(window=10)
mean_reversion_data = mean_reversion_strategy.generate_signals(data.copy())

backtester2 = Backtester()
result2 = backtester2.run(mean_reversion_data)
print_results(result2, "Equity Curve - Mean Reversion Strategy")