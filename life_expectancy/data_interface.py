"""Module for loading data in different formats"""
import pathlib
import re
from abc import ABC, abstractmethod
import pandas as pd
from . import cleaning

class DataLoader(ABC):
    """
    Define interface wich should be used by the different loader classes
    independent from the type of file
    """

    @staticmethod
    @abstractmethod
    def read_data(file_name: str, path: pathlib.Path):
        """Load data from file in path provided"""

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

        data_raw = pd.read_table(path / file_name)

        tabular_data = cleaning.transform_data_into_tabular(data_raw)
        cleaned_data = cleaning.extract_floats(tabular_data)

        return cleaned_data

class DataLoaderCompressed(DataLoader):
    """Load JSON data from a compressed file"""

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

        data_raw: pd.DataFrame = pd.read_json(path / file_name, compression='infer')
        data_raw = data_raw.drop(columns=['flag', 'flag_detail'])

        return data_raw

class  DataInterface():
    """Interface to rewrite the necessary data from raw files to a processed one"""

    def __init__(
        self,
        file_name: str,
        path: pathlib.Path
    ) -> None:
        """
        Define the name of the file and the path to it
        :param file_name: The name of the file with the data to load
        :param path: The path where the data is, by default is folder named data
        in current path

        :return: None
        """

        self._file_name = file_name
        self._path = path
        self._file_extension = re.search("\.(.*)", self._file_name)[0]

    def _check_file_extension(
        self
    ) -> DataLoader:
        """Return the correct DataLoader according to file extension"""

        if self._file_extension == '.tsv':
            return DataLoaderTSV()
        if self._file_extension == '.zip':
            return DataLoaderCompressed()

        raise ValueError('File extension not valid!')

    def load_data(
        self
    ) -> pd.DataFrame:
        """Load the file identified"""

        data_loader = self._check_file_extension()
        self.data: pd.DataFrame = data_loader.read_data(self._file_name, self._path)

        # Rename the column with region data
        self.data = self.data.rename(columns={self.data.columns[3]: 'region'})

    def filter_data(
        self,
        region: str
    ) ->pd.DataFrame:
        """Filter DataFrame by region"""

        self.data = self.data[self.data['region']==region]
