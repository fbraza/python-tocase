from tocase.for_strings import ToCase
import tocase.for_pandas
import pandas as pd


def test_pascal_should_pascal_case_usual_strings():
    assert ToCase("pascal case").pascal() == "PascalCase"
    assert ToCase("pascalCase").pascal() == "PascalCase"
    assert ToCase("PASCALcase").pascal() == "PascalCase"
    assert ToCase("PASCAL_Case").pascal() == "PascalCase"
    assert ToCase("Pascal$%Case").pascal() == "PascalCase"
    assert ToCase("Pascal.Case").pascal() == "PascalCase"
    assert ToCase("PASCAL_CASE").pascal() == "PascalCase"
    assert ToCase("__pascal_case__").pascal() == "PascalCase"
    assert ToCase("pascal?case").pascal() == "PascalCase"
    assert ToCase("pascal_case").pascal() == "PascalCase"
    assert ToCase("PASCALCase").pascal() == "PascalcAse"


def test_pascal_should_pascal_case_usual_string_in_other_languages():
    # test the UTF-8 char for russian, french and greek.
    # Feel free to test other languages
    assert ToCase("не волнуйтесь беспокойтесь").pascal() == "НеВолнуйтесьБеспокойтесь" # noqa: 501
    assert ToCase("épicurien ambiguë").pascal() == "ÉpicurienAmbiguë"
    assert ToCase("Μου αρέσει το κοτόπουλο").pascal() == "ΜουΑρέσειΤοΚοτόπουλο"


def test_should_pascal_single_letter():
    assert ToCase("p").pascal() == "P"


def test_pascal_should_return_only_special_chars():
    assert ToCase("£$%^&*()_-+=:;.,'@#~?").pascal() == "£$%^&*()_-+=:;.,'@#~?"


def test_pascal_should_return_empty_string():
    assert ToCase("").pascal() == ""


def test_pandas_accessor_col_pascal_should_pascal_case_all_columns_name(fake_data): # noqa: 501
    exp_cols = ["FirstName", "LastName", "Age", "FamilyDoctor"]
    res_cols = list(fake_data.col.pascal().columns)
    assert exp_cols == res_cols


def test_pandas_accessor_val_pascal_should_pascal_case_all_values_present_in_columns(fake_data): # noqa: 501
    columns = ["first name", "last name", "age", "family doctor"]
    values = [["Jules", "Otti", 35, "DrJamesPorter"],
              ["Marie", "Curie", 22, "DrVickyLaporte"],
              ["Marc", "ElBichon", 35, "DrHydeFrank"]]
    exp_df = pd.DataFrame(data=values, columns=columns)
    res_df = fake_data.val.pascal([
        "first name",
        "last name",
        "family doctor"
        ])
    assert exp_df.equals(res_df)
