from tocase.tocase import ToCase


def test_camel_should_camel_case_usual_strings():
    assert ToCase("camel case").camel() == "camelCase"
    assert ToCase("camel-case").camel() == "camelCase"
    assert ToCase("camel_case").camel() =="camelCase"
    assert ToCase("CAMEL.CASE").camel() == "camelCase"
    assert ToCase("camelCase").camel() == "camelCase"
    assert ToCase("CamelCase").camel() == "camelCase"
    assert ToCase("CAMelCase").camel() == "camElCase"


def test_camel_should_camel_case_usual_string_in_other_languages():
    # first russian, then french and greek. Feel free to test other languages
    assert ToCase("не волнуйтесь беспокойтесь").camel() == "неВолнуйтесьБеспокойтесь"
    assert ToCase("épicurien ambiguë").camel() == "épicurienAmbiguë"
    assert ToCase("Μου αρέσει το κοτόπουλο").camel() == "μουΑρέσειΤοΚοτόπουλο"


def test_should_camel_single_letter():
    assert ToCase("c").camel() == "c"


def test_camel_should_return_if_only_special_chars():
    assert ToCase("£$%^&*()_-+=:;.,'@#~?").camel() == "£$%^&*()_-+=:;.,'@#~?"


def test_camel_should_return_empty_string():
    assert ToCase("").camel() == ""
