from tocase.tocase import ToCase


def test_constant_should_constant_case_usual_strings():
    assert ToCase("constant case").constant() == "CONSTANT_CASE"
    assert ToCase("constantCase").constant() == "CONSTANT_CASE"
    assert ToCase("CONSTANTcase").constant() == "CONSTANT_CASE"
    assert ToCase("Constant$%Case").constant() == "CONSTANT_CASE"
    assert ToCase("Constant.Case").constant() == "CONSTANT_CASE"
    assert ToCase("CONSTANT_CASE").constant() == "CONSTANT_CASE"
    assert ToCase("__constant_case__").constant() == "CONSTANT_CASE"
    assert ToCase("constant?case").constant() == "CONSTANT_CASE"
    assert ToCase("constant_case").constant() == "CONSTANT_CASE"
    assert ToCase("CONSTANTCase").constant() == "CONSTANTC_ASE"


def test_constant_should_constant_case_usual_string_in_other_languages():
    # test the UTF-8 char for russian, french and greek. Feel free to test other languages
    assert ToCase("не волнуйтесь беспокойтесь").constant() == "НЕ_ВОЛНУЙТЕСЬ_БЕСПОКОЙТЕСЬ"
    assert ToCase("épicurien ambiguë").constant() == "ÉPICURIEN_AMBIGUË"
    assert ToCase("Μου αρέσει το κοτόπουλο").constant() == "ΜΟΥ_ΑΡΈΣΕΙ_ΤΟ_ΚΟΤΌΠΟΥΛΟ"


def test_constant_should_return_single_letter():
    assert ToCase("c").constant() == "C"


def test_constant_should_return_string_if_only_special_chars():
    assert ToCase("£$%^&*()_-+=:;.,'@#~?").constant() == "£$%^&*()_-+=:;.,'@#~?" # noqa: 501 


def test_constant_should_return_empty_string():
    assert ToCase("").constant() == ""
