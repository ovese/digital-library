import pandas as pd
import numpy as np
import yfinance as yf
import psycopg2
from psycopg2.extensions import register_adapter, AsIs 
psycopg2.extensions.register_adapter(np.int64, psycopg2._psycopg.AsIs)
import datetime

#Historical Stock Prices Table
def get_hist_df(ticker):
    df = yf.download(ticker, period = 'max')
    return (df
              .rename(columns = {'Adj Close':'Adj_Close'})
              .assign(
                        Date = np.datetime_as_string(df.index, unit = 'D'),
                        Ticker = ticker)
              .set_index('Date')

              #PostgreSQL requires df to be inserted as records
              .to_records(index = True))
    
#Option Chain Table
def get_options_chain_df(ticker):
    ticker_object = yf.Ticker(ticker)

    #Expirations Dates
    expiration_dates = ticker_object.options
    
    #Chain data for each expiration date
    options = pd.DataFrame()
    for each_date in expiration_dates:
        option_data = ticker_object.option_chain(each_date)
        option_data = pd.DataFrame().append(option_data.calls).append(option_data.puts)
        options = options.append(option_data, ignore_index=True)

    #Cleaning the dataframe for PostgreSQL compatibility                 
    return (options
                    .assign(
                        ticker = ticker,
                        isCall = options['contractSymbol'].str[4:].apply(lambda x: "C" in x),
                        bid = options['bid'].apply(pd.to_numeric),
                        ask = options['ask'].apply(pd.to_numeric),
                        strike = options['strike'].apply(pd.to_numeric),
                        mark_midpoint_of_bid_ask = (options.bid + options.ask)/2,
                        expirationDate = pd.to_datetime(options['contractSymbol'].str[6:8] + '-' + options['contractSymbol'].str[8:10] + '-' + '20' + options['contractSymbol'].str[4:6]),
                            )
                    .drop(columns=['contractSize','currency', 'change', 'percentChange', 'lastTradeDate', 'lastPrice'])
                    .to_records(index = True)
            )  