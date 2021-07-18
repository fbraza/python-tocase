from tocase.tocase import toCase


# tests for pascal()
def test_pascal_should_pascal_case_usual_strings():
    assert toCase("pascal case").pascal() == "PascalCase"
    assert toCase("pascal-case").pascal() == "PascalCase"
    assert toCase("pascal_case").pascal() == "PascalCase"
    assert toCase("PASCAL.CASE").pascal() == "PascalCase"
    assert toCase("pascalCase").pascal() == "PascalCase"
    assert toCase("PascalCase").pascal() == "PascalCase"


def test_should_pascal_single_letter():
    assert toCase("p").pascal() == "P"


def test_pascal_should_return_if_only_special_chars():
    assert toCase("£$%^&*()_-+=:;.,'@#~?").pascal() == "£$%^&*()_-+=:;.,'@#~?"


def test_pascal_should_return_empty_string():
    assert toCase("").pascal() == ""


# tests for camel()
def test_camel_should_camel_case_usual_strings():
    assert toCase("camel case").camel() == "camelCase"
    assert toCase("camel-case").camel() == "camelCase"
    assert toCase("camel_case").camel() == "camelCase"
    assert toCase("CAMEL.CASE").camel() == "camelCase"
    assert toCase("camelCase").camel() == "camelCase"
    assert toCase("CamelCase").camel() == "camelCase"
    assert toCase("CAMelCase").camel() == "camElCase"


def test_should_camel_single_letter():
    assert toCase("c").camel() == "c"


def test_camel_should_return_if_only_special_chars():
    assert toCase("£$%^&*()_-+=:;.,'@#~?").camel() == "£$%^&*()_-+=:;.,'@#~?"


def test_camel_should_return_empty_string():
    assert toCase("").camel() == ""
