if 'transformer' not in globals():
    from mage_ai.data_preparation.decorators import transformer
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


@transformer
def transform(data, *args, **kwargs):
    # Keep only the two input features
    df = data[['amount', 'is_new_recipient']].copy()
    # Flag large payments (1 = amount over 150)
    df['is_large_amount'] = (df['amount'] > 150).astype(int)
    return df


@test
def test_output(output, *args) -> None:
    assert list(output.columns) == ['amount', 'is_new_recipient', 'is_large_amount']