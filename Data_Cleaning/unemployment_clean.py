import pandas as pd
import numpy as np


def main():
    # import csv
    unemployment = pd.read_csv("unemployment.csv", header=None)
    # create dataframe
    df = unemployment
    # display first 5 rows of  dataframe
    print('Below are the first 5 rows of the raw dataframe')
    print(df.head())

    # drop unnecessary rows (first blank rows/doc title)
    df.drop([0, 1], inplace=True)
    # drop unecessary columns (LAUS code, # employed, # unemployed)
    df.drop(columns=[0, 6, 7], inplace=True)
    print('After dropping unnecessary rows and columns')

    print(df.head())

    # rename column headings
    headings = ['State_Fips', 'County_Fips', 'County_State', 'Period',
                'Labor_Force', 'Unemployment_Rate']
    df.columns = headings
    print('Renaming column headings')

    print(df.head())

    # drop extra rows (the previous column headings)
    print('Dropping extra rows')
    df.drop([2, 3, 4, 5], inplace=True)
    # reset index after dropping rows
    df.reset_index(inplace=True, drop=True)
    print(df.head())

    # concat state and county fips to create full fips identifier (must be string)
    print('Creating full fips identifier')
    df['Full_Fips'] = df['State_Fips'].astype(
        str) + df['County_Fips'].astype(str)

    print(df.head())

    # split county and state into two seperate columns and drop previous combined column
    df[['County', 'State']] = df.County_State.str.split(",", expand=True,)
    print(df.head())
    df.drop(columns=['County_State'], inplace=True)
    print(df.head())

    # split month and year into two seperate columns
    df[['Month', 'Year']] = df.Period.str.split("-", expand=True,)
    print(df.head())

    # split year and prelim identifier into two seperate columns (july 2020 data)
    df[['Year', 'Preliminary']] = df.Year.str.split(" ", expand=True,)
    print(df.head())

    print('List rows with null Year column and remove them')
    print(df[df['Year'].isnull()])
    df.drop([45066, 45067, 45068], inplace=True)
    # check null year values have been removed, rows indicate source and do not contain data
    print(df[df['Year'].isnull()])

    # drop preliminary column
    df.drop(columns=['Preliminary'], inplace=True)

    # find and remove 2019 unemployment data
    bad2019 = df[df['Year'].astype(int) == 19].index
    df.drop(bad2019, inplace=True)

    # find and remove puerto rico data
    puertorico = df[df['State'].astype(str) == ' PR'].index
    df.drop(puertorico, inplace=True)

    # drop month and year columns (finished using them to remove 2019 data)
    df.drop(columns=['Month', 'Year'], inplace=True)

    # split period to have a period column and a preliminary column.
    # will join covid data on period
    df[['Period', 'Preliminary_Unemp_Data']
       ] = df.Period.str.split(" ", expand=True)

    # update prelim column to true/false
    df['Preliminary_Unemp_Data'].fillna('False', inplace=True)
    df['Preliminary_Unemp_Data'].replace({'p': 'True'}, inplace=True)

    # remove comma from labor force so it can be converted to a number
    df['Labor_Force'] = df['Labor_Force'].str.replace(',', '')

    # populate state for DC
    print('List rows with null State column')
    print(df[df['State'].isnull()])
    print('DC does not have a state, populate state value with DC')
    df['State'].fillna('DC', inplace=True)

    # print head and tail
    print('Below is the beginning and the end of the dataset')
    print(df.head())
    print(df.tail())

    df.to_csv('unemployment_clean.csv', index=False)


main()
