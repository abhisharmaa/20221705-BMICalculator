import pandas as pd 
from pandas.testing import assert_frame_equal
import BMICalculator


def test_json_to_object_conversion():
    #Test data
    json_data = [{"Gender": "Male", "HeightCm": 171, "WeightKg": 96}]
    #Expected dataframe after calculation
    expected_df = pd.DataFrame({'Gender': 'Male', 'HeightCm': 171,'WeightKg':96,'BMI': 32.8,'Health_Risk':'Medium risk','BMI_CATEGORY':'Moderately obese'},index=[0])
    print(expected_df)
    df = pd.DataFrame.from_dict(json_data) 
    #Returned Dataframe  
    Actual_df = BMICalculator.calculate_BMI_RISK(df)
    print(Actual_df)   
    #Comparing two dataframes
    assert_frame_equal(Actual_df, expected_df)
    if  assert_frame_equal(Actual_df, expected_df) == None:
        print('Test Passed')
    else:
        print('Test Failed')        

test_json_to_object_conversion()    