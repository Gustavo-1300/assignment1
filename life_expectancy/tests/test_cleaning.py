"""Tests for the cleaning module"""
import pandas as pd

from life_expectancy.cleaning import load_data, clean_data, save_data
from . import OUTPUT_DIR


def test_clean_data(pt_life_expectancy_expected):
    """Run the `clean_data` function and compare the output to the expected output"""
    expected_file_name = 'pt_life_expectancy.csv'

    pt_life_expectancy_data = load_data(
        file_name='eu_life_expectancy_raw.tsv'
    )

    pt_life_expectancy_data = clean_data(
        life_data=pt_life_expectancy_data,
        region='PT'
    )

    save_data(
        data_to_save=pt_life_expectancy_data,
        file_name=expected_file_name
    )

    pt_life_expectancy_actual = pd.read_csv(
        OUTPUT_DIR / expected_file_name
    )
    pd.testing.assert_frame_equal(
        pt_life_expectancy_actual, pt_life_expectancy_expected
    )
