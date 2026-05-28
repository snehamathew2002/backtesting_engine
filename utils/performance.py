def calculate_return(data):
    return (data['Portfolio'].iloc[-1] / data['Portfolio'].iloc[0]) - 1
