if 'transformer' not in globals():
    from mage_ai.data_preparation.decorators import transformer
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


@transformer
def transform(Uber_data, *args, **kwargs):
    """
    Template code for a transformer block.

    Add more parameters to this function if this block has multiple parent blocks.
    There should be one parameter for each output variable from each parent block.

    Args:
        data: The output from the upstream parent block
        args: The output from any additional upstream blocks (if applicable)

    Returns:
        Anything (e.g. data frame, dictionary, array, int, str, etc.)
    """
    import pandas as pd

    #Creating payment_type_dim table
    data={1:'Credit card',
      2: 'Cash',
      3: 'No charge',
      4: 'Dispute',
      5: 'Unknown',
      6: 'Voided trip'
     }
    payment_type_dim = pd.DataFrame()
    payment_type_dim['payment_type'] = Uber_data['payment_type'].drop_duplicates().reset_index(drop=True)
    payment_type_dim['payment_type_name']=payment_type_dim['payment_type'].map(data)

    payment_type_dim['payment_type_id']=payment_type_dim.index
    payment_type_dim.insert(0, 'payment_type_id', payment_type_dim.pop('payment_type_id'))

    return payment_type_dim


@test
def test_output(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    assert output is not None, 'The output is undefined'
