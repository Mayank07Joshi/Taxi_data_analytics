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

    #Creating rate_code_dim table

    data={1:'Standard rate',
      2: 'JFK',
      3: 'Newark',
      4: 'Nassau or Westchester',
      5: 'Negotiated fare',
      6: 'Group ride'
     }
    rate_code_dim=pd.DataFrame()
    rate_code_dim['RatecodeID']=Uber_data['RatecodeID'].drop_duplicates().reset_index(drop=True)
    rate_code_dim['rate_code_name']=rate_code_dim['RatecodeID'].map(data)
    rate_code_dim['rate_code_id']=rate_code_dim.index
    rate_code_dim.insert(0, 'rate_code_id', rate_code_dim.pop('rate_code_id'))

    return rate_code_dim


@test
def test_output(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    assert output is not None, 'The output is undefined'
