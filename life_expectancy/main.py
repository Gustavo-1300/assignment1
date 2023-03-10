"""Module for processing and saving a file"""
import pathlib
import argparse
from enum import Enum, unique
from .data_interface import DataInterface
from .cleaning import save_data

# Define path of files
full_path: pathlib.Path = pathlib.Path(__file__).parent / 'data'

# Define possible countries
@unique
class Country(Enum):
    """Existing regions in dataset"""
    AT = 'AUSTRIA'
    BE = 'BELGIUM'
    BG = 'BULGARIA'
    CH = 'SWITZERLAND'
    CY = 'CYPRUS'
    CZ = 'CZECHIA'
    DK = 'DENMARK'
    EE = 'ESTONIA'
    EL = 'GREECE'
    ES = 'SPAIN'
    FI = 'FINLAND'
    FR = 'FRANCE'
    HR = 'CROACIA'
    HU = 'HUNGARY'
    IS = 'ICELAND'
    IT = 'ITALY'
    LI = 'LIECHTENSTEIN'
    LT = 'LITHUANIA'
    LU = 'LUXEMBOURG'
    LV = 'LATVIA'
    MT = 'MALTA'
    NL = 'NETHERLANDS'
    NO = 'NORWAY'
    PL = 'POLAND'
    PT = 'PORTUGAL'
    RO = 'ROMANIA'
    SE = 'SWEDEN'
    SI = 'SLOVENIA'
    SK = 'SLOVAKIA'
    DE = 'GERMANY'
    AL = 'ALBANIA'
    IE = 'IRELAND'
    ME = 'MONTENEGRO'
    MK = 'NORTH_MACEDONIA'
    RS = 'SERBIA'
    AM = 'ARMENIA'
    AZ = 'AZERBAIJAN'
    GE = 'GEORGIA'
    TR = 'TURKEY'
    UA = 'UKRAINE'
    BY = 'BELARUS'
    UK = 'UNITED_KINGDOM'
    XK = 'KOSOVO'
    FX = 'FRANCE_METROPOLITAN'
    MD = 'MOLDOVA'
    SM = 'SAN_MARINO'
    RU = 'RUSSIA'

    @staticmethod
    def list():
        """Print list of countries"""
        return [e.value for e in Country]

# Define possible regions
@unique
class Region(Enum):
    """Existing regions in dataset"""
    EU_27_2020 = 'EUROPEAN_UNION'
    DE_TOT = 'GERMANY_TOT'
    EA_18 = 'EURO_AREA_18'
    EA_19 = 'EURO_AREA_19'
    EFTA = 'EUROPE_FREE_TRADE_ASSOCIATION'
    EEA30_2007 = 'EUROPEAN_ECONOMIC_AREA_2007'
    EEA31 = 'EUROPEAN_ECONOMIC_AREA'
    EU27_2007 = 'EUROPEAN_UNION_2007'
    EU28 = 'EUROPEAN_UNION_28'

if __name__=='__main__': # pragma: no cover

    # Parse arguments passed through cli
    parser = argparse.ArgumentParser()
    parser.add_argument('file')
    parser.add_argument('region')
    args = parser.parse_args()

    # Parse the region argument
    try:
        region = Country(args.region.upper()).name
    except ValueError:
        try:
            region = Region(args.region.upper()).name
        except ValueError:
            print(f'{args.region} is not a valid region')

    data_interface = DataInterface(
        file_name=args.file,
        path=full_path
    )

    data_interface.load_data()
    data_interface.filter_data(region)

    save_data(
        data_to_save=data_interface.data,
        file_name='pt_life_expectancy.csv',
        path_file=full_path
    )
