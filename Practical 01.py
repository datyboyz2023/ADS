import pandas as pd
sInputFileName = r"C:\Users\Cnx2\OneDrive\Desktop\ADS\prac1.csv"
InputData = pd.read_csv(sInputFileName, encoding="latin-1")
print(InputData, "\n\n\n\n------- -")
ProcessData = InputData
ProcessData.drop('ISO-2-CODE', axis=1, inplace=True)
ProcessData.drop('ISO-3-Code', axis=1, inplace=True)
ProcessData.rename(columns={'Country': 'CountryName'}, inplace=True)
ProcessData.rename(columns={'ISO-M49': 'CountryNumber'}, inplace=True)
ProcessData.set_index('CountryNumber', inplace=True)
ProcessData.sort_values('CountryNumber', axis=0, ascending=False, inplace=True)
print(ProcessData)
OutputData = ProcessData
sOutputFileName = r"C:\Users\Cnx2\OneDrive\Desktop\ADS\practical1.csv"
OutputData.to_csv(sOutputFileName, index=False)
print('CSV TO HORUS - Done')
