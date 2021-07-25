from tocase.tocase import ToCase


def test_kebab_should_kebab_case_usual_strings():
    assert ToCase("kebab case").kebab() == "kebab-case"
    assert ToCase("kebabCase").kebab() == "kebab-case"
    assert ToCase("KEBABcase").kebab() == "kebab-case"
    assert ToCase("Kebab_Case").kebab() == "kebab-case"
    assert ToCase("Kebab$%Case").kebab() == "kebab-case"
    assert ToCase("Kebab.Case").kebab() == "kebab-case"
    assert ToCase("KEBAB_CASE").kebab() == "kebab-case"
    assert ToCase("__kebab_case__").kebab() == "kebab-case"
    assert ToCase("kebab?case").kebab() == "kebab-case"
    assert ToCase("kebab_case").kebab() == "kebab-case"
    assert ToCase("KEBABCase").kebab() == "kebabc-ase"


def test_kebab_should_kebab_case_usual_string_in_other_languages():
    # test the UTF-8 char for russian, french and greek. Feel free to test other languages
    assert ToCase("не волнуйтесь беспокойтесь").kebab() == "не-волнуйтесь-беспокойтесь"
    assert ToCase("épicurien ambiguë").kebab() == "épicurien-ambiguë"
    assert ToCase("Μου αρέσει το κοτόπουλο").kebab() == "μου-αρέσει-το-κοτόπουλο"


def test_kebab_should_return_single_letter():
    assert ToCase("K").kebab() == "k"


def test_kebab_should_return_string_if_only_special_chars():
    assert ToCase("£$%^&*()_-+=:;.,'@#~?").kebab() == "£$%^&*()_-+=:;.,'@#~?"


def test_kebab_should_return_empty_string():
    assert ToCase("").kebab() == ""
