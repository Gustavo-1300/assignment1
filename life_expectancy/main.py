"""Module for processing and saving a file"""
import pathlib
import argparse
from data_interface import DataInterface
from cleaning import save_data

# Define path of files
full_path: pathlib.Path = pathlib.Path(__file__).parent / 'data'

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