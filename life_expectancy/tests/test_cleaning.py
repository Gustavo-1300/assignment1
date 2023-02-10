"""Tests for the cleaning module"""
import pandas as pd
import pytest
from life_expectancy.cleaning import clean_data
from life_expectancy.tests.fixtures.mock_date import data_raw, data_expect


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

def test_clean_data():
    """Run the `clean_data` function and compare the output to the expected output"""

    pt_life_expectancy_data = clean_data(
        life_data=fixture_raw(),
        region='PT'
    )

    pd.testing.assert_frame_equal(
        pt_life_expectancy_data, fixture_expect()
    )
