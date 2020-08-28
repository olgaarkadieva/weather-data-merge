
import datetime
import os
import os.path
import numpy as np
import pandas as pd

datadir = "./data/"  # data dorectory path 


input_column_names = ["unit","date","rawtime","wind_speed_avg_mps","wind_direction_avg_deg",
    "wind_direction_stddev_deg","wind_speed_peak_mps","temperature_C",
    "relative_humidity","pressure_mbar","battery_V","zero"]


output_column_names = ["temperature_C","pressure_mbar","relative_humidity",
    "wind_speed_avg_mps","wind_speed_peak_mps",
    "wind_direction_avg_deg","wind_direction_stddev_deg"]

# read and merge
dfs = []  # empty list to store data file one by one
for name in sorted(os.listdir(datadir)):  # read files in sorted fashion 
    filename = os.path.join(datadir, name)  # it will return filename as ./data/filename.txt
    print(f"reading {filename}")  # console file name 
    df = pd.read_csv(filename, names=input_column_names, index_col=False, comment='#') # read the content of file 
    dfs.append(df) # add file to list 
df = pd.concat(dfs)
df.drop_duplicates(inplace=True) # remove duplicates
del(dfs) # remove list content after loop finishes 

# create datetime index
df["datetime"] = pd.to_datetime(df['date'] +' '+ df['rawtime'], format="%y/%m/%d %H:%M:%S", utc=True)
df.set_index("datetime", inplace=True)

print(df)


print("Checking unit colums")

print(type(df['unit']))


print(df['unit'])


for column in output_column_names:
    print(df[column].dtype)
    assert df[column].dtype in [np.int64, object , np.float64] # check column type 

# write output file
filename = "ccat_site_weather_data_2006_to_2014.csv"
print(f"writing {filename}")

df.to_csv(filename, columns=output_column_names) # creating csv file with output column name list 

