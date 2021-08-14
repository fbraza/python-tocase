from tocase.for_strings import ToCase
import pandas as pd
import tocase.for_pandas


def test_camel_should_camel_case_usual_strings():
    assert ToCase("camel case").camel() == "camelCase"
    assert ToCase("camel-case").camel() == "camelCase"
    assert ToCase("camel_case").camel() == "camelCase"
    assert ToCase("CAMEL.CASE").camel() == "camelCase"
    assert ToCase("camelCase").camel() == "camelCase"
    assert ToCase("CamelCase").camel() == "camelCase"
    assert ToCase("CAMelCase").camel() == "camElCase"


def test_camel_should_camel_case_usual_string_in_other_languages():
    # first russian, then french and greek. Feel free to test other languages
    assert ToCase("не волнуйтесь беспокойтесь").camel() == "неВолнуйтесьБеспокойтесь"  # noqa: 501
    assert ToCase("épicurien ambiguë").camel() == "épicurienAmbiguë"
    assert ToCase("Μου αρέσει το κοτόπουλο").camel() == "μουΑρέσειΤοΚοτόπουλο"


def test_should_camelcase_single_letter():
    assert ToCase("C").camel() == "c"


def test_camel_should_return_input_if_input_has_only_special_chars():
    assert ToCase("£$%^&*()_-+=:;.,'@#~?").camel() == "£$%^&*()_-+=:;.,'@#~?"


def test_camel_should_return_empty_string():
    assert ToCase("").camel() == ""


def test_pandas_accessor_col_camel_should_camel_case_all_columns_name(fake_data): # noqa: 501
    exp_cols = ["firstName", "lastName", "age", "familyDoctor"]
    res_cols = list(fake_data.col.camel().columns)
    assert exp_cols == res_cols


def test_pandas_accessor_val_camel_should_camel_case_all_columns_name(fake_data): # noqa: 501
    columns = ["first name", "last name", "age", "family doctor"]
    values = [["jules", "otti", 35, "drJamesPorter"],
              ["marie", "curie", 22, "drVickyLaporte"],
              ["marc", "elBichon", 35, "drHydeFrank"]]
    exp_df = pd.DataFrame(data=values, columns=columns)
    res_df = fake_data.val.camel([
        "first name",
        "last name",
        "family doctor"
        ])
    assert exp_df.equals(res_df)
