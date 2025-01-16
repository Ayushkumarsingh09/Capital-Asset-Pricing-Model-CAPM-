import pytest
import pandas as pd
from src.data_preparation import DataPreparation

def test_load_data():
    data = DataPreparation.load_data("tests/test_data.csv")
    assert not data.empty

def test_validate_data():
    data = pd.DataFrame({"A": [1, 2, 3], "B": [4, 5, None]})
    with pytest.raises(ValueError):
        DataPreparation.validate_data(data)
