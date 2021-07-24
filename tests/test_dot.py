from tocase.tocase import toCase


def test_dot_should_dot_case_usual_strings():
    assert toCase("dot case").dot() == "dot.case"
    assert toCase("dotCase").dot() == "dot.case"
    assert toCase("DOTcase").dot() == "dot.case"
    assert toCase("DOT_Case").dot() == "dot.case"
    assert toCase("Dot$%Case").dot() == "dot.case"
    assert toCase("Dot.Case").dot() == "dot.case"
    assert toCase("DOT_CASE").dot() == "dot.case"
    assert toCase("__dot_case__").dot() == "dot.case"
    assert toCase("dot?case").dot() == "dot.case"
    assert toCase("dot_case").dot() == "dot.case"
    assert toCase("DOTCase").dot() == "dotc.ase"


def test_dot_should_dot_case_usual_string_in_other_languages():
    # test the UTF-8 char for russian, french and greek. Feel free to test other languages
    assert toCase("не волнуйтесь беспокойтесь") == "не.волнуйтесь.беспокойтесь"
    assert toCase("épicurien ambiguë") == "épicurien.ambiguië"
    assert toCase("Μου αρέσει το κοτόπουλο") == "μου.αρέσει.το.κοτόπουλο"


def test_should_pascal_single_letter():
    assert toCase("h").dot() == "H"


def test_pascal_should_return_if_only_special_chars():
    assert toCase("£$%^&*()_-+=:;.,'@#~?").dot() == "£$%^&*()_-+=:;.,'@#~?"


def test_pascal_should_return_empty_string():
    assert toCase("").dot() == ""
