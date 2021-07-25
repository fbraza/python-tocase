from tocase.tocase import ToCase


def test_pascal_should_pascal_case_usual_strings():
    assert ToCase("pascal case").pascal() == "PascalCase"
    assert ToCase("pascalCase").pascal() == "PascalCase"
    assert ToCase("PASCALcase").pascal() == "PascalCase"
    assert ToCase("PASCAL_Case").pascal() == "PascalCase"
    assert ToCase("Pascal$%Case").pascal() == "PascalCase"
    assert ToCase("Pascal.Case").pascal() == "PascalCase"
    assert ToCase("PASCAL_CASE").pascal() == "PascalCase"
    assert ToCase("__pascal_case__").pascal() == "PascalCase"
    assert ToCase("pascal?case").pascal() == "PascalCase"
    assert ToCase("pascal_case").pascal() == "PascalCase"
    assert ToCase("PASCALCase").pascal() == "PascalcAse"


def test_pascal_should_pascal_case_usual_string_in_other_languages():
    # test the UTF-8 char for russian, french and greek. Feel free to test other languages
    assert ToCase("не волнуйтесь беспокойтесь").pascal() == "НеВолнуйтесьБеспокойтесь"
    assert ToCase("épicurien ambiguë").pascal() == "ÉpicurienAmbiguë"
    assert ToCase("Μου αρέσει το κοτόπουλο").pascal() == "ΜουΑρέσειΤοΚοτόπουλο"


def test_should_pascal_single_letter():
    assert ToCase("p").pascal() == "P"


def test_pascal_should_return_only_special_chars():
    assert ToCase("£$%^&*()_-+=:;.,'@#~?").pascal() == "£$%^&*()_-+=:;.,'@#~?"


def test_pascal_should_return_empty_string():
    assert ToCase("").pascal() == ""
