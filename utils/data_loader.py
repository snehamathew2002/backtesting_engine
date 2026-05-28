import pandas as pd

def load_data(path):
    df = pd.read_csv(path)
    df['Date'] = pd.to_datetime(df['Date'])
    df = df.sort_values('Date')
    df.reset_index(drop=True, inplace=True)
    df['Close'] = df['Close'].replace(r'[\$,]', '', regex=True).astype(float)
    return df