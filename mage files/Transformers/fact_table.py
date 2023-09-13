if 'transformer' not in globals():
    from mage_ai.data_preparation.decorators import transformer
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


@transformer
def transform(datetime_dim, passenger_count_dim, trip_distance_dim, rate_code_dim, payment_type_dim, pick_up_location_dim, drop_off_location_dim, Uber_data, **kwargs):
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
    # Creating fact table
    import pandas as pd

    Uber_data['tpep_pickup_datetime'] = pd.to_datetime(Uber_data['tpep_pickup_datetime'])
    Uber_data['tpep_dropoff_datetime'] = pd.to_datetime(Uber_data['tpep_dropoff_datetime'])

    fact_table= Uber_data.merge(passenger_count_dim, left_on='passenger_count', right_on='passenger_count')\
    .merge(trip_distance_dim, left_on='trip_distance', right_on='trip_distance')\
    .merge(rate_code_dim, left_on='RatecodeID', right_on='RatecodeID')\
    .merge(payment_type_dim, left_on='payment_type', right_on='payment_type')\
    .merge(datetime_dim, left_on=['tpep_pickup_datetime','tpep_dropoff_datetime'], right_on=['tpep_pickup_datetime','tpep_dropoff_datetime'])\
    [['trip_id','VendorID', 'datetime_id', 'passenger_count_id', 'trip_distance_id', 'PULocationID', 'DOLocationID', 'rate_code_id','payment_type_id','fare_amount','extra','mta_tax','tip_amount','tolls_amount','improvement_surcharge','total_amount','congestion_surcharge','airport_fee']]

    return fact_table


@test
def test_output(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    assert output is not None, 'The output is undefined'
