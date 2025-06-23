from your_module.logic import sample_function
import pandas as pd

if __name__ == '__main__':
    df = pd.DataFrame({'col': [1, 2, 3]})
    result = sample_function(df)
    print(result)
