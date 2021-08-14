from tocase.for_strings import ToCase
import tocase.for_pandas
import pandas as pd


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
    # test the UTF-8 char for russian, french and greek.
    # Feel free to test other languages
    assert ToCase("не волнуйтесь беспокойтесь").constant() == "НЕ_ВОЛНУЙТЕСЬ_БЕСПОКОЙТЕСЬ" # noqa: 501
    assert ToCase("épicurien ambiguë").constant() == "ÉPICURIEN_AMBIGUË"
    assert ToCase("Μου αρέσει το κοτόπουλο").constant() == "ΜΟΥ_ΑΡΈΣΕΙ_ΤΟ_ΚΟΤΌΠΟΥΛΟ" # noqa: 501


def test_constant_should_return_single_letter():
    assert ToCase("c").constant() == "C"


def test_constant_should_return_string_if_only_special_chars():
    assert ToCase("£$%^&*()_-+=:;.,'@#~?").constant() == "£$%^&*()_-+=:;.,'@#~?" # noqa: 501


def test_constant_should_return_empty_string():
    assert ToCase("").constant() == ""


def test_pandas_accessor_col_constant_should_constant_case_all_columns_name(fake_data): # noqa: 501
    exp_cols = ["FIRST_NAME", "LAST_NAME", "AGE", "FAMILY_DOCTOR"]
    res_cols = list(fake_data.col.constant().columns)
    assert exp_cols == res_cols


def test_pandas_accessor_val_constant_should_constant_case_all_values_present_in_columns(fake_data): # noqa: 501
    columns = ["first name", "last name", "age", "family doctor"]
    values = [["JULES", "OTTI", 35, "DR_JAMES_PORTER"],
              ["MARIE", "CURIE", 22, "DR_VICKY_LAPORTE"],
              ["MARC", "EL_BICHON", 35, "DR_HYDE_FRANK"]]
    exp_df = pd.DataFrame(data=values, columns=columns)
    res_df = fake_data.val.constant([
        "first name",
        "last name",
        "family doctor"
        ])
    assert exp_df.equals(res_df)
