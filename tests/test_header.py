from tocase.tocase import toCase


def test_header_should_header_case_usual_strings():
    assert toCase("header case").header() == "Header-Case"
    assert toCase("headerCase").header() == "Header-Case"
    assert toCase("HEADERcase").header() == "Header-Case"
    assert toCase("HEADER_Case").header() == "Header-Case"
    assert toCase("Header$%Case").header() == "Header-Case"
    assert toCase("Header.Case").header() == "Header-Case"
    assert toCase("HEADER_CASE").header() == "Header-Case"
    assert toCase("__header_case__").header() == "Header-Case"
    assert toCase("header?case").header() == "Header-Case"
    assert toCase("header_case").header() == "Header-Case"
    assert toCase("HEADERCase").header() == "Headerc-Ase"


def test_header_should_header_case_usual_string_in_other_languages():
    # test the UTF-8 char for russian, french and greek. Feel free to test other languages
    assert toCase("не волнуйтесь беспокойтесь").header() == "Не-Волнуйтесь-Беспокойтесь"
    assert toCase("épicurien ambiguë").header() == "Épicurien-Ambiguë"
    assert toCase("Μου αρέσει το κοτόπουλο").header() == "Μου-Αρέσει-Το-Κοτόπουλο"


def test_header_should_header_case_single_letter():
    assert toCase("h").header() == "H"


def test_header_should_return_if_only_special_chars():
    assert toCase("£$%^&*()_-+=:;.,'@#~?").header() == "£$%^&*()_-+=:;.,'@#~?"


def test_header_should_return_empty_string():
    assert toCase("").header() == ""
