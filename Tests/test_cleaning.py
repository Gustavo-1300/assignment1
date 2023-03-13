"""Tests for the cleaning module"""
from unittest.mock import patch
import pytest
import pandas as pd
from assignment1.life_expectancy import etl
from .fixtures.mock_date import fixture_raw_tsv, fixture_expect, fixture_tabular
from .fixtures.mock_date import fixture_with_floats
from . import OUTPUT_DIR

def test_transform_data_into_tabular(fixture_raw_tsv, fixture_tabular):
    """Run the 'transform_data_into_tabular' function and compare expected output"""

    data_observed = etl.transform_data_into_tabular(fixture_raw_tsv)

    pd.testing.assert_frame_equal(data_observed, fixture_tabular)

def test_extract_floats(fixture_tabular, fixture_with_floats):
    """Run the 'extract_floct' function and compare expected output"""

    data_observed = etl.extract_floats(fixture_tabular)

    pd.testing.assert_frame_equal(data_observed, fixture_with_floats)

def test_save_data(fixture_expect, capfd):
    """Run the 'save_data'"""
    with patch.object(fixture_expect, 'to_csv') as to_csv_mock:
        to_csv_mock.side_effect = print('Data saved', end="")
        etl.save_data(
            fixture_expect,
            'pt_life_expectancy.csv',
            OUTPUT_DIR
        )
        to_csv_mock.assert_called_once()

        # capfd is a Pytest fixture that captures the output of the print statement
        out, _ = capfd.readouterr()
        assert out == "Data saved"
