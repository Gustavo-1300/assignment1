"""Module for cleaning code and saving data transformed"""
import argparse
import pathlib
import pandas as pd

def load_data(
    file_name: str,
    path: str
) -> pd.DataFrame:
    """
    Load specified file as a pandas DataFrame from data directory
    :param file_name: Name of the file to be loaded

    :return: Pandas DataFrame with loaded data
    """

    path = pathlib.Path(__file__).parent / 'data'
    data_loaded = pd.read_table(path / file_name)

    return data_loaded


def clean_data( #pylint: disable=useless-return
    region: str = 'PT'
) -> None:
    """
    Read life expactancy data and perform cleaning and filtering before saving as a csv file
    :param region: Region to select data from

    :return: None
    """

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

    return None

def save_data(
    data_to_save: pd.DataFrame,
    file_name: str,
    path: str
) ->  None:
    """
    Save a pandas DataFrame to a direcotry specified
    :param data_to_save: Pandas DataFrame with data to be saved
    :param file_name: Name to give the file created
    :param path: Path to the directory where to store the file

    :return: None
    """

    file_save = 'pt_life_expectancy.csv'
    data_to_save.to_csv(path / file_save, index=False)

    return None

if __name__=='__main__': # pragma: no cover
    parser = argparse.ArgumentParser()
    parser.add_argument('region')
    args = parser.parse_args()

    clean_data(region=args.region)
