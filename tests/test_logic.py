from src.your_module.logic import sample_function
import pandas as pd

def test_sample_function():
    df = pd.DataFrame({'col': [1, 2]})
    result = sample_function(df)
    assert result.equals(df)
