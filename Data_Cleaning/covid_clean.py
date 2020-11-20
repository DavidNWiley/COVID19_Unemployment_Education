import pandas as pd
import numpy as np


def main():
    # import csv
    covid = pd.read_csv("covid_data.csv", dtype={'fips': np.str})
    # create dataframe
    df = covid
    # display first 5 rows of  dataframe
    print('Below are the first 5 rows of the dataframe')
    print(df.head())

    # create list of last day of the month to match with covid data
    lastday = ['2020-01-31', '2020-02-29', '2020-03-31', '2020-04-30',
               '2020-05-31', '2020-06-30', '2020-07-31', '2020-08-31', '2020-09-30']

    # drop all days not in lastday list
    df = df[df['date'].isin(lastday)]

    # next line creates a warning
    # replace dates to match format in unemployment, where the value will be the total cases at the end of the month
    df['date'].replace({'2020-01-31': 'Jan-20', '2020-02-29': 'Feb-20', '2020-03-31': 'Mar-20', '2020-04-30': 'Apr-20',
                        '2020-05-31': 'May-20', '2020-06-30': 'Jun-20', '2020-07-31': 'Jul-20', '2020-08-31': 'Aug-20', '2020-09-30': 'Sep-20'}, inplace=True)

    print(df.head())

    df.to_csv('covid_cleaned.csv', index=False)


main()
