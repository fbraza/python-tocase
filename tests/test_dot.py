from tocase.tocase import ToCase


def test_dot_should_dot_case_usual_strings():
    assert ToCase("dot case").dot() == "dot.case"
    assert ToCase("dotCase").dot() == "dot.case"
    assert ToCase("DOTcase").dot() == "dot.case"
    assert ToCase("DOT_Case").dot() == "dot.case"
    assert ToCase("Dot$%Case").dot() == "dot.case"
    assert ToCase("Dot.Case").dot() == "dot.case"
    assert ToCase("DOT_CASE").dot() == "dot.case"
    assert ToCase("__dot_case__").dot() == "dot.case"
    assert ToCase("dot?case").dot() == "dot.case"
    assert ToCase("dot_case").dot() == "dot.case"
    assert ToCase("DOTCase").dot() == "dotc.ase"


def test_dot_should_dot_case_usual_string_in_other_languages():
    # test the UTF-8 char for russian, french and greek. Feel free to test other languages
    assert ToCase("не волнуйтесь беспокойтесь").dot() == "не.волнуйтесь.беспокойтесь"
    assert ToCase("épicurien ambiguë").dot() == "épicurien.ambiguë"
    assert ToCase("Μου αρέσει το κοτόπουλο").dot() == "μου.αρέσει.το.κοτόπουλο"


def test_should_dotcase_single_letter():
    assert ToCase("D").dot() == "d"


def test_dot_should_return_if_only_special_chars():
    assert ToCase("£$%^&*()_-+=:;.,'@#~?").dot() == "£$%^&*()_-+=:;.,'@#~?"


def test_dot_should_return_empty_string():
    assert ToCase("").dot() == ""
