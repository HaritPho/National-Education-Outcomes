# National Education Outcomes (Kaggle)
import pandas as pd
import numpy as np
#Importing and Cleaning the Dataset
dataset = pd.read_csv("EdStatsData.csv")
dataset = dataset.iloc[:,0:53]
ArabDataset = dataset[dataset["Country Code"]=="ARB"]

#Importing Literacy Rates used as metric for education quality
###FIX###
literacy_rate = pd.read_csv("cross-country-literacy-rates.csv")
removeliteracylist = []
for country in set(literacy_rate["Entity"]):
    country_subsetindex = list(literacy_rate[literacy_rate["Entity"]==country].index)
    del country_subsetindex[-1]
    removeliteracylist.append(country_subsetindex)

cleanliteracyrate = literacy_rate.drop(literacy_rate.index[removeliteracylist])

#Simple Imputer
from sklearn.impute import SimpleImputer
imputer = SimpleImputer(missing_values = np.nan, strategy = 'constant', fill_value = "na")
imputer = imputer.fit(dataset.iloc[:,:])
dataset.iloc[:,:] = imputer.transform(dataset.iloc[:,:])

#Need to improve efficiency
removelinelist = []
for row in range(0,len(dataset)):
    value_check = False
    for column in range(4,53):
        if str(dataset.iloc[row][column])!="na":
            value_check= True
            break
    if value_check ==False:
        removelinelist.append(row)

cleandataset = dataset.drop(dataset.index[removelinelist])


#Process of arab dataset
from sklearn.impute import SimpleImputer
imputer = SimpleImputer(missing_values = np.nan, strategy = 'constant', fill_value = "na")
imputer = imputer.fit(ArabDataset.iloc[:,:])
ArabDataset.iloc[:,:] = imputer.transform(ArabDataset.iloc[:,:])

#Need to improve efficiency
removelinelist = []
for row in range(0,len(ArabDataset)):
    value_check = False
    for column in range(4,53):
        if str(ArabDataset.iloc[row][column])!="na":
            value_check= True
            break
    if value_check ==False:
        removelinelist.append(row)

cleanArabdataset = ArabDataset.drop(ArabDataset.index[removelinelist])

#Cutting Out data that lacks half the dataset
removelacking = []
for row1 in range(0,len(cleanArabdataset)):
    half_check =0
    for column1 in range(4,53):
        if str(cleanArabdataset.iloc[row1][column1])!="na":
            half_check = half_check+1
    if half_check<=25:
        removelacking.append(row1)

cleanArabdataset = cleanArabdataset.drop(cleanArabdataset.index[removelacking])

unique_countries = set(dataset["Country Name"])
    










