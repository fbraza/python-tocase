from tocase.tocase import toCase


def test_pascal_should_pascal_case_usual_strings():
    assert toCase("pascal case").pascal() == "PascalCase"
    assert toCase("pascalCase").pascal() == "PascalCase"
    assert toCase("PASCALcase").pascal() == "PascalCase"
    assert toCase("PASCAL_Case").pascal() == "PascalCase"
    assert toCase("Pascal$%Case").pascal() == "PascalCase"
    assert toCase("Pascal.Case").pascal() == "PascalCase"
    assert toCase("PASCAL_CASE").pascal() == "PascalCase"
    assert toCase("__pascal_case__").pascal() == "PascalCase"
    assert toCase("pascal?case").pascal() == "PascalCase"
    assert toCase("pascal_case").pascal() == "PascalCase"
    assert toCase("PASCALCase").pascal() == "PascalcAse"


def test_should_pascal_single_letter():
    assert toCase("p").pascal() == "P"


def test_pascal_should_return_if_only_special_chars():
    assert toCase("£$%^&*()_-+=:;.,'@#~?").pascal() == "£$%^&*()_-+=:;.,'@#~?"


def test_pascal_should_return_empty_string():
    assert toCase("").pascal() == ""
