from tocase.for_strings import ToCase
import tocase.for_pandas
import pandas as pd


def test_dot_should_dot_case_usual_strings():
    assert ToCase("dot case").dot() == "dot.case"
    assert ToCase("dotCase").dot() == "dot.case"
    assert ToCase("DOTcase").dot() == "dot.case"
    assert ToCase("DOT_Case").dot() == "dot.case"
    assert ToCase("Dot$%Case").dot() == "dot.case"
    assert ToCase("Dot.Case").dot() == "dot.case"
    assert ToCase("DOT_CASE").dot() == "dot.case"
    assert ToCase("__dot_case__").dot() == "dot.case"
    assert ToCase("dot?case").dot() == "dot.case"
    assert ToCase("dot_case").dot() == "dot.case"
    assert ToCase("DOTCase").dot() == "dotc.ase"


def test_dot_should_dot_case_usual_string_in_other_languages():
    # test the UTF-8 char for russian, french and greek.
    # Feel free to test other languages
    assert ToCase("не волнуйтесь беспокойтесь").dot() == "не.волнуйтесь.беспокойтесь" # noqa: 501
    assert ToCase("épicurien ambiguë").dot() == "épicurien.ambiguë"
    assert ToCase("Μου αρέσει το κοτόπουλο").dot() == "μου.αρέσει.το.κοτόπουλο"


def test_should_dotcase_single_letter():
    assert ToCase("D").dot() == "d"


def test_dot_should_return_if_only_special_chars():
    assert ToCase("£$%^&*()_-+=:;.,'@#~?").dot() == "£$%^&*()_-+=:;.,'@#~?"


def test_dot_should_return_empty_string():
    assert ToCase("").dot() == ""


def test_pandas_accessor_col_dot_should_dot_case_all_columns_name(fake_data): # noqa: 501
    exp_cols = ["first.name", "last.name", "age", "family.doctor"]
    res_cols = list(fake_data.col.dot().columns)
    assert exp_cols == res_cols


def test_pandas_accessor_val_dot_should_dot_case_all_values_present_in_columns(fake_data): # noqa: 501
    columns = ["first name", "last name", "age", "family doctor"]
    values = [["jules", "otti", 35, "dr.james.porter"],
              ["marie", "curie", 22, "dr.vicky.laporte"],
              ["marc", "el.bichon", 35, "dr.hyde.frank"]]
    exp_df = pd.DataFrame(data=values, columns=columns)
    res_df = fake_data.val.dot([
        "first name",
        "last name",
        "family doctor"
        ])
    assert exp_df.equals(res_df)
