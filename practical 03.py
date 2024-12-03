import os
import pandas as pd
InputFileName = r"F:\ADS\Practicals\Practicals\Practical 03\IP_DATA_ALL.csv"
OutputFileName = 'Retrieve_Router_Location.csv'
sFileName = r"F:\ADS\Practicals\Practicals\Practical 03\IP_DATA_ALL.csv"
print('Loading:', sFileName)
IP_DATA_ALL = pd.read_csv(sFileName, header=0, low_memory=False,
                          usecols=['Country', 'Place.Name', 'Latitude', 'Longitude'])
IP_DATA_ALL.rename(columns={'Place.Name': 'Place_Name'}, inplace=True)
sFileDir = r"F:\ADS\Practicals\Practicals\Practical 03"
if not os.path.exists(sFileDir):
    os.makedirs(sFileDir)
ROUTERLOC = IP_DATA_ALL.drop_duplicates(keep='first', inplace=False)
print('Rows:', ROUTERLOC.shape[0])
print('Columns:', ROUTERLOC.shape[1])
sFileName2 = os.path.join(sFileDir, OutputFileName)
ROUTERLOC.to_csv(sFileName2, index=False)
print('Done!')
