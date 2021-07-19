from tocase.tocase import toCase


def test_camel_should_camel_case_usual_strings():
    assert toCase("camel case").camel() == "camelCase"
    assert toCase("camel-case").camel() == "camelCase"
    assert toCase("camel_case").camel() == "camelCase"
    assert toCase("CAMEL.CASE").camel() == "camelCase"
    assert toCase("camelCase").camel() == "camelCase"
    assert toCase("CamelCase").camel() == "camelCase"
    assert toCase("CAMelCase").camel() == "camElCase"


def test_should_camel_single_letter():
    assert toCase("c").camel() == "c"


def test_camel_should_return_if_only_special_chars():
    assert toCase("£$%^&*()_-+=:;.,'@#~?").camel() == "£$%^&*()_-+=:;.,'@#~?"


def test_camel_should_return_empty_string():
    assert toCase("").camel() == ""
