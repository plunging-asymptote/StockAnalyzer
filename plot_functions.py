import pandas
import matplotlib
import data_functions

def plot_stock(filename, ticker):
    
    dataframe = data_functions.load_data(filename)
    dataframe = data_functions.sort_by_ticker(dataframe, True)

    returns = []
    dates = []

    for x in range(len(dataframe)):
        if ticker == dataframe["Ticker"][x]:
            returns.append(dataframe["Return"][x])
            dates.append(pandas.to_datetime(dataframe["Date"][x]))
    
    
    stock_plot, ax = matplotlib.pyplot.subplots()
    ax.plot(dates, returns)
    matplotlib.pyplot.title(f"Daily returns of {ticker}")
    matplotlib.pyplot.xlabel("Dates")
    matplotlib.pyplot.ylabel("Returns (in %)")
    matplotlib.pyplot.show()

    plot_name = str(input("Input desired filename of plot: "))
    stock_plot.savefig(plot_name + ".png")
