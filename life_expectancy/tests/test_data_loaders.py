"""Tests for data loaders classes"""
from unittest.mock import patch, Mock
import pytest
import pandas as pd
from life_expectancy.data_loaders import LoadDataTSV
from life_expectancy.tests.fixtures.mock_date import data_raw
from . import OUTPUT_DIR

@pytest.fixture
def fixture_raw():
    """
    Load mock raw data
    :return: Dict with raw data mocked
    """

    return pd.DataFrame(data_raw())

@patch("life_expectancy.cleaning.pd.read_table")
def test_load_data_tsv(read_table_mock: Mock, fixture_raw):
    """Run the data load"""
    read_table_mock.return_value = fixture_raw
    data_loader = LoadDataTSV()
    results = data_loader.read_data('eu_life_expectancy_raw.tsv', OUTPUT_DIR)
    read_table_mock.assert_called_once()

    pd.testing.assert_frame_equal(results, fixture_raw)
