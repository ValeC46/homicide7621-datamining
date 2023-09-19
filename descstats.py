import pandas as pd
import numpy as np

data = pd.read_csv('csv/cleandata.csv')

data.replace(999, np.NaN, inplace=True)

#Analysis of Victim's Age per Year per State
state_year = data.groupby(['State', 'Year']).agg({'VicAge': ['count', 'mean', 'min', 'max']})
state_year.reset_index(inplace=True)
print(state_year.head())
state_year.to_csv('csv/state_year_victim', index=False)

#Analysis of Offender's Age per Year per State
state_year_off = data.groupby(['State', 'Year']).agg({'OffAge': ['count', 'mean', 'min', 'max']})
state_year_off.reset_index(inplace=True)
print(state_year_off.head())
state_year_off.to_csv('csv/state_year_offender', index=False)

#Analysis of Victim's Age per Date per State
state_date = data.groupby(['State', 'Date']).agg({'VicAge': ['count', 'mean', 'min', 'max']})
state_date.reset_index(inplace=True)
print(state_date.head())
state_date.to_csv('csv/state_date_victim', index=False)

#Analysis of Offender's Age per Date per State
state_date_off = data.groupby(['State', 'Date']).agg({'OffAge': ['count', 'mean', 'min', 'max']})
state_date_off.reset_index(inplace=True)
print(state_date_off.head())
state_date_off.to_csv('csv/state_date_offender', index=False)