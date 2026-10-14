import pandas
import data_functions

def calculate_daily_return(filename):
    dataframe = pandas.DataFrame()
    
    if filename.endswith(".csv"):
        dataframe = pandas.read_csv(filename)
    elif filename.endswith(".xlsx"):
        dataframe = pandas.read_excel(filename)
        
        
    ticker_open_close = dataframe[["Ticker", "Date", "Open", "Close"]]
    ticker_open_close = ticker_open_close.sort_values(by = "Ticker")
    
    ticker_set = set(dataframe["Ticker"])
    
    ticker = []
    
    for x in ticker_set:
        new_data = dataframe[dataframe["Ticker"] == x]
        ticker.append(new_data)
    
    ticker = pandas.concat(ticker)
    ticker = ticker.reset_index(drop = True)
    
    data_range = len(ticker) - 1
    x = 0
    
    rows_to_remove = []
    
    while x < data_range:
        date3 = pandas.to_datetime(ticker["Date"].iloc[x - 1])
        date1 = pandas.to_datetime(ticker["Date"].iloc[x])
        date2 = pandas.to_datetime(ticker["Date"].iloc[x + 1])
        gap = (date2 - date1).days
        gap2 = (date1 - date3).days
        """Check if days before or after is more than 1"""
        if gap > 1 and gap2 > 1: 
            data_range = len(ticker) - 1
            rows_to_remove.append(x)
            x += 1
        else:
            x += 1
        
    
    for x in rows_to_remove:
        ticker = ticker.drop(x)
    
    ticker = ticker.reset_index(drop = True)
    list_daily_return = []
    
    for x in range(len(ticker) - 1):
        today_close = ticker["Close"].iloc[x + 1]
        yesterday_close = ticker["Close"].iloc[x]
        daily_return = (
            ((today_close - yesterday_close) / yesterday_close) * 100)
        list_daily_return.append(daily_return)
        
    ticker = ticker.drop(0)
    ticker = ticker.reset_index(drop = True)
    ticker["Return"] = list_daily_return
    
    data_functions.export_data(ticker)
    
def function(foo):
    """
    lovely documentation 
    """
    return 