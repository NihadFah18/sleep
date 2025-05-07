import pandas as pd 
import os 
def save_data(fullname,age, genre , duree_som,niv_stress, trouble,bmi_cat):
    data={
        "fullname":[fullname],
        "age":[age],
        "genre":[genre],
        "duree_som":[duree_som],
        "niv_stress":[niv_stress],
        "trouble":[trouble],
        "bmi_cat":[bmi_cat],
    }
    df =pd.DataFrame(data)
    file_data="data_sommeil.csv"
    if os.path.exists(file_data):
        df.to_csv(file_data,mode='a',index=False,header=False)
    else:
        df.to_csv(file_data,index=False)
        
    return True