"""Module for cleaning code and saving data transformed"""
import pathlib
import pandas as pd

def transform_data_into_tabular(
    raw_data: pd.DataFrame
) -> pd.DataFrame:
    """
    Transform DataFrame into tabular data
    :param raw_data: DataFrame with data to pivot

    :return: DataFrame in tabular form
    """

    old_column = raw_data.columns[0]
    new_columns = old_column.split(',')

    raw_data[new_columns] = raw_data[old_column].str.split(',', expand=True)
    raw_data = raw_data.drop(columns=old_column)

    tabular_data = raw_data.melt(
        new_columns,
        var_name='year',
        value_name='life_expectancy'
    )

    return tabular_data

def extract_floats(
    tabular_data: pd.DataFrame
) -> pd.DataFrame:
    """
    Filter only rows with float like values and convert them
    :param tabular_data: DataFrame with column of life_expectancy with float like 
    values

    :return: DataFrame with life_expectancy column as float
    """

    # Valus parsed to float
    float_regex = r'([0-9]+\.?[0-9])'
    life_expectancy = tabular_data['life_expectancy'].str.extract(float_regex)

    # Update DataFrame
    tabular_data['life_expectancy'] = life_expectancy.astype('float')
    cleaned_data = tabular_data[~tabular_data['life_expectancy'].isna()]

    return cleaned_data

def save_data(
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

    data_to_save.to_csv(
        path_file / file_name,
        index=False
    )
