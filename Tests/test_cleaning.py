"""Tests for the cleaning module"""
from unittest.mock import patch
import pytest
import pandas as pd
from life_expectancy import cleaning
from .fixtures.mock_date import data_raw_tsv, data_expect, data_tabular, data_with_floats
from . import OUTPUT_DIR

@pytest.fixture
def fixture_raw():
    """
    Load mock raw data
    :return: Dict with raw data mocked
    """

    return pd.DataFrame(data_raw_tsv())

@pytest.fixture
def fixture_expect():
    """
    Load mock expected data
    :return: Dict with prepared data mocked
    """

    return pd.DataFrame(data_expect())

@pytest.fixture
def fixture_tabular():
    """
    Load mock tabular data
    :return: Dict with tabular data mocked
    """

    return pd.DataFrame(data_tabular())

@pytest.fixture
def fixture_floats():
    """
    Load mock float data
    :return: Dict with float data mocked
    """

    return pd.DataFrame(data_with_floats())

def test_transform_data_into_tabular(fixture_raw, fixture_tabular):
    """Run the 'transform_data_into_tabular' function and compare expected output"""

    data_observed = cleaning.transform_data_into_tabular(fixture_raw)

    pd.testing.assert_frame_equal(data_observed, fixture_tabular)

def test_extract_floats(fixture_tabular, fixture_floats):
    """Run the 'extract_floct' function and compare expected output"""

    data_observed = cleaning.extract_floats(fixture_tabular)

    pd.testing.assert_frame_equal(data_observed, fixture_floats)

def test_save_data(fixture_expect, capfd):
    """Run the 'save_data'"""
    with patch.object(fixture_expect, 'to_csv') as to_csv_mock:
        to_csv_mock.side_effect = print('Data saved', end="")
        cleaning.save_data(
            fixture_expect,
            'pt_life_expectancy.csv',
            OUTPUT_DIR
        )
        to_csv_mock.assert_called_once()

        # capfd is a Pytest fixture that captures the output of the print statement
        out, _ = capfd.readouterr()
        assert out == "Data saved"
