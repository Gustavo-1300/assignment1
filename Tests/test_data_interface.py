"""Tests for data loaders classes"""
from unittest.mock import patch, Mock
import pytest
import pandas as pd
from life_expectancy.data_interface import DataInterface
from .fixtures.mock_date import data_raw
from . import OUTPUT_DIR

@pytest.fixture
def fixture_raw():
    """
    Load mock raw data
    :return: Dict with raw data mocked
    """

    return pd.DataFrame(data_raw())

@patch("life_expectancy.cleaning.pd.read_table")
def test_Data_Interface_load_data(read_table_mock: Mock, fixture_raw):
    """Run the data load"""
    read_table_mock.return_value = fixture_raw
    data_interface = DataInterface(
        file_name='test.tsv',
        path=OUTPUT_DIR
    )
    results = data_interface.load_data()
    read_table_mock.assert_called_once()

    pd.testing.assert_frame_equal(results, fixture_raw)
