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
    #Creating trip_distance_dim table
    trip_distance_dim=pd.DataFrame()
    trip_distance_dim.reset_index
    trip_distance_dim['trip_distance']=Uber_data['trip_distance'].drop_duplicates().reset_index(drop=True)
    trip_distance_dim['trip_distance_id']=trip_distance_dim.index
    trip_distance_dim.insert(0,'trip_distance_id', trip_distance_dim.pop('trip_distance_id'))

    return trip_distance_dim


@test
def test_output(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    assert output is not None, 'The output is undefined'
