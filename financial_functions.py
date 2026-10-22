import pandas
import data_functions
import numpy

def calculate_daily_return(filename):

    dataframe = data_functions.load_data(filename)
    
    dataframe = data_functions.remove_negatives(dataframe, "Close")
        
    ticker_open_close = dataframe.sort_values(by = "Ticker")
    
    ticker = data_functions.sort_by_ticker(ticker_open_close, concat = False)
        
    for x in range(len(ticker)):
        ticker[x] = ticker[x].reset_index(drop = True)
        date_range = len(ticker[x]) - 1
        rows_to_remove = []
        y = 1
        while y < date_range:
            date3 = pandas.to_datetime(ticker[x]["Date"].iloc[y - 1])
            date1 = pandas.to_datetime(ticker[x]["Date"].iloc[y])
            date2 = pandas.to_datetime(ticker[x]["Date"].iloc[y + 1])
            gap = (date2 - date1).days
            gap2 = (date1 - date3).days
            """Check if days before or after is more than 1"""
            if gap > 1 and gap2 > 1: 
                date_range = len(ticker[x]) - 1
                rows_to_remove.append(y)
                y += 1
            else:
                y += 1
        for z in rows_to_remove:
            ticker[x] = ticker[x].drop(z)
    
        ticker[x] = ticker[x].reset_index(drop = True)
        list_daily_return = []
        list_positive_negative = []
    
        for x_1 in range(len(ticker[x]) - 1):
            today_date = pandas.to_datetime(ticker[x]["Date"].iloc[x_1 + 1])
            yesterday_date = pandas.to_datetime(ticker[x]["Date"].iloc[x_1])
            gap = (today_date - yesterday_date).days
            if gap > 1:
                list_daily_return.append(0)
                list_positive_negative.append(3)
            else:
                today_close = ticker[x]["Close"].iloc[x_1 + 1]
                yesterday_close = ticker[x]["Close"].iloc[x_1]
                daily_return = (
                    ((today_close - yesterday_close) / yesterday_close) * 100)
                if daily_return > 0:
                    list_positive_negative.append(1)
                elif daily_return < 0:
                    list_positive_negative.append(0)
                else:
                    list_positive_negative.append(3)
                list_daily_return.append(daily_return)
            
        ticker[x] = ticker[x].drop(0)
        ticker[x] = ticker[x].reset_index(drop = True)
        ticker[x]["Return"] = list_daily_return
        ticker[x]["IsPositiveReturn"] = list_positive_negative
    
    master_ticker = pandas.concat(ticker)
    
    data_functions.export_data(master_ticker)

def return_details(filename):
    
    dataframe = data_functions.load_data(filename)
    
    stock_returns = dataframe["Return"]
        
    index_high_return = numpy.argmax(stock_returns)
    print(f"Highest return was: "
          f"{dataframe.iloc[index_high_return]['Return']:.2f}"
          f" by {dataframe.iloc[index_high_return]['Ticker']}"
          f" on {dataframe.iloc[index_high_return]['Date']}.")
    
    index_low_return = numpy.argmin(stock_returns)
    print(f"Lowest return was: "
          f"{dataframe.iloc[index_low_return]['Return']:.2f}"
          f" by {dataframe.iloc[index_low_return]['Ticker']}"
          f" on {dataframe.iloc[index_low_return]['Date']}.")
    
    ticker_set = set(dataframe["Ticker"])
    ticker = []
    for x in ticker_set:
        new_data = dataframe[dataframe["Ticker"] == x]
        ticker.append(new_data)
    
    
    for x in range(len(ticker)):
        average_return = numpy.average(ticker[x]["Return"])
        best_day_index = numpy.argmax(ticker[x]["Return"])
        worst_day_index = numpy.argmin(ticker[x]["Return"])
        print(f"Average daily return of {ticker[x].iloc[0]['Ticker']}"
              f" is {average_return:.2f}."
              f" Best day: {ticker[x].iloc[best_day_index]['Date']}"
              f" return: {ticker[x].iloc[best_day_index]['Return']:.2f}."
              f" Worst day: {ticker[x].iloc[worst_day_index]['Date']}"
              f" return: {ticker[x].iloc[worst_day_index]['Return']:.2f}.")
    
    export_select = int(input("Do you want to export data? 1. Yes. 2. No "))
    
    if export_select == 1:
        return_detail_df = pandas.DataFrame()
        ticker_name_list = []
        average_return_list = []
        best_return_list = []
        best_return_day_list = []
        worst_return_list = []
        wrost_return_day_list = []
        for x in range(len(ticker)):
            average_return = numpy.average(ticker[x]["Return"])
            best_day_index = numpy.argmax(ticker[x]["Return"])
            best_return = ticker[x].iloc[best_day_index]["Return"]
            best_return_day = ticker[x].iloc[best_day_index]["Date"]
            worst_day_index = numpy.argmin(ticker[x]["Return"])
            worst_return = ticker[x].iloc[worst_day_index]["Return"]
            worst_return_day = ticker[x].iloc[worst_day_index]["Date"]
            
            ticker_name_list.append(ticker[x].iloc[0]["Ticker"])
            average_return_list.append(average_return)
            best_return_list.append(best_return)
            best_return_day_list.append(best_return_day)
            worst_return_list.append(worst_return)
            wrost_return_day_list.append(worst_return_day)
        
        return_detail_df["Ticker"] = ticker_name_list
        return_detail_df["Average_return"] = average_return_list
        return_detail_df["Best_return"] = best_return_list
        return_detail_df["Best_return_date"] = best_return_day_list
        return_detail_df["Worst_return"] = worst_return_list
        return_detail_df["Worst_return_date"] = worst_return_day
        
        data_functions.export_data(return_detail_df)
        print("Succesfully exported.")