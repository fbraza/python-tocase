import pytest
import pandas as pd


@pytest.fixture
def fake_data():
    columns = ["first name", "last name", "age", "family doctor"]
    values = [["Jules", "Otti", 35, "Dr James Porter"],
              ["Marie", "Curie", 22, "Dr Vicky Laporte"],
              ["Marc", "El Bichon", 35, "Dr Hyde Frank"]]
    return pd.DataFrame(data=values, columns=columns)
