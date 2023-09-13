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

    #Creating datetime_dim table
    Uber_data['tpep_pickup_datetime'] = pd.to_datetime(Uber_data['tpep_pickup_datetime'])
    Uber_data['tpep_dropoff_datetime'] = pd.to_datetime(Uber_data['tpep_dropoff_datetime'])

    datetime_dim = Uber_data[['tpep_pickup_datetime','tpep_dropoff_datetime']].drop_duplicates().reset_index(drop=True)

    #### Pickup ####
    datetime_dim['pick_up_hour']= datetime_dim['tpep_pickup_datetime'].dt.hour
    datetime_dim['pick_up_day']= datetime_dim['tpep_pickup_datetime'].dt.day
    datetime_dim['pick_up_month']= datetime_dim['tpep_pickup_datetime'].dt.month
    datetime_dim['pick_up_year']= datetime_dim['tpep_pickup_datetime'].dt.year
    datetime_dim['pick_up_weekday']= datetime_dim['tpep_pickup_datetime'].dt.weekday

    #### Drop-off ####
    datetime_dim['drop_off_hour']= datetime_dim['tpep_dropoff_datetime'].dt.hour
    datetime_dim['drop_off_day']= datetime_dim['tpep_dropoff_datetime'].dt.day
    datetime_dim['drop_off_month']= datetime_dim['tpep_dropoff_datetime'].dt.month
    datetime_dim['drop_off_year']= datetime_dim['tpep_dropoff_datetime'].dt.year
    datetime_dim['drop_off_weekday']= datetime_dim['tpep_dropoff_datetime'].dt.weekday

    datetime_dim['datetime_id']=datetime_dim.index
    datetime_dim.insert(0, 'datetime_id',datetime_dim.pop('datetime_id'))

    return datetime_dim


@test
def test_output(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    assert output is not None, 'The output is undefined'
