# Importing required libraries
import pandas as pd
import numpy as np

"""
    Read a CSV file with a specific date format and set the date column as the index.

    Parameters:
    filename (str): The name/path of the CSV file to read.

    Returns:
    pandas.DataFrame: A DataFrame containing the data from the CSV file, with the date column
    as the index.

"""
def reads_columns_from_csv(filename):
    # Read the CSV file and specify the date format of the 'date' column and set it as index
    df = pd.read_csv(filename, sep=';', parse_dates=['Date'], index_col='Date',
                     date_parser=lambda x: pd.to_datetime(x, format='%d.%m.%Y'))
    return df


"""
    Predict future prices for a time series, given a start and end date.

    Parameters:
    time_series (pandas.Series): The time series to predict future prices for.
    start_date (str or pandas.Timestamp): The start date of the prediction period.
    end_date (str or pandas.Timestamp): The end date of the prediction period.

    Returns:
    numpy.ndarray: An array of predicted prices, with length equal to the number of days
    between start_date and end_date.

"""
def create_result_data_frame(input_prices):
    # Define the start and end dates for the DataFrame
    start_date = '2024-06-01'
    end_date = '2028-12-31'

    # Create a DataFrame with a date index that starts and ends at the specified dates
    predicted_prices = pd.DataFrame(index=pd.date_range(start=start_date, end=end_date))

    # Predict prices for all time series in input_prices
    for col in input_prices.columns:
        # Call the predict_prices() function on the current column of input_prices,
        # and store the result in a new column of predicted_prices
        predicted_prices[col] = predict_prices(input_prices[col], start_date, end_date)

    # Return the predicted_prices DataFrame
    return predicted_prices


"""
    Predicts the value of a time series for a range of dates.

    Parameters:
    - time_series (pandas.Series or pandas.DataFrame): The time series to predict values for.
      Must have a datetime index.
    - start_date (str): The start date of the range to predict, in a format that pandas.to_datetime() can parse.
    - end_date (str): The end date of the range to predict, in a format that pandas.to_datetime() can parse.

    Returns:
    - predicted_values (numpy.ndarray): An array of predicted values, with one element for each day in the range
      from start_date to end_date (inclusive). Each element is the last value of the input time series.
"""
def predict_prices(time_series, start_date, end_date):
    # Convert start and end dates to pandas datetime objects
    start_date = pd.to_datetime(start_date)
    end_date = pd.to_datetime(end_date)

    # Calculate the number of days between start and end dates, inclusive
    num_days = (end_date - start_date).days + 1

    # Create an array of predicted values, initialized with the last value of the time series
    predicted_values = np.full(num_days, time_series.iloc[-1])

    # Return the array of predicted values
    return predicted_values



if __name__ == '__main__':
    # Define the path to the input CSV file
    input_file_path = "prices_steel.csv"

    # Read the input data from the CSV file
    input_prices = reads_columns_from_csv(input_file_path)

    # Create a DataFrame of predicted prices and add it to the input data
    predicted_prices = create_result_data_frame(input_prices)
    full_times_series = pd.concat([input_prices, predicted_prices])

    # Write the resulting DataFrame to a new CSV file with specified separator, date format, and index label
    full_times_series.to_csv('predict_'+input_file_path, sep=';', date_format='%d.%m.%Y', index_label='Date')
