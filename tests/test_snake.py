from tocase.tocase import ToCase


def test_snake_should_snake_case_usual_strings():
    assert ToCase("snake case").snake() == "snake_case"
    assert ToCase("snakeCase").snake() == "snake_case"
    assert ToCase("SNAKEcase").snake() == "snake_case"
    assert ToCase("Snake_Case").snake() == "snake_case"
    assert ToCase("Snake$%Case").snake() == "snake_case"
    assert ToCase("Snake.Case").snake() == "snake_case"
    assert ToCase("SNAKE_CASE").snake() == "snake_case"
    assert ToCase("__snake_case__").snake() == "snake_case"
    assert ToCase("snake?case").snake() == "snake_case"
    assert ToCase("snake_case").snake() == "snake_case"
    assert ToCase("SNAKECase").snake() == "snakec_ase"


def test_snake_should_snake_case_usual_string_in_other_languages():
    # test the UTF-8 char for russian, french and greek. Feel free to test other languages
    assert ToCase("не волнуйтесь беспокойтесь").snake() == "не_волнуйтесь_беспокойтесь"
    assert ToCase("épicurien ambiguë").snake() == "épicurien_ambiguë"
    assert ToCase("Μου αρέσει το κοτόπουλο").snake() == "μου_αρέσει_το_κοτόπουλο"


def test_snake_should_return_single_letter():
    assert ToCase("s").snake() == "s"


def test_snake_should_return_string_if_only_special_chars():
    assert ToCase("£$%^&*()_-+=:;.,'@#~?").snake() == "£$%^&*()_-+=:;.,'@#~?"


def test_snake_should_return_empty_string():
    assert ToCase("").snake() == ""
