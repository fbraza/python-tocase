"""
This module provides two pandas DataFrame accessors that can
leverage the ToCase methods to recase column names or column
values.
"""


from typing import Callable, List
import pandas as pd

from tocase.for_strings import ToCase


@pd.api.extensions.register_dataframe_accessor("col")
class RecaseColumnNamesAccessor:
    """A Pandas DataFrame accessor defined to recase columns names

    Attributes:
    -----------
    - __obj: The accessed pandas DataFrame
    - __todot: lambda function to dot case strings
    - __tokebab: lambda function to kebab case strings
    - __totitle: lambda function to title case strings
    - __tosnake: lambda function to snake case strings
    - __tocamel: lambda function to camel case strings
    - __topascal: lambda function to pascal case strings
    - __toheader: lambda function to header case strings
    - __toconstant: lambda function to constant case strings

    Methods:
    --------
    - dot(): method to recase DataFrame columns in dot case
    - camel(): method to recase DataFrame columns in camel case
    - kebab(): method to recase DataFrame columns in kebab case
    - snake(): method to recase DataFrame columns in snake case
    - title(): method to recase DataFrame columns in title case
    - pascal(): method to recase DataFrame columns in pascal case
    - header(): method to recase DataFrame columns in header case
    - constant(): method to recase DataFrame columns in constant case
    """

    # pylint: disable=too-many-instance-attributes
    # Nine is reasonable in this case.

    def __init__(self, pandas_obj):
        self.__obj = pandas_obj
        self.__todot = lambda x: ToCase(x).dot()
        self.__tokebab = lambda x: ToCase(x).kebab()
        self.__totitle = lambda x: ToCase(x).title()
        self.__tosnake = lambda x: ToCase(x).snake()
        self.__tocamel = lambda x: ToCase(x).camel()
        self.__topascal = lambda x: ToCase(x).pascal()
        self.__toheader = lambda x: ToCase(x).header()
        self.__toconstant = lambda x: ToCase(x).constant()

    def camel(self, inplace: bool = False) -> pd.DataFrame:
        """Method to camel case DataFrame columns

        Parameters:
        -----------
        inplace, bool: False by default. If True return a new DataFrame

        Return:
        -------
        pd.DataFrame, the DataFrame with recased columns name
        """
        return self.__obj.rename(columns=self.__tocamel, inplace=inplace)

    def dot(self, inplace: bool = False) -> pd.DataFrame:
        """Method to dot case DataFrame columns

        Parameters:
        -----------
        inplace, bool: False by default. If True return a new DataFrame

        Return:
        -------
        pd.DataFrame, the DataFrame with recased columns name
        """
        return self.__obj.rename(columns=self.__todot, inplace=inplace)

    def kebab(self, inplace: bool = False) -> pd.DataFrame:
        """Method to kebab case DataFrame columns

        Parameters:
        -----------
        inplace, bool: False by default. If True return a new DataFrame

        Return:
        -------
        pd.DataFrame, the DataFrame with recased columns name
        """
        return self.__obj.rename(columns=self.__tokebab, inplace=inplace)

    def snake(self, inplace: bool = False) -> pd.DataFrame:
        """Method to snake case DataFrame columns

        Parameters:
        -----------
        inplace, bool: False by default. If True return a new DataFrame

        Return:
        -------
        pd.DataFrame, the DataFrame with recased columns name
        """
        return self.__obj.rename(columns=self.__tosnake, inplace=inplace)

    def title(self, inplace: bool = False) -> pd.DataFrame:
        """Method to title case DataFrame columns

        Parameters:
        -----------
        inplace, bool: False by default. If True return a new DataFrame

        Return:
        -------
        pd.DataFrame, a new DataFrame with recased columns name
        """
        return self.__obj.rename(columns=self.__totitle, inplace=inplace)

    def pascal(self, inplace: bool = False) -> pd.DataFrame:
        """Method to pascal case DataFrame columns

        Parameters:
        -----------
        inplace, bool: False by default. If True return a new DataFrame

        Return:
        -------
        pd.DataFrame, a new DataFrame with recased columns name
        """
        return self.__obj.rename(columns=self.__topascal, inplace=inplace)

    def header(self, inplace: bool = False) -> pd.DataFrame:
        """Method to header case DataFrame columns

        Parameters:
        -----------
        inplace, bool: False by default. If True return a new DataFrame

        Return:
        -------
        pd.DataFrame, a new DataFrame with recased columns name
        """
        return self.__obj.rename(columns=self.__toheader, inplace=inplace)

    def constant(self, inplace: bool = False) -> pd.DataFrame:
        """Method to constant case DataFrame columns

        Parameters:
        -----------
        inplace, bool: False by default. If True return a new DataFrame

        Return:
        -------
        pd.DataFrame, a new DataFrame with recased columns name
        """
        return self.__obj.rename(columns=self.__toconstant, inplace=inplace)


@pd.api.extensions.register_dataframe_accessor("val")
class RecaseColumnValuesAccessor:
    """A Pandas DataFrame accessor defined to recase columns string values

    Attributes:
    -----------
    - __obj: The accessed pandas DataFrame
    - __todot: lambda function to dot case strings
    - __tokebab: lambda function to kebab case strings
    - __totitle: lambda function to title case strings
    - __tosnake: lambda function to snake case strings
    - __tocamel: lambda function to camel case strings
    - __topascal: lambda function to pascal case strings
    - __toheader: lambda function to header case strings
    - __toconstant: lambda function to constant case strings

    Methods:
    --------
    - __recase_values(): private static method that enpasulate the recasing logic # noqa: 501
    - dot(): method to recase DataFrame column values in dot case
    - camel(): method to recase DataFrame column values in camel case
    - kebab(): method to recase DataFrame column values in kebab case
    - snake(): method to recase DataFrame column values in snake case
    - title(): method to recase DataFrame column values in title case
    - pascal(): method to recase DataFrame column values in pascal case
    - header(): method to recase DataFrame column values in header case
    - constant(): method to recase DataFrame column values in constant case
    """

    # pylint: disable=too-many-instance-attributes
    # Nine is reasonable in this case.

    def __init__(self, pandas_obj):
        self.__obj = pandas_obj
        self.__todot = lambda x: ToCase(x).dot()
        self.__tokebab = lambda x: ToCase(x).kebab()
        self.__totitle = lambda x: ToCase(x).title()
        self.__tosnake = lambda x: ToCase(x).snake()
        self.__tocamel = lambda x: ToCase(x).camel()
        self.__topascal = lambda x: ToCase(x).pascal()
        self.__toheader = lambda x: ToCase(x).header()
        self.__toconstant = lambda x: ToCase(x).constant()

    @staticmethod
    def __recase_values(
        data: pd.DataFrame,
        columns: List[str],
        func: Callable,
    ) -> pd.DataFrame:
        df_copy = data.copy()
        for column in columns:
            if column not in data.columns:
                raise AttributeError(
                    "Column '{}' not present in DataFrame".format(column)
                )
        for column in columns:
            df_copy[column] = df_copy[column].apply(func)
        return df_copy

    def camel(self, columns: List[str]) -> pd.DataFrame:
        """Method to camel case DataFrame column values

        Parameters:
        -----------
        columns, List[str]: list of the columns to recase

        Return:
        -------
        pd.DataFrame, the DataFrame with recased columns values
        """
        return self.__recase_values(self.__obj, columns, self.__tocamel)

    def constant(self, columns: List[str]) -> pd.DataFrame:
        """Method to constant case DataFrame column values

        Parameters:
        -----------
        columns, List[str]: list of the columns to recase

        Return:
        -------
        pd.DataFrame, the DataFrame with recased columns values
        """
        return self.__recase_values(self.__obj, columns, self.__toconstant)

    def dot(self, columns: List[str]) -> pd.DataFrame:
        """Method to dot case DataFrame column values

        Parameters:
        -----------
        columns, List[str]: list of the columns to recase

        Return:
        -------
        pd.DataFrame, the DataFrame with recased columns values
        """
        return self.__recase_values(self.__obj, columns, self.__todot)

    def header(self, columns: List[str]) -> pd.DataFrame:
        """Method to header case DataFrame column values

        Parameters:
        -----------
        columns, List[str]: list of the columns to recase

        Return:
        -------
        pd.DataFrame, the DataFrame with recased columns values
        """
        return self.__recase_values(self.__obj, columns, self.__toheader)

    def kebab(self, columns: List[str]) -> pd.DataFrame:
        """Method to kebab case DataFrame column values

        Parameters:
        -----------
        columns, List[str]: list of the columns to recase

        Return:
        -------
        pd.DataFrame, the DataFrame with recased columns values
        """
        return self.__recase_values(self.__obj, columns, self.__tokebab)

    def pascal(self, columns: List[str]) -> pd.DataFrame:
        """Method to pascal case DataFrame column values

        Parameters:
        -----------
        columns, List[str]: list of the columns to recase

        Return:
        -------
        pd.DataFrame, the DataFrame with recased columns values
        """
        return self.__recase_values(self.__obj, columns, self.__topascal)

    def snake(self, columns: List[str]) -> pd.DataFrame:
        """Method to snake case DataFrame column values

        Parameters:
        -----------
        columns, List[str]: list of the columns to recase

        Return:
        -------
        pd.DataFrame, the DataFrame with recased columns values
        """
        return self.__recase_values(self.__obj, columns, self.__tosnake)

    def title(self, columns: List[str]) -> pd.DataFrame:
        """Method to title case DataFrame column values

        Parameters:
        -----------
        columns, List[str]: list of the columns to recase

        Return:
        -------
        pd.DataFrame, the DataFrame with recased columns values
        """
        return self.__recase_values(self.__obj, columns, self.__totitle)
