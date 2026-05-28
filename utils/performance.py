import pandas as pd
import numpy as np

def calculate_return(data):
    return (data['Portfolio'].iloc[-1] / data['Portfolio'].iloc[0]) - 1

def sharpe_ratio(portfolio_values):
    returns = pd.Series(portfolio_values).pct_change().dropna()

    if returns.std() == 0:
        return 0

    return returns.mean() / returns.std()

def max_drawdown(portfolio_values):
    portfolio = pd.Series(portfolio_values)

    peak = portfolio.cummax()
    drawdown = (portfolio - peak) / peak

    return drawdown.min()