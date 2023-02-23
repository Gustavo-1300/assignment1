"""Module for cleaning code and saving data transformed"""
import argparse
import pathlib
import pandas as pd

# Define path of files
full_path: pathlib.Path = pathlib.Path(__file__).parent / 'data'

def load_data(
    file_name: str,
    path_file: pathlib.Path
) -> pd.DataFrame:
    """
    Load specified file as a pandas DataFrame from data directory
    :param file_name: Name of the file to be loaded
    :param path_file: Path to the file

    :return: Pandas DataFrame with loaded data
    """

    # Get file's path
    data_loaded = pd.read_table(path_file / file_name)

    return data_loaded


def clean_data(
    life_data: pd.DataFrame,
    region: str = 'PT'
) -> pd.DataFrame:
    """
    Perform cleaning and filtering on a given table with life expectancy data
    :param life_data: Pandas DataFRame with data of life expectancy
    :param region: Region to select data from

    :return: Pandas DataFramed cleaned and filtered
    """

    # Pivot data to long format
    old_column = life_data.columns[0]
    new_columns = old_column.split(',')

    life_data[new_columns] = life_data[old_column].str.split(',', expand=True)
    life_data = life_data.drop(columns=old_column)

    life_data_pivoted = life_data.melt(
        new_columns,
        var_name='year',
        value_name='value'
        )

    # Rename the column with region data
    rename_columns = {
        life_data_pivoted.columns[3]: 'region'
        }
    life_data_pivoted = life_data_pivoted.rename(columns=rename_columns)

    # Get columns of year and value to int and float
    life_data_pivoted['year'] = life_data_pivoted['year'].astype('int')

    float_regex = r'([0-9]+\.?[0-9])'
    life_data_pivoted['value'] = life_data_pivoted['value'].str.extract(float_regex).astype('float')
    life_data_cleaned = life_data_pivoted[~life_data_pivoted['value'].isna()]

    # Filter data to user specified region
    life_data_cleaned = life_data_cleaned[life_data_cleaned['region']==region]

    return life_data_cleaned

def save_data( #pylint: disable=useless-return
    data_to_save: pd.DataFrame,
    file_name: str,
    path_file: pathlib.Path
) ->  None:
    """
    Save a pandas DataFrame to a direcotry specified
    :param data_to_save: Pandas DataFrame with data to be saved
    :param file_name: Name to give the file created
    :param path_file: Path where to store the file

    :return: None
    """

    # Get file's path
    data_to_save.to_csv(
        path_file / file_name,
        index=False
    )

    return None

if __name__=='__main__': # pragma: no cover

    # Parse arguments passed through cli
    parser = argparse.ArgumentParser()
    parser.add_argument('region')
    args = parser.parse_args()

    life_data_raw = load_data(
        file_name='eu_life_expectancy_raw.tsv',
        path_file=full_path
    )

    life_data_processed = clean_data(
        life_data=life_data_raw,
        region=args.region
    )

    save_data(
        data_to_save=life_data_processed,
        file_name='pt_life_expectancy.csv',
        path_file=full_path
    )
