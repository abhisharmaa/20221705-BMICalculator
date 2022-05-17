import pandas as pd 
from pandas.testing import assert_frame_equal
import BMICalculator


def test_json_to_object_conversion():
    json_data = [{"Gender": "Male", "HeightCm": 171, "WeightKg": 96}]
    bmi = round(96 / 1.71, 3)
    health_risk = 'Medium risk'
    bmi_category = 'Moderately obese'
    expected_df = pd.DataFrame({'Gender': 'Male', 'HeightCm': 171,'WeightKg':96,'BMI': 32.8,'Health_Risk':'Medium risk','BMI_CATEGORY':'Moderately obese'},index=[0])
    print(expected_df)
    df = pd.DataFrame.from_dict(json_data)
    #df = pd.DataFrame(list(json_data.items()),columns = ['Gender','HeightCm','WeightKg'])
    #df = pd.read_json(json_data)
    
    Actual_df = BMICalculator.calculate_BMI_RISK(df)
    print(Actual_df)
   
    # if pd.testing.assert_frame_equal(Actual_df, expected_df):
    #     print('Test Passed')
    # else:
    #     print('Test Failed')    
    assert_frame_equal(Actual_df, expected_df)
    if  assert_frame_equal(Actual_df, expected_df) == None:
        print('Test Passed')
    else:
        print('Test Failed')        
    
    #assert BMICalculator.calculate_BMI_RISK(df)['BMI'] == bmi
    #assert assert_df[assert_df['Health_Risk'] == health_risk]
    # assert main_oops.create_people_health_list(dictionary)[0].bmi_category == bmi_category

test_json_to_object_conversion()    