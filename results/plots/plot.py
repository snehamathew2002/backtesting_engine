import matplotlib.pyplot as plt

def plot_equity_curve(result, title):
    plt.plot(result['Date'], result['Portfolio'])
    plt.title(title)
    plt.xlabel("Date")
    plt.ylabel("Portfolio Value")
    plt.xticks(rotation=45)
    plt.show()