import pandas as pd

def transform_data(file_path):
    
    df = pd.read_csv(file_path)

    # epoch time real time conversion
    df['open_time'] = pd.to_datetime(df['open_time'], unit='ms')

    df['close_time'] = pd.to_datetime(df['close_time'], unit='ms')

    # Overwrite the original CSV file
    df.to_csv(file_path, index=False)

file_path = 'BTCUSD_1h.csv'
transform_data(file_path)