"""
This module provides a class ToCase with a string recasing API.
You can recase any string into any case format from the following
list: camel, constant, dot, header, kebab, pascal, sanke and title
cases.
"""


from typing import List, Dict
import regex


class ToCase:
    """A class to hold data necessary for recasing strings

    Attributes:
    -----------
    - __string: the string to recase
    - __pattern: regex pattern to extract words and numbers
    - __separators: dict for separators used during recasing

    Methods:
    --------
    - pattern(): getter method for the __pattern attribute
    - string(): getter method for the __string attribute
    - separators(): getter method for the __separators attribute
    - __convert(): private method that holds logic to convert string in specified case
    - camel(): method to recase string in camel case
    - constant(): method to recase string in constant case
    - dot(): method to recase string in dot case
    - header(): method to recase string in header case
    - kebab(): method to recase string in kebab case
    - pascal(): method to recase string in pascal case
    - snake(): method to recase string in snake case
    - title(): method to recase string in title case
    """

    def __init__(
        self,
        string: str,
        pattern: str = r"""
    /\p{Lu}{2,}(?=\p{Lu}\p{Ll}+[0-9]*|\b)|\p{Lu}?\p{Ll}+[0-9]*|\p{Lu}+|[0-9]+/
    """,
    ) -> None:
        """
        Parameters:
        -----------
        - string: the string you want to recase
        - pattern: the regex pattern used to extract words and numbers

        Raises:
        -------
        TypeError if string is not of str type
        """
        if not isinstance(string, str):
            raise TypeError(
                """
                Wrong type used. The toCase constructor accepts strings only
                """
            )
        self.__string: str = string
        self.__pattern: str = pattern
        self.__separators: Dict[str, str] = {
            "pascal": "",
            "camel": "",
            "snake": "_",
            "title": " ",
            "kebab": "-",
            "dot": ".",
            "header": "-",
            "constant": "_",
        }

    @property
    def pattern(self) -> str:
        """Getter method for the __pattern attribute

        Returns:
        --------
        str, the regex pattern used to extract words and numbers
        """
        return self.__pattern

    @property
    def string(self) -> str:
        """Getter method for the __string attribute

        Returns:
        --------
        str, the string to recase
        """
        return self.__string

    @property
    def separators(self):
        """Getter method for the __separators attribute

        Returns:
        --------
        Dict[str, str], a dictionnary holding respective separators
        """
        return self.__separators

    def __convert(self, kind: str) -> str:
        """Private method to recase string into the expected case format

        Parameters:
        -----------
        kind: Case format you want the string to be converted into

        Return:
        -------
        str, the recased string
        """
        sep: str = self.separators[kind]
        words: List[str] = regex.findall(self.pattern, self.string)
        size: int = len(words)
        converted: str = ""
        if size == 0:
            converted = self.string
        elif kind in ("pascal", "title", "header"):
            converted = sep.join([w.lower().capitalize() for w in words])
        elif kind in ("snake", "kebab", "dot"):
            converted = sep.join([w.lower() for w in words])
        elif kind == "camel":
            converted = sep.join(
                [
                    w.lower() if i == 0 else w.lower().capitalize()
                    for i, w in enumerate(words)
                ]
            )
        elif kind == "constant":
            converted = sep.join([w.upper() for w in words])
        return converted

    def pascal(self) -> str:
        """Recase string into pascal case

        Return:
        -------
        str, the pascal cased string
        """
        return self.__convert("pascal")

    def camel(self) -> str:
        """Recase string into camel case

        Return:
        -------
        str, the camel cased string
        """
        return self.__convert("camel")

    def snake(self) -> str:
        """Recase string into snake case

        Return:
        -------
        str, the snake cased string
        """
        return self.__convert("snake")

    def kebab(self) -> str:
        """Recase string into kebab case

        Return:
        -------
        str, the kebab cased string
        """
        return self.__convert("kebab")

    def constant(self) -> str:
        """Recase string into constant case

        Return:
        -------
        str, the constant cased string
        """
        return self.__convert("constant")

    def dot(self) -> str:
        """Recase string into dot case

        Return:
        -------
        str, the dot cased string
        """
        return self.__convert("dot")

    def title(self) -> str:
        """Recase string into title case

        Return:
        -------
        str, the title cased string
        """
        return self.__convert("title")

    def header(self) -> str:
        """Recase string into header case

        Return:
        -------
        str, header cased string
        """
        return self.__convert("header")
