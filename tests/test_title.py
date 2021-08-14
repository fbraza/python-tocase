from tocase.for_strings import ToCase
import tocase.for_pandas
import pandas as pd


def test_title_should_title_case_usual_strings():
    assert ToCase("title case").title() == "Title Case"
    assert ToCase("titleCase").title() == "Title Case"
    assert ToCase("TITLEcase").title() == "Title Case"
    assert ToCase("Title_Case").title() == "Title Case"
    assert ToCase("Title$%Case").title() == "Title Case"
    assert ToCase("Title.Case").title() == "Title Case"
    assert ToCase("TITLE_CASE").title() == "Title Case"
    assert ToCase("__title_case__").title() == "Title Case"
    assert ToCase("title?case").title() == "Title Case"
    assert ToCase("title_case").title() == "Title Case"
    assert ToCase("TITLECase").title() == "Titlec Ase"


def test_title_should_tile_case_usual_string_in_other_languages():
    # test the UTF-8 char for russian, french and greek.
    # Feel free to test other languages
    assert ToCase("не волнуйтесь беспокойтесь").title() == "Не Волнуйтесь Беспокойтесь" # noqa: 501
    assert ToCase("épicurien ambiguë").title() == "Épicurien Ambiguë"
    assert ToCase("Μου αρέσει το κοτόπουλο").title() == "Μου Αρέσει Το Κοτόπουλο" # noqa: 501


def test_title_should_return_single_letter():
    assert ToCase("t").title() == "T"


def test_title_should_return_string_if_only_special_chars():
    assert ToCase("£$%^&*()_-+=:;.,'@#~?").title() == "£$%^&*()_-+=:;.,'@#~?"


def test_title_should_return_empty_string():
    assert ToCase("").title() == ""


def test_title_pandas_accessor_should_title_case_all_columns_name(fake_data): # noqa: 501
    exp_cols = ["First Name", "Last Name", "Age", "Family Doctor"]
    res_cols = list(fake_data.col.title().columns)
    assert exp_cols == res_cols


def test_pandas_accessor_val_title_should_title_case_all_values_present_in_columns(fake_data): # noqa: 501
    columns = ["first name", "last name", "age", "family doctor"]
    values = [["Jules", "Otti", 35, "Dr James Porter"],
              ["Marie", "Curie", 22, "Dr Vicky Laporte"],
              ["Marc", "El Bichon", 35, "Dr Hyde Frank"]]
    exp_df = pd.DataFrame(data=values, columns=columns)
    res_df = fake_data.val.title([
        "first name",
        "last name",
        "family doctor"
        ])
    assert exp_df.equals(res_df)
