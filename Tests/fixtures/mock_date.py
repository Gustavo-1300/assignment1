"Fixtures for testing"
import pathlib
import pytest
import pandas as pd

path_files = pathlib.Path(__file__).parent

@pytest.fixture(scope='module')
def fixture_raw_tsv() -> pd.DataFrame:
    """
    Load mock raw data
    :return: DataFrame with raw data mocked
    """

    return pd.read_json(path_files / 'data_raw_tsv.json',orient='table')

@pytest.fixture(scope='module')
def fixture_tabular() -> pd.DataFrame:
    """
    Load mock tabular data
    :return: DataFrame with tabular data mocked
    """

    return pd.read_json(path_files / 'data_tabular.json',orient='table')

@pytest.fixture(scope='module')
def fixture_with_floats() -> pd.DataFrame:
    """
    Load mock data with floats
    :return: DataFrame with data with floats mocked
    """

    return pd.read_json(path_files / 'data_with_floats.json',orient='table')

@pytest.fixture(scope='module')
def fixture_loaded() -> pd.DataFrame:
    """
    Load mock loaded data
    :return: DataFrame with loaded data mocked
    """

    return pd.read_json(path_files / 'data_loaded.json',orient='table')

@pytest.fixture(scope='module')
def fixture_expect() -> pd.DataFrame:
    """
    Load mock expected data
    :return: DataFrame with expected data mocked
    """

    return pd.read_json(path_files / 'data_expect.json',orient='table')
