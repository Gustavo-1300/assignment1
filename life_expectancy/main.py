"""Module for processing and saving a file"""
import pathlib
import argparse
from itertools import chain
from enum import Enum, unique
from .data_interface import DataInterface
from .etl import save_data

# Define path of files
full_path: pathlib.Path = pathlib.Path(__file__).parent / 'data'

# Define possible countries
@unique
class Countries(Enum):
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
        return [e.value for e in Countries]

# Define possible regions
@unique
class Instituions(Enum):
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

Regions = Enum('Regions', [(i.name, i.value) for i in chain(Countries, Instituions)])

def main(
        file: str,
        region: str
) -> None:
    """
    Function that receives user arguments to process a data file for a choosen region
    :param file: Name of the file with data to process and filter
    :param region: Region to filter data

    :return: None
    """
    region = Regions(region.upper()).name

    data_interface = DataInterface(
        file_name=file,
        path=full_path
    )

    data_interface.load_data()
    data_interface.filter_data(region)

    save_data(
        data_to_save=data_interface.data,
        file_name='pt_life_expectancy.csv',
        path_file=full_path
    )

if __name__=='__main__': # pragma: no cover

    # Parse arguments passed through cli
    parser = argparse.ArgumentParser()
    parser.add_argument('file')
    parser.add_argument('region')
    args = parser.parse_args()

    main(args.file, args.region)
