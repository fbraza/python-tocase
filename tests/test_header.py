from tocase.for_strings import ToCase
import tocase.for_pandas
import pandas as pd


def test_header_should_header_case_usual_strings():
    assert ToCase("header case").header() == "Header-Case"
    assert ToCase("headerCase").header() == "Header-Case"
    assert ToCase("HEADERcase").header() == "Header-Case"
    assert ToCase("HEADER_Case").header() == "Header-Case"
    assert ToCase("Header$%Case").header() == "Header-Case"
    assert ToCase("Header.Case").header() == "Header-Case"
    assert ToCase("HEADER_CASE").header() == "Header-Case"
    assert ToCase("__header_case__").header() == "Header-Case"
    assert ToCase("header?case").header() == "Header-Case"
    assert ToCase("header_case").header() == "Header-Case"
    assert ToCase("HEADERCase").header() == "Headerc-Ase"


def test_header_should_header_case_usual_string_in_other_languages():
    # test the UTF-8 char for russian, french and greek.
    # Feel free to test other languages
    assert ToCase("не волнуйтесь беспокойтесь").header() == "Не-Волнуйтесь-Беспокойтесь"  # noqa: 501
    assert ToCase("épicurien ambiguë").header() == "Épicurien-Ambiguë"
    assert ToCase("Μου αρέσει το κοτόπουλο").header() == "Μου-Αρέσει-Το-Κοτόπουλο"  # noqa: 501


def test_header_should_header_case_single_letter():
    assert ToCase("h").header() == "H"


def test_header_should_return_if_only_special_chars():
    assert ToCase("£$%^&*()_-+=:;.,'@#~?").header() == "£$%^&*()_-+=:;.,'@#~?"


def test_header_should_return_empty_string():
    assert ToCase("").header() == ""


def test_pandas_accessor_col_header_should_header_case_all_columns_name(fake_data): # noqa: 501
    exp_cols = ["First-Name", "Last-Name", "Age", "Family-Doctor"]
    res_cols = list(fake_data.col.header().columns)
    assert exp_cols == res_cols


def test_pandas_accessor_val_header_should_header_case_all_values_present_in_columns(fake_data): # noqa: 501
    columns = ["first name", "last name", "age", "family doctor"]
    values = [["Jules", "Otti", 35, "Dr-James-Porter"],
              ["Marie", "Curie", 22, "Dr-Vicky-Laporte"],
              ["Marc", "El-Bichon", 35, "Dr-Hyde-Frank"]]
    exp_df = pd.DataFrame(data=values, columns=columns)
    res_df = fake_data.val.header([
        "first name",
        "last name",
        "family doctor"
        ])
    assert exp_df.equals(res_df)
