import pandas as pd

data = pd.read_csv("ECA_kommun_tmean_w41.csv", index_col="kommun")
names = pd.read_csv("kommun_names.csv", sep=';', index_col="id")
names = names.sort_index()

data[['tmean']] = data[['tmean']].apply(lambda x: x/10)
data[['tmax']] = data[['tmax']].apply(lambda x: x/10)
data[['tmin']] = data[['tmin']].apply(lambda x: x/10)

#print(data.head())
#print(data.describe())
#data.info()
#print(data.index)

#How was the weather in Stockholm?

#si = names[names['label'] == 'Stockholm'].index.item()
si = names[names['label'] == 'Stockholm'].index[0]

#print(data.loc[si])
#print(si)
#Which kommun was the coldest and the warmest?

#print(data[data['tmin'] == data['tmin'].min()])
#print(data[data['tmax'] == data['tmax'].max()])

mi = data[data['tmin'] == data['tmin'].min()].index[0]
mm = data[data['tmax'] == data['tmax'].max()].index[0]

#print(names.loc[mi])

#print("The coldest place in Sweden was", names.loc[mi].item())
#print("The warmest place in Sweden was", names.loc[mm].item())

#Explore the built in funcionality of pandas with the following questions:
#Find the 10 most humid kommuner. Print their names.
#Find the kommun with the median humidity. The list all kommuner with humidity lesser than the median.

data_hum = data.sort_values(by='humidity', ascending=False)
data_hum2 = data_hum.head(10)
#print(data_hum2)
#for i in range(10):
#    print(names.loc[data_hum2.index[i]].item())
#for row_index in data_hum2.index:
#    print(names.loc[row_index].item())

median = data_hum['humidity'].median()
#print(median)

mid = len(data_hum) // 2
#print(data_hum.iloc[mid:])

for i, row in data_hum.iloc[mid:].iterrows():
    print(names.loc[i].item() + " " + str(row['humidity']))



