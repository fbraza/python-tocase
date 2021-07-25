from tocase.tocase import ToCase


def test_header_should_header_case_usual_strings():
    assert ToCase("header case").header() == "Header-Case"
    assert ToCase("headerCase").header() == "Header-Case"
    assert ToCase("HEADERcase").header() == "Header-Case"
    assert ToCase("HEADER_Case").header() == "Header-Case"
    assert ToCase("Header$%Case").header() == "Header-Case"
    assert ToCase("Header.Case").header() == "Header-Case"
    assert ToCase("HEADER_CASE").header() == "Header-Case"
    assert ToCase("__header_case__").header() == "Header-Case"
    assert ToCase("header?case").header() == "Header-Case"
    assert ToCase("header_case").header() == "Header-Case"
    assert ToCase("HEADERCase").header() == "Headerc-Ase"


def test_header_should_header_case_usual_string_in_other_languages():
    # test the UTF-8 char for russian, french and greek. Feel free to test other languages
    assert ToCase("не волнуйтесь беспокойтесь").header() == "Не-Волнуйтесь-Беспокойтесь"
    assert ToCase("épicurien ambiguë").header() == "Épicurien-Ambiguë"
    assert ToCase("Μου αρέσει το κοτόπουλο").header() == "Μου-Αρέσει-Το-Κοτόπουλο"


def test_header_should_header_case_single_letter():
    assert ToCase("h").header() == "H"


def test_header_should_return_if_only_special_chars():
    assert ToCase("£$%^&*()_-+=:;.,'@#~?").header() == "£$%^&*()_-+=:;.,'@#~?"


def test_header_should_return_empty_string():
    assert ToCase("").header() == ""
