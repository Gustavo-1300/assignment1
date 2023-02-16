"""Tests for the cleaning module"""
import pytest
import pandas as pd
from unittest.mock import patch, Mock
from life_expectancy.cleaning import load_data, clean_data
from life_expectancy.tests.fixtures.mock_date import data_raw, data_expect
from . import OUTPUT_DIR

@pytest.fixture
def fixture_raw():
    """
    Load mock raw data
    :return: Dict with raw data mocked
    """

    return pd.DataFrame(data_raw())

@pytest.fixture
def fixture_expect():
    """
    Load mock expected data
    :return: Dict with prepared data mocked
    """

    return pd.DataFrame(data_expect())

@patch("path.to.file.pandas.read_table")
def test_load_data(fixture_raw, read_table_mock: Mock):
    read_table_mock.return_value = fixture_raw
    results = clean_data(OUTPUT_DIR)
    read_table_mock.assert_called_once()

def test_clean_data(fixture_raw, fixture_expect):
    """Run the `clean_data` function and compare the output to the expected output"""

    pt_life_expectancy_data = clean_data(
        life_data=fixture_raw,
        region='PT'
    ).reset_index(drop=True)

    pd.testing.assert_frame_equal(
        pt_life_expectancy_data, fixture_expect
    )
