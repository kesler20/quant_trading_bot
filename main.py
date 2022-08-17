import pandas as pd
from yahoo_fin.stock_info import * 
import matplotlib.pyplot as plt 
import time
from orders import OrderEngine

data: list = []
WAIT_TIME = 2 #seconds
order_engine = OrderEngine()

def calculate_sma(df: pd.DataFrame, i: int):
    df[f'SMA{i}'] = df[0].rolling(i).mean()
    return df

buy = False

if __name__ == '__main__':
    while True:
        data.append(get_live_price('TSLA'))
        time.sleep(WAIT_TIME)
        df = pd.DataFrame(data)
        df = calculate_sma(df,5)
        print(df)
        buy = True if df['SMA5'].head(1)[0] > df[0].head(1)[0] else False
        if buy:
            order_engine.submit_buy_order('TSLA',1)

