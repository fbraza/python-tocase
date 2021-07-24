from typing import List
import regex


class toCase:
    def __init__(
        self,
        string: str,
        pattern: str = r"""
    /\p{Lu}{2,}(?=\p{Lu}\p{Ll}+[0-9]*|\b)|\p{Lu}?\p{Ll}+[0-9]*|\p{Lu}+|[0-9]+/
    """
    ) -> None:
        if not isinstance(string, str):
            raise TypeError(
                """
                Wrong type used. The toCase constructor accepts strings only
                """
                )
        self.__string: str = string
        self.__pattern: str = pattern
        self.__separators: dict[str, str] = {
            "pascal": "",
            "camel": "",
            "snake": "_",
            "title": " ",
            "kebab": "-",
            "dot": ".",
            "header": "-",
            "constant": "_"
        }

    @property
    def pattern(self) -> str:
        return self.__pattern

    @property
    def string(self) -> str:
        return self.__string

    @property
    def separators(self):
        return self.__separators

    def __convert(self, kind: str) -> str:
        sep: str = self.separators[kind]
        words: List[str] = regex.findall(self.pattern, self.string)
        size: int = len(words)
        converted: str = ""
        if size == 0:
            converted = self.string
        elif kind == "pascal" or kind == "title" or kind == "header":
            converted = sep.join([w.lower().capitalize() for w in words])
        elif kind == "snake" or kind == "kebab" or kind == "dot":
            converted = sep.join([w.lower() for w in words])
        elif kind == "camel":
            converted = sep.join([w.lower() if i == 0 else w.lower().capitalize() for i, w in enumerate(words)]) # noqa: 501
        elif kind == "constant":
            converted = sep.join([w.upper() for w in words])
        return converted

    def pascal(self) -> str:
        return self.__convert("pascal")

    def camel(self) -> str:
        return self.__convert("camel")

    def snake(self) -> str:
        return self.__convert("snake")

    def kebab(self) -> str:
        return self.__convert("kebab")

    def constant(self) -> str:
        return self.__convert("constant")

    def dot(self) -> str:
        return self.__convert("dot")

    def title(self) -> str:
        return self.__convert("title")

    def header(self) -> str:
        return self.__convert("header")
