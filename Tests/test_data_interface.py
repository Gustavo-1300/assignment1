"""Tests for data loaders classes"""
from unittest.mock import patch, Mock
import pytest
import pandas as pd
from life_expectancy.data_interface import DataInterface
from .fixtures.mock_date import fixture_raw_tsv, fixture_loaded
from . import OUTPUT_DIR

@patch("life_expectancy.etl.pd.read_table")
def test_data_interface_load_data(read_table_mock: Mock, fixture_raw_tsv, fixture_loaded):
    """Run the data load"""
    read_table_mock.return_value = fixture_raw_tsv
    data_interface = DataInterface(
        file_name='test.tsv',
        path=OUTPUT_DIR
    )
    data_interface.load_data()
    read_table_mock.assert_called_once()

    pd.testing.assert_frame_equal(data_interface.data, fixture_loaded)
