# 📊 Systematic Trading Backtesting Engine (Python)

A modular Python-based backtesting engine for evaluating quantitative trading strategies using historical market data.  
The project implements and compares **Momentum** and **Mean Reversion** strategies with performance evaluation metrics.

---

# 🚀 Features

- Momentum trading strategy (trend-following)
- Mean Reversion strategy (contrarian approach)
- Portfolio simulation engine (cash + position tracking)
- Signal-based trade execution system
- Performance evaluation metrics
- Equity curve visualization support

---

# 🧠 Quant Concepts Implemented

- Moving Averages
- Trading Signals (Buy / Sell / Hold)
- Backtesting Simulation
- Market Regimes (trend vs mean reversion behavior)
- Risk-adjusted returns
- Portfolio tracking over time

---

# 📈 Strategies

## 1. Momentum Strategy
- Buys when price is above moving average
- Assumes trend continuation
- Performs well in trending markets

## 2. Mean Reversion Strategy
- Buys when price is below moving average
- Assumes price returns to mean
- Performs better in sideways markets

---

# 📊 Performance Metrics

## Total Return
Measures overall profit:

Final Portfolio / Initial Portfolio - 1

---

## Sharpe Ratio
Risk-adjusted return metric:

Return per unit of volatility.

---

## Maximum Drawdown
Measures worst loss from peak:

Indicates downside risk of the strategy.

---

# 📌 Sample Results

## Momentum Strategy

- Total Return: **5.35%**
- Sharpe Ratio: **0.47**
- Max Drawdown: **-0.79%**

**Observation:**
Momentum strategy performed well in a strong upward trending market.

---

## Mean Reversion Strategy

- Total Return: **0%**
- Sharpe Ratio: **0**
- Max Drawdown: **0%**

**Observation:**
Mean reversion underperformed due to strong trending market conditions where price rarely reverted below the moving average.

---

# 🧠 Key Insight

Strategy performance depends heavily on **market regime**:

| Market Condition | Momentum | Mean Reversion |
|------------------|----------|----------------|
| Trending Market  | Strong | Weak        |
| Sideways Market  | Mixed  | Strong      |

---

# ⚙️ How to Run

```bash
pip install pandas numpy matplotlib
python main.py
