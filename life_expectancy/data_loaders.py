"""Module for loading data in different formats"""
import pathlib
from abc import ABC, abstractmethod
import pandas as pd

class DataLoader(ABC):
    """
    Define interface wich should be used by the different loader classes
    independent from the type of file
    """

    @staticmethod
    @abstractmethod
    def read_data(file_name: str, path: pathlib.Path):
        """
        Load data from file in path provided
        """

class DataLoaderTSV(DataLoader):
    """
    Load data from a TSV file
    """

    @staticmethod
    def read_data(
        file_name: str,
        path: pathlib.Path
    ) -> pd.DataFrame:
        """
        Load specified file as a pandas DataFrame from data directory
        :param file_name: Name of the file to be loaded in tsv format
        :param path_file: Path to the file

        :return: Pandas DataFrame with loaded data
        """

        return pd.read_table(path / file_name)

class DataLoaderComrpessed(DataLoader):
    """
    Load JSON data from a compressed file
    """

    @staticmethod
    def read_data(
        file_name: str,
        path: pathlib.Path
    ) -> pd.DataFrame:
        """
        Load specified file as a pandas DataFrame from data directory
        :param file_name: Name of the file to be loaded in json compressed format
        :param path_file: Path to the file

        :return: Pandas DataFrame with loaded data
        """

        return pd.read_json(path / file_name, compression='infer')
