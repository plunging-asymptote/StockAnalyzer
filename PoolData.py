import os
import pandas

def main():
    files = os.listdir("./CSV_Data") #Put all .csv files into a folder named CSV_Data.
    dataframe = pandas.DataFrame()
    data_list = []
    
    for file in files: #Create a list with all .csv files.
        filepath = "./CSV_Data/" + file
        current_data = pandas.read_csv(filepath)
        data_list.append(current_data)
        
    dataframe = pandas.concat(data_list) #Merge all the dataframes.
    dataframe = dataframe.reset_index(drop = True)
    
    dataframe.to_csv("2008to2023Data.csv") #Create a .csv file containing all the data.
    
main()
