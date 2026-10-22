import pandas
import pathlib

def export_data(dataframe):
    
    file_selector = int(input("Save to: 1. csv 2. xlxs 3. Both "))
    write_file = str(input("Input desired filename for exported file: "))
    
    match file_selector: #Create a file containing all the data.
        case 1:
            dataframe.to_csv(write_file + ".csv", index = False)
        case 2:
            dataframe.to_excel(write_file + ".xlsx", index = False)
        case 3:
            dataframe.to_csv(write_file + ".csv", index = False)
            dataframe.to_excel(write_file + ".xlsx", index = False)

def pool_csv(csv_path):
    files = pathlib.Path(csv_path)#Path to all data files
    dataframe = pandas.DataFrame()
    data_list = []
    
    for file in files.iterdir(): #Create a list with all .csv files.
        current_data = pandas.read_csv(file)
        data_list.append(current_data)
        
    dataframe = pandas.concat(data_list) #Merge all the dataframes.
    dataframe = dataframe.reset_index(drop = True)
    
    export_data(dataframe)
            
def segment_data(filename):
    dataframe = pandas.DataFrame()
    
    if filename.endswith(".csv"):
        dataframe = pandas.read_csv(filename)
    elif filename.endswith(".xlsx"):
        dataframe = pandas.read_excel(filename)
    print(f"File has dates between, {dataframe['Date'].min()}"
          f" and {dataframe['Date'].max()}")
    
    start_date = str(input("Select start date of data: "))
    end_date = str(input("Select end date of data: "))
    
    segmented_dataframe = dataframe[(dataframe["Date"] > start_date) & 
                                    (dataframe["Date"] < end_date)]
    segmented_dataframe = segmented_dataframe.reset_index(drop = True)
    
    export_data(segmented_dataframe)
    
def load_data(filename):
    dataframe = pandas.DataFrame()
    
    if filename.endswith(".csv"):
        dataframe = pandas.read_csv(filename)
    elif filename.endswith(".xlsx"):
        dataframe = pandas.read_excel(filename)
        
    return dataframe

def sort_by_ticker(dataframe, concat = True):
    
    sorted_dataframe = dataframe
    sorted_dataframe = sorted_dataframe.sort_values(by = "Date")
    
    ticker_set = set(sorted_dataframe["Ticker"])
    
    ticker = []
    
    for x in ticker_set:
        new_data = sorted_dataframe[sorted_dataframe["Ticker"] == x]
        ticker.append(new_data)
        
    
    sorted_dataframe = ticker
    
    if concat == True:
        sorted_dataframe = pandas.concat(ticker)
    
    return sorted_dataframe

def remove_negatives(dataframe, column):
    
    rows_to_remove = []
    
    for x in range(len(dataframe)):
        if dataframe.iloc[x]["Close"] < 0:
            rows_to_remove.append(x)
            
    for z in rows_to_remove:
        dataframe = dataframe.drop(z)
    
    return dataframe