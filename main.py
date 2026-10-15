import data_functions
import financial_functions
      
def main():
    running = True
    selected = False
    while running:
        try:
            choice_selector = int(input("Select an option:" 
                                    " 1. Pool CSV data." 
                                    " 2. Segment data based on date."
                                    " 3. Calculate daily returns." 
                                    " 4. Show return details. "
                                    " 9. Exit "))
            selected = True
        except ValueError:
            print("Only enter numbers!")
            
        if selected == True:
            match choice_selector:
                case 1:
                    csv_path = str(input
                                   ("Input the folder containg .csv files:"))
                    try: 
                        data_functions.pool_csv(csv_path)
                        print("Successfully pooled data")
                    except Exception as e:
                        print(f"Error: {e}")
                case 2:
                    filename = str(input("Input filename of data: "))
                    try:
                        data_functions.segment_data(filename)
                        print("Successfully segmented data")
                    except Exception as e:
                        print(f"Error: {e}")
                case 3:
                    try:
                        filename = str(input("Input filename of data: "))
                        financial_functions.calculate_daily_return(filename)
                        print("Successfully calculated daily return data")
                    except Exception as e:
                        print(f"Error: {e}")
                case 4:
                    try:
                        filename = str(input("Input filename of data: "))
                        financial_functions.return_details(filename)
                    except Exception as e:
                        print(f"Error: {e}")
                case 9:
                    running = False
            
                
                
main()
