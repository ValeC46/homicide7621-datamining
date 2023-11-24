import matplotlib.pyplot as plt
import statsmodels.api as sm
import numbers
import pandas as pd
import numpy as np
import seaborn as sn

def transform_variable(df: pd.DataFrame, x:str):
    if isinstance(df[x][0], numbers.Number):
        return df[x]
    else:
        return pd.Series([i for i in range(0, len(df[x]))])

def linear_regression(df: pd.DataFrame, x:str, y: str):
    fixed_x = transform_variable(df, x)
    model= sm.OLS(df[y],sm.add_constant(fixed_x)).fit()
    print(model.summary())

    coef = pd.read_html(model.summary().tables[1].as_html(),header=0,index_col=0)[0]['coef']
    df.plot(x=x,y=y, kind='scatter')
    plt.plot(df[x],[pd.DataFrame.mean(df[y]) for _ in fixed_x.items()], color='gold')
    plt.plot(df[x],[ coef.values[1] * x + coef.values[0] for _, x in fixed_x.items()], color='red')
    plt.xticks(rotation=90)
    plt.savefig(f'img/lr_{y}_{x}.png')
    plt.close()

data = pd.read_csv('csv/cleandata.csv')

cleandata = data.replace(999, np.NaN)

#Linear Regression for Victim Age
vicage_lin = cleandata.groupby("Year")[['VicAge']].aggregate(pd.DataFrame.mean)
vicage_lin.reset_index(inplace=True)
linear_regression(vicage_lin, "Year", "VicAge")

#Linear Regression for Offender Age
offage_lin = cleandata.groupby("Year")[['OffAge']].aggregate(pd.DataFrame.mean)
offage_lin.reset_index(inplace=True)
linear_regression(offage_lin, "Year", "OffAge")

#Correlacion
data.drop(columns=['Agency', 'Solved', 'Month', 'Situation', 'Circumstance', 'Date'], inplace=True)
data['Relationship']=data['Relationship'].astype('category').cat.codes
data['Weapon']=data['Weapon'].astype('category').cat.codes
data['City']=data['City'].astype('category').cat.codes
data['State']=data['State'].astype('category').cat.codes
data['VicRace']=data['VicRace'].astype('category').cat.codes
data['OffRace']=data['OffRace'].astype('category').cat.codes
data['VicSex']=data['VicSex'].astype('category').cat.codes
data['OffSex']=data['OffSex'].astype('category').cat.codes
data['Homicide']=data['Homicide'].astype('category').cat.codes
correlation = data.corr()
print(correlation)

f = plt.figure(figsize=(10, 10))
# plt.matshow(correlation)
# plt.xticks(labels=correlation.columns, fontsize=14, rotation=90)
# plt.yticks(labels=correlation.columns,fontsize=14)
# cb = plt.colorbar()
# cb.ax.tick_params(labelsize=14)
# plt.title('Correlation Matrix', fontsize=16)
# plt.savefig('img/Correlation.png')

sn.heatmap(correlation, cmap="Reds", square=True, linewidths=.5, cbar_kws={"shrink": .5}, annot=True, fmt=".2f")
plt.savefig('img/correlation.png')

correlation.to_csv('csv/Correlation.csv', index=False)
