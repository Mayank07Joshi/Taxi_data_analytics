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
    #Creating passenger_count_dim table
    passenger_count_dim=pd.DataFrame()
    passenger_count_dim.reset_index
    passenger_count_dim['passenger_count']=Uber_data['passenger_count'].drop_duplicates().reset_index(drop=True)
    passenger_count_dim['passenger_count_id']=passenger_count_dim.index
    passenger_count_dim.insert(0, 'passenger_count_id', passenger_count_dim.pop('passenger_count_id'))

    return passenger_count_dim


@test
def test_output(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    assert output is not None, 'The output is undefined'
