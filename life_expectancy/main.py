"""Module for processing and saving a file"""
import pathlib
import argparse
from enum import Enum, unique
from data_interface import DataInterface
from cleaning import save_data

# Define path of files
full_path: pathlib.Path = pathlib.Path(__file__).parent / 'data'

# Define possible regions
@unique
class Country(Enum):
    """Existing regions in dataset"""
    AUSTRIA = 'AT'
    BELGIUM = 'BE'
    BULGARIA = 'BG'
    SWITZERLAND = 'CH'
    CYPRUS = 'CY'
    CZECHIA = 'CZ'
    DENMARK = 'DK'
    ESTONIA = 'EE'
    GREECE = 'EL'
    SPAIN = 'ES'
    EUROPEAN_UNION = 'EU27_2020'
    FINLAND = 'FI'
    FRANCE = 'FR'
    CROACIA = 'HR'
    HUNGARY = 'HU'
    ICELAND = 'IS'
    ITALY = 'IT'
    LIECHTENSTEIN = 'LI'
    LITHUANIA = 'LT'
    LUXEMBOURG = 'LU'
    LATVIA = 'LV'
    MALTA = 'MT'
    NETHERLANDS = 'NL'
    NORWAY = 'NO'
    POLAND = 'PL'
    PORTUGAL = 'PT'
    ROMANIA = 'RO'
    SWEDEN = 'SE'
    SLOVENIA = 'SI'
    SLOVAKIA = 'SK'
    GERMANY = 'DE'
    GERMANY_TOT = 'DE_TOT'
    ALBANIA = 'AL'
    EURO_AREA_18 = 'EA18'
    EURO_AREA_19 = 'EA19'
    EUROPE_FREE_TRADE_ASSOCIATION = 'EFTA'
    IRELAND = 'IE'
    MONTENEGRO = 'ME'
    NORTH_MACEDONIA = 'MK'
    SERBIA = 'RS'
    ARMENIA = 'AM'
    AZERBAIJAN = 'AZ'
    GEORGIA = 'GE'
    TURKEY = 'TR'
    UKRAINE = 'UA'
    BELARUS = 'BY'
    EUROPEAN_ECONOMIC_AREA_2007 = 'EEA30_2007'
    EUROPEAN_ECONOMIC_AREA = 'EEA31'
    EUROPEAN_UNION_2007 = 'EU27_2007'
    EUROPEAN_UNION_28 = 'EU28'
    UNITED_KINGDOM = 'UK'
    KOSOVO = 'XK'
    FRANCE_METROPOLITAN = 'FX'
    MOLDOVA = 'MD'
    SAN_MARINO = 'SM'
    RUSSIA = 'RU'

if __name__=='__main__': # pragma: no cover

    # Parse arguments passed through cli
    parser = argparse.ArgumentParser()
    parser.add_argument('file')
    parser.add_argument('region')
    args = parser.parse_args()

    data_interface = DataInterface(
        file_name=args.file,
        path=full_path
    )

    data_interface.load_data()
    data_interface.filter_data(args.region)

    save_data(
        data_to_save=data_interface.data,
        file_name='pt_life_expectancy.csv',
        path_file=full_path
    )