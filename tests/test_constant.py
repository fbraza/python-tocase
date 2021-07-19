from tocase.tocase import toCase


def test_constant_should_constant_case_usual_strings():
    assert toCase("constant case").constant() == "CONSTANT_CASE"
    assert toCase("constantCase").constant() == "CONSTANT_CASE"
    assert toCase("CONSTANTcase").constant() == "CONSTANT_CASE"
    assert toCase("Constant$%Case").constant() == "CONSTANT_CASE"
    assert toCase("Constant.Case").constant() == "CONSTANT_CASE"
    assert toCase("CONSTANT_CASE").constant() == "CONSTANT_CASE"
    assert toCase("__constant_case__").constant() == "CONSTANT_CASE"
    assert toCase("constant?case").constant() == "CONSTANT_CASE"
    assert toCase("constant_case").constant() == "CONSTANT_CASE"
    assert toCase("CONSTANTCase").constant() == "CONSTANTC_ASE"


def test_constant_should_return_single_letter():
    assert toCase("c").constant() == "C"


def test_constant_should_return_string_if_only_special_chars():
    assert toCase("£$%^&*()_-+=:;.,'@#~?").constant() == "£$%^&*()_-+=:;.,'@#~?" # noqa: 501 


def test_constant_should_return_empty_string():
    assert toCase("").constant() == ""
