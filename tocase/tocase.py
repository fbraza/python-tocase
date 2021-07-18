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
        self.size = len(self.string)
        self.words = regex.findall(self.pattern, self.string)

    def pascal(self):
        size = len(self.words)
        if size == 0:
            return self.string
        else:
            return self.words if size == 0 else "".join([w.lower().capitalize()
                                                         for w in self.words])

    def camel(self):
        pass

    def snake(self):
        pass

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
