import regex
from dataclasses import dataclass


# /\p{Lu}{2,}(?=\p{Lu}\p{Ll}+[0-9]*|\b)|\p{Lu}?\p{Ll}+[0-9]*|\p{Lu}+|[0-9]+/


@dataclass
class toCase:
    string: str
    pattern: str = r"""
    /\p{Lu}{2,}(?=\p{Lu}\p{Ll}+[0-9]*|\b)|\p{Lu}?\p{Ll}+[0-9]*|\p{Lu}+|[0-9]+/
    """

    def __post_init__(self):
        self.words = regex.findall(self.pattern, self.string)
        self.size = len(self.words)
        self.separators: dict[str, str] = {
            "pascal": "",
            "camel": "",
            "snake": "_",
            "title": " ",
            "kebab": "-",
            "dot": ".",
            "header": "-"
        }

    def __convert(self, kind: str = "pascal"):
        sep: str = self.separators[kind]
        if self.size == 0:
            return self.string
        elif kind == "pascal" or kind == "title" or kind == "header":
            return sep.join([w.lower().capitalize() for w in self.words])
        elif kind == "snake" or kind == "kebab" or "kind" == "dot":
            return sep.join([w.lower() for w in self.words])
        elif kind == "camel":
            return sep.join([w.lower() if i == 0 else w.lower().capitalize() for i, w in enumerate(self.words)]) # noqa: 501

    def pascal(self):
        return self.__convert("pascal")

    def camel(self):
        return self.__convert("camel")

    def snake(self):
        return self.__convert("snake")

    def kebab(self):
        pass

    def constant(self):
        pass

    def dot(self):
        pass

    def title(self):
        pass

    def header(self):
        pass
