from tocase.for_strings import ToCase
import tocase.for_pandas
import pandas as pd


def test_snake_should_snake_case_usual_strings():
    assert ToCase("snake case").snake() == "snake_case"
    assert ToCase("snakeCase").snake() == "snake_case"
    assert ToCase("SNAKEcase").snake() == "snake_case"
    assert ToCase("Snake_Case").snake() == "snake_case"
    assert ToCase("Snake$%Case").snake() == "snake_case"
    assert ToCase("Snake.Case").snake() == "snake_case"
    assert ToCase("SNAKE_CASE").snake() == "snake_case"
    assert ToCase("__snake_case__").snake() == "snake_case"
    assert ToCase("snake?case").snake() == "snake_case"
    assert ToCase("snake_case").snake() == "snake_case"
    assert ToCase("SNAKECase").snake() == "snakec_ase"


def test_snake_should_snake_case_usual_string_in_other_languages():
    # test the UTF-8 char for russian, french and greek.
    # Feel free to test other languages
    assert ToCase("не волнуйтесь беспокойтесь").snake() == "не_волнуйтесь_беспокойтесь" # noqa: 501
    assert ToCase("épicurien ambiguë").snake() == "épicurien_ambiguë"
    assert ToCase("Μου αρέσει το κοτόπουλο").snake() == "μου_αρέσει_το_κοτόπουλο"  # noqa: 501


def test_snake_should_return_single_letter():
    assert ToCase("s").snake() == "s"


def test_snake_should_return_string_if_only_special_chars():
    assert ToCase("£$%^&*()_-+=:;.,'@#~?").snake() == "£$%^&*()_-+=:;.,'@#~?"


def test_snake_should_return_empty_string():
    assert ToCase("").snake() == ""


def test_pandas_accessor_col_snake_should_camel_case_all_columns_name(fake_data): # noqa: 501
    exp_cols = ["first_name", "last_name", "age", "family_doctor"]
    res_cols = list(fake_data.col.snake().columns)
    assert exp_cols == res_cols


def test_pandas_accessor_val_snake_should_snake_case_all_values_present_in_columns(fake_data): # noqa: 501
    columns = ["first name", "last name", "age", "family doctor"]
    values = [["jules", "otti", 35, "dr_james_porter"],
              ["marie", "curie", 22, "dr_vicky_laporte"],
              ["marc", "el_bichon", 35, "dr_hyde_frank"]]
    exp_df = pd.DataFrame(data=values, columns=columns)
    res_df = fake_data.val.snake([
        "first name",
        "last name",
        "family doctor"
        ])
    assert exp_df.equals(res_df)
