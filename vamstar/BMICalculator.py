import pandas as pd
import numpy as np


def calculate_BMI_RISK(df):
    df['Heightmeter']=df.HeightCm/100
    df['BMI']=df.WeightKg/(df.Heightmeter*df.Heightmeter)
    df['BMI']=df.BMI.round(decimals=1)
    #print(df.dtypes)
    #df['BMI'] = df['BMI']
    conditions = [ (df['BMI']  <= 18.4),
    (df['BMI']  >= 18.5) & (df['BMI'] <= 24.9),
    (df['BMI'] >= 25.0) & (df['BMI'] <= 29.9),
    (df['BMI'] >= 30.0) & (df['BMI'] <= 34.9),
    (df['BMI'] >= 35.0) & (df['BMI'] <= 39.9),
    (df['BMI'] >= 40.0) ]
    BMI_CATEGORY  = ['Underweight', 'Normal weight', 'Overweight', 'Moderately obese','Severely obese','Very severely obese']
    Health_risk = ['Malnutrition risk', 'Low risk', 'Enhanced risk', 'Medium risk','High risk','Very High risk']
    df['Health_Risk'] = np.select(conditions, Health_risk)
    df['BMI_CATEGORY'] =  np.select(conditions, BMI_CATEGORY)
    df.drop('Heightmeter', axis=1, inplace=True)
    ## Count Number of Overweight People 
    

    #print(df)
    return df




    # x=df.merge(df_BMI_category, how='cross')
    # x=x[(x.BMI>=x.bmi_lower) & (x.BMI<=x.bmi_upper)]
    #return x[['Gender','HeightCm','WeightKg','BMI','bmi_category','health_risk']]

# This could read data in millions

if __name__ == "__main__":
    df= pd.read_json('customer.json')
    print(df)
    #df_BMI_category=pd.read_csv('config/BMI_category.csv')
    file_name='output/BMIofCustomers.csv'
    
    customer_health = calculate_BMI_RISK(df)
    cnts = customer_health[customer_health['BMI_CATEGORY'] == 'Overweight' ].shape[0]
    print('Total number of overweight customers = ' + str(cnts))
    
    #print(cnts)
    customer_health.to_csv(file_name,index=False)
   