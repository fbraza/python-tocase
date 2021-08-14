from tocase.for_strings import ToCase
import tocase.for_pandas
import pandas as pd


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
    # test the UTF-8 char for russian, french and greek.
    # Feel free to test other languages
    assert ToCase("не волнуйтесь беспокойтесь").kebab() == "не-волнуйтесь-беспокойтесь" # noqa: 501
    assert ToCase("épicurien ambiguë").kebab() == "épicurien-ambiguë"
    assert ToCase("Μου αρέσει το κοτόπουλο").kebab() == "μου-αρέσει-το-κοτόπουλο"  # noqa: 501


def test_kebab_should_return_single_letter():
    assert ToCase("K").kebab() == "k"


def test_kebab_should_return_string_if_only_special_chars():
    assert ToCase("£$%^&*()_-+=:;.,'@#~?").kebab() == "£$%^&*()_-+=:;.,'@#~?"


def test_kebab_should_return_empty_string():
    assert ToCase("").kebab() == ""


def test_pandas_accessor_col_kebab_should_kebab_case_all_columns_name(fake_data): # noqa: 501
    exp_cols = ["first-name", "last-name", "age", "family-doctor"]
    res_cols = list(fake_data.col.kebab().columns)
    assert exp_cols == res_cols


def test_pandas_accessor_val_kebab_should_kebab_case_all_values_present_in_columns(fake_data): # noqa: 501
    columns = ["first name", "last name", "age", "family doctor"]
    values = [["jules", "otti", 35, "dr-james-porter"],
              ["marie", "curie", 22, "dr-vicky-laporte"],
              ["marc", "el-bichon", 35, "dr-hyde-frank"]]
    exp_df = pd.DataFrame(data=values, columns=columns)
    res_df = fake_data.val.kebab([
        "first name",
        "last name",
        "family doctor"
        ])
    assert exp_df.equals(res_df)
