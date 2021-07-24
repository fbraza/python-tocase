from tocase.tocase import toCase


def test_kebab_should_kebab_case_usual_strings():
    assert toCase("kebab case").kebab() == "kebab-case"
    assert toCase("kebabCase").kebab() == "kebab-case"
    assert toCase("KEBABcase").kebab() == "kebab-case"
    assert toCase("Kebab_Case").kebab() == "kebab-case"
    assert toCase("Kebab$%Case").kebab() == "kebab-case"
    assert toCase("Kebab.Case").kebab() == "kebab-case"
    assert toCase("KEBAB_CASE").kebab() == "kebab-case"
    assert toCase("__kebab_case__").kebab() == "kebab-case"
    assert toCase("kebab?case").kebab() == "kebab-case"
    assert toCase("kebab_case").kebab() == "kebab-case"
    assert toCase("KEBABCase").kebab() == "kebabc-ase"


def test_kebab_should_kebab_case_usual_string_in_other_languages():
    # test the UTF-8 char for russian, french and greek. Feel free to test other languages
    assert toCase("не волнуйтесь беспокойтесь").kebab() == "не-волнуйтесь-беспокойтесь"
    assert toCase("épicurien ambiguë").kebab() == "épicurien-ambiguë"
    assert toCase("Μου αρέσει το κοτόπουλο").kebab() == "μου-αρέσει-το-κοτόπουλο"


def test_kebab_should_return_single_letter():
    assert toCase("K").kebab() == "k"


def test_kebab_should_return_string_if_only_special_chars():
    assert toCase("£$%^&*()_-+=:;.,'@#~?").kebab() == "£$%^&*()_-+=:;.,'@#~?"


def test_kebab_should_return_empty_string():
    assert toCase("").kebab() == ""
