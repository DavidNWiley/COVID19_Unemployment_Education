import pandas as pd
import numpy as np


def main():
    # import covid
    covid = pd.read_csv("covid_cleaned.csv", dtype={
                        'fips': np.str})
    # create dataframe
    covid_df = covid
    # display first 5 rows of  dataframe
    print('Below are the first 5 rows of the dataframe')
    print(covid_df.head())

    # import unemployment
    unemp = pd.read_csv("unemployment_clean.csv", dtype={
                        'Full_Fips': np.str, 'Labor_Force': np.int})
    # create dataframe
    unemp_df = unemp
    # display first 5 rows of  dataframe
    print('Below are the first 5 rows of the dataframe')
    print(unemp_df.head())

    # join unemployment and covid df's
    final_df = pd.merge(unemp_df, covid_df, how="left", left_on=[
                        'Full_Fips', 'Period'], right_on=['fips', 'date'])
    # print head of unemployment and covid merge
    print(final_df.head())

    # drop extra columns
    final_df.drop(columns=['State_Fips', 'County_Fips', 'date',
                           'county', 'state', 'fips'], inplace=True)

    print(final_df.head())
    # fill na cases with 0 (ie before covid was recorded in the county)
    final_df['cases'].fillna(0, inplace=True)
    final_df['deaths'].fillna(np.int(0), inplace=True)
    print(final_df.head())

    # read education csv
    edu = pd.read_csv("edu_cleaned.csv", dtype={'Fips': np.str})
    # # create dataframe
    edu_df = edu
    # display first 5 rows of  dataframe
    print('Below are the first 5 rows of the dataframe')
    print(edu_df.head())

    # merge education with previous merge - linking all three
    final_all_df = pd.merge(final_df, edu_df, how="left", left_on=[
        'Full_Fips'], right_on=['Fips'])

    # drop extra fips column
    final_all_df.drop(columns=['Fips'], inplace=True)

    print(final_all_df.head())
    final_all_df.to_csv('final_completed.csv')

    print(final_all_df.corr())
    print(final_all_df.dtypes)
    print(final_all_df.count())


main()
