from tocase.tocase import toCase


def test_title_should_title_case_usual_strings():
    assert toCase("snake case").title() == "Snake Case"
    assert toCase("snakeCase").title() == "Snake Case"
    assert toCase("SNAKEcase").title() == "Snake Case"
    assert toCase("Snake_Case").title() == "Snake Case"
    assert toCase("Snake$%Case").title() == "Snake Case"
    assert toCase("Snake.Case").title() == "Snake Case"
    assert toCase("SNAKE_CASE").title() == "Snake Case"
    assert toCase("__snake_case__").title() == "Snake Case"
    assert toCase("snake?case").title() == "Snake Case"
    assert toCase("snake_case").title() == "Snake Case"
    assert toCase("SNAKECase").title() == "Snakec Ase"


def test_title_should_return_single_letter():
    assert toCase("t").title() == "T"


def test_title_should_return_string_if_only_special_chars():
    assert toCase("£$%^&*()_-+=:;.,'@#~?").title() == "£$%^&*()_-+=:;.,'@#~?"


def test_title_should_return_empty_string():
    assert toCase("").title() == ""