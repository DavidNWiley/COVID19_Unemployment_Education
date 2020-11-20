import pandas as pd
import numpy as np


def main():
    # import csv
    education = pd.read_csv("education.csv", header=None)
    # create dataframe
    df = education
    # display first 5 rows of  dataframe
    print('Below are the first 5 rows of the raw dataframe')
    print(df.head())

    # drop unnecessary rows (doc title, general info)and columns
    df.drop([0, 1, 2, 3], inplace=True)
    # drop unecessary columns (everything before 2014-2018 (most recent) data)
    df.drop(df.iloc[:, 3:43], inplace=True, axis=1)
    print('After dropping unnecessary rows and columns')
    print(df.head())

    # create column headings
    headings = ['Fips', 'State', 'Area_Name', 'Less_HS_Dip_pct',
                'HS_Dipl_pct', 'Some_col_pct', 'Bach_plus_pct']
    # drop previous heading and set headings
    df.drop([4], inplace=True)
    df.columns = headings

    # drop state and area_name
    df.drop(columns=['State', 'Area_Name'], inplace=True)

    print(df.head())

    df.to_csv('edu_cleaned.csv', index=False)


main()
