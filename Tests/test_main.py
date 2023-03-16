"""Test the main module"""
from unittest.mock import patch, Mock
from life_expectancy.main import Countries, main
from .fixtures.mock_date import fixture_raw_tsv

def test_list_country():
    """Test Country list function"""

    countries_list_actual = Countries.list()
    countries_list_expected = [
        'AUSTRIA', 'BELGIUM', 'BULGARIA', 'SWITZERLAND', 'CYPRUS', 'CZECHIA', 'DENMARK',
        'ESTONIA', 'GREECE', 'SPAIN', 'FINLAND', 'FRANCE', 'CROACIA', 'HUNGARY', 
        'ICELAND', 'ITALY', 'LIECHTENSTEIN', 'LITHUANIA', 'LUXEMBOURG', 'LATVIA',
        'MALTA', 'NETHERLANDS', 'NORWAY', 'POLAND', 'PORTUGAL', 'ROMANIA', 'SWEDEN',
        'SLOVENIA', 'SLOVAKIA', 'GERMANY', 'ALBANIA', 'IRELAND', 'MONTENEGRO', 
        'NORTH_MACEDONIA', 'SERBIA', 'ARMENIA', 'AZERBAIJAN', 'GEORGIA', 'TURKEY',
        'UKRAINE', 'BELARUS', 'UNITED_KINGDOM', 'KOSOVO', 'FRANCE_METROPOLITAN',
        'MOLDOVA', 'SAN_MARINO', 'RUSSIA'
    ]

    assert not set(countries_list_actual) ^ set(countries_list_expected)

@patch("life_expectancy.main.save_data")
@patch("life_expectancy.etl.pd.read_table")
def test_main(read_table_mock: Mock, write_table_mock: Mock, fixture_raw_tsv):
    """Integration test e2e"""

    read_table_mock.return_value = fixture_raw_tsv
    main('test.tsv', 'Portugal')
    read_table_mock.assert_called_once()
    write_table_mock.assert_called_once()
