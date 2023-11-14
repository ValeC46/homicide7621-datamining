import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
from scipy.stats import mode

def monthtonum(month):
    s = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
    return s.index(month) + 1

def scatter_group_by(file_path, df, x_column, y_column, label_column):
    fig, ax = plt.subplots(figsize=(20,10))
    labels = pd.unique(df[label_column])
    cmap = ['red', 'gold', 'darkmagenta', 'blue']
    for i, label in enumerate(labels):
        filter_df = df.query(f"{label_column} == '{label}'")
        ax.scatter(filter_df[x_column], filter_df[y_column], label=label, color=cmap[i])
    ax.legend()
    plt.xticks(rotation=90)
    plt.savefig(file_path)
    plt.close()

def euclidean_distance(p_1: np.array, p_2: np.array) -> float:
    return np.sqrt(np.sum((p_2 - p_1) ** 2))


def k_nearest_neightbors(points, labels, input_data, k):
    input_distances = [
        [euclidean_distance(input_point, point) for point in points]
        for input_point in input_data
    ]
    points_k_nearest = [
        np.argsort(input_point_dist)[:k] for input_point_dist in input_distances
    ]
    return [
        mode([labels[index] for index in point_nearest])
        for point_nearest in points_k_nearest
    ]

pd.options.mode.chained_assignment = None

data = pd.read_csv('csv/cleandata.csv')

cleandata = data.replace(999, np.NaN)

vicage_date = cleandata.groupby(['Date', 'Year', 'Month'])[['VicAge']].aggregate(pd.DataFrame.mean)
vicage_date.reset_index(inplace=True)
for x in vicage_date.index:
    vicage_date['Date'][x] = (vicage_date['Year'][x] * 10000) + (monthtonum(vicage_date['Month'][x]) * 100) + 1
vicage_date['ClassYear'] = 'Temp'
vicage_date['ClassSeason'] = 'Temp'

# print(vicage_date.info(), vicage_date.head())

for ind in vicage_date.index:
    if vicage_date['Year'][ind] in range(1965, 1981):
        vicage_date['ClassYear'][ind] = 'Gen X'
    elif vicage_date['Year'][ind] in range(1981, 1997):
        vicage_date['ClassYear'][ind] = 'Millenials'
    elif vicage_date['Year'][ind] in range(1997, 2013):
        vicage_date['ClassYear'][ind] = 'Gen Z'
    elif vicage_date['Year'][ind] in range(2013, 2022):
        vicage_date['ClassYear'][ind] = 'Gen Alpha'

for i in vicage_date.index:
    if vicage_date['Month'][i] in ['March', 'April', 'May']:
        vicage_date['ClassSeason'][i] = 'Spring'
    elif vicage_date['Month'][i] in ['June', 'July', 'August']:
        vicage_date['ClassSeason'][i] = 'Summer'
    elif vicage_date['Month'][i] in ['September', 'October', 'November']:
        vicage_date['ClassSeason'][i] = 'Autumn'
    elif vicage_date['Month'][i] in ['December', 'January', 'February']:
        vicage_date['ClassSeason'][i] = 'Winter'

# print(vicage_date.info(), vicage_date.tail())

scatter_group_by('img/classYear', vicage_date, 'Date', 'VicAge', 'ClassYear')
scatter_group_by('img/classSeason', vicage_date, 'Date', 'VicAge', 'ClassSeason')

vicage_date.drop(columns=['Year', 'Month'], inplace=True)

# print(vicage_date.info())

list_t = [
    (np.array(tuples[0:1]), tuples[2])
    for tuples in vicage_date.itertuples(index=False, name=None)
]
# print(list_t)
points = [point for point, _ in list_t]
labels = [label for _, label in list_t]

kn = k_nearest_neightbors(points, labels,
    [np.array(['20190201', 35]), np.array(['19800401', 32]), np.array(['19970401', 30])],
    5
)
print(kn)