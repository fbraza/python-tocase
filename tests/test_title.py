from tocase.tocase import ToCase


def test_title_should_title_case_usual_strings():
    assert ToCase("snake case").title() == "Snake Case"
    assert ToCase("snakeCase").title() == "Snake Case"
    assert ToCase("SNAKEcase").title() == "Snake Case"
    assert ToCase("Snake_Case").title() == "Snake Case"
    assert ToCase("Snake$%Case").title() == "Snake Case"
    assert ToCase("Snake.Case").title() == "Snake Case"
    assert ToCase("SNAKE_CASE").title() == "Snake Case"
    assert ToCase("__snake_case__").title() == "Snake Case"
    assert ToCase("snake?case").title() == "Snake Case"
    assert ToCase("snake_case").title() == "Snake Case"
    assert ToCase("SNAKECase").title() == "Snakec Ase"


def test_title_should_tile_case_usual_string_in_other_languages():
    # test the UTF-8 char for russian, french and greek. Feel free to test other languages
    assert ToCase("не волнуйтесь беспокойтесь").title() == "Не Волнуйтесь Беспокойтесь"
    assert ToCase("épicurien ambiguë").title() == "Épicurien Ambiguë"
    assert ToCase("Μου αρέσει το κοτόπουλο").title() == "Μου Αρέσει Το Κοτόπουλο"


def test_title_should_return_single_letter():
    assert ToCase("t").title() == "T"


def test_title_should_return_string_if_only_special_chars():
    assert ToCase("£$%^&*()_-+=:;.,'@#~?").title() == "£$%^&*()_-+=:;.,'@#~?"


def test_title_should_return_empty_string():
    assert ToCase("").title() == ""
