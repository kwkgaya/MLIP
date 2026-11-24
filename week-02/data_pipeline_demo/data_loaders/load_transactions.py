import os
import pandas as pd
from mage_ai.settings.repo import get_repo_path

if 'data_loader' not in globals():
    from mage_ai.data_preparation.decorators import data_loader
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


@data_loader
def load_data(*args, **kwargs):
    # data.csv lives in week-02/, one level above the Mage project folder
    path = os.path.join(get_repo_path(), '..', 'data.csv')
    return pd.read_csv(path)


@test
def test_output(output, *args) -> None:
    assert output is not None, 'The output is undefined'
    assert len(output) > 0, 'data.csv is empty'