import pandas as pd

names = pd.read_csv("kommun_names.csv", sep=';', index_col="id")
names = names.sort_index()

data = []

for i in range(41, 51):
    filename = "ECA_kommun_tmean_w" + str(i) + ".csv"
    df = pd.read_csv(filename, index_col="kommun")
    df[['tmean']] = df[['tmean']].apply(lambda x: x / 10)
    df[['tmax']] = df[['tmax']].apply(lambda x: x / 10)
    df[['tmin']] = df[['tmin']].apply(lambda x: x / 10)
    data.append(df)

#Which kommun saw the largest difference in mean temperatures during the period?

names['temprange'] = 0.0
names['tmmin'] = 0.0
names['tmmax'] = 0.0


for i, _ in names.iterrows():
    names.loc[i, ['tmmin']] = data[0].loc[i, ['tmean']].item()
    names.loc[i, ['tmmax']] = data[0].loc[i, ['tmean']].item()
    for d in data:
        if d.loc[i, ['tmean']].item() < names.loc[i, ['tmmin']].item():
            names.loc[i, ['tmmin']] = d.loc[i, ['tmean']].item()
        if d.loc[i, ['tmean']].item() > names.loc[i, ['tmmax']].item():
            names.loc[i, ['tmmax']] = d.loc[i, ['tmean']].item()
    names.loc[i, ['temprange']] = names.loc[i, ['tmmax']].item() - names.loc[i, ['tmmin']].item()


names_s = names.sort_values(by='temprange', ascending=False)

print(names_s)
