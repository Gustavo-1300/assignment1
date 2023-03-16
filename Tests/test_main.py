"""Test the main module"""
from life_expectancy.main import Country

def test_list_country():
    """Test Country list function"""

    countries_list_actual = Country.list()
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
