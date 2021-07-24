from tocase.tocase import toCase


def test_snake_should_snake_case_usual_strings():
    assert toCase("snake case").snake() == "snake_case"
    assert toCase("snakeCase").snake() == "snake_case"
    assert toCase("SNAKEcase").snake() == "snake_case"
    assert toCase("Snake_Case").snake() == "snake_case"
    assert toCase("Snake$%Case").snake() == "snake_case"
    assert toCase("Snake.Case").snake() == "snake_case"
    assert toCase("SNAKE_CASE").snake() == "snake_case"
    assert toCase("__snake_case__").snake() == "snake_case"
    assert toCase("snake?case").snake() == "snake_case"
    assert toCase("snake_case").snake() == "snake_case"
    assert toCase("SNAKECase").snake() == "snakec_ase"


def test_snake_should_snake_case_usual_string_in_other_languages():
    # test the UTF-8 char for russian, french and greek. Feel free to test other languages
    assert toCase("не волнуйтесь беспокойтесь").snake() == "не_волнуйтесь_беспокойтесь"
    assert toCase("épicurien ambiguë").snake() == "épicurien_ambiguë"
    assert toCase("Μου αρέσει το κοτόπουλο").snake() == "μου_αρέσει_το_κοτόπουλο"


def test_snake_should_return_single_letter():
    assert toCase("s").snake() == "s"


def test_snake_should_return_string_if_only_special_chars():
    assert toCase("£$%^&*()_-+=:;.,'@#~?").snake() == "£$%^&*()_-+=:;.,'@#~?"


def test_snake_should_return_empty_string():
    assert toCase("").snake() == ""
