"""Module for caening code and saving data transformed"""
import argparse
import pandas as pd

def clean_data( #pylint: disable=useless-return
    region: str = 'PT'
) -> None:
    """
    Read life expactancy data and perform cleaning and filtering before saving as a csv file
    :param region: Region to select data from

    :return: None
    """

    # Load data
    path = '/nfs/backup/wb_mciba_003/gspereira/assignment1/life_expectancy/data/'
    file_read = 'eu_life_expectancy_raw.tsv'
    data = pd.read_table(path+file_read)

    # Pivot data to long format
    old_column = data.columns[0]
    new_columns = old_column.split(',')

    data[new_columns] = data[old_column].str.split(',', expand=True)
    data = data.drop(columns=old_column)

    data = data.melt(
        new_columns,
        var_name='year',
        value_name='value'
        )

    # Rename the column with region data
    rename_columns = {
        data.columns[3]: 'region'
        }
    data = data.rename(columns=rename_columns)

    # Get columns of year and value to int and float
    data['year'] = data['year'].astype('int')

    float_regex = r'([0-9]+\.?[0-9])'
    data['value'] = data['value'].str.extract(float_regex).astype('float')
    data = data[~data['value'].isna()]

    # Filter data to Portugal and save file
    data = data[data['region']==region]

    file_save = 'pt_life_expectancy.csv'
    data.to_csv(path+file_save, index=False)

    return None

if __name__=='__main__': # pragma: no cover
    parser = argparse.ArgumentParser()
    parser.add_argument('region')
    args = parser.parse_args()

    clean_data(region=args.region)
