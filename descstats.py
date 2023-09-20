import pandas as pd
import numpy as np

data = pd.read_csv('csv/cleandata.csv')

data.replace(999, np.NaN, inplace=True)

#Analysis of Victim's Age per Year per State
state_year = data.groupby(['State', 'Year']).agg({'VicAge': ['count', 'mean', 'min', 'max'], 'Incident': 'count'})
state_year.reset_index(inplace=True)
state_year = state_year.set_axis(['State', 'Year', 'VicAge_Count', 'VicAge_Mean', 'VicAge_Min', 'VicAge_Max', 'Incidents'], axis=1)
state_year['N/A Age'] = state_year['Incidents'] - state_year['VicAge_Count']
print(state_year.head())
state_year.to_csv('csv/state_year_victim.csv', index=False)

#Analysis of Offender's Age per Year per State
state_year_off = data.groupby(['State', 'Year']).agg({'OffAge': ['count', 'mean', 'min', 'max'], 'Incident': 'count'})
state_year_off.reset_index(inplace=True)
state_year_off = state_year_off.set_axis(['State', 'Year', 'OffAge_Count', 'OffAge_Mean', 'OffAge_Min', 'OffAge_Max', 'Incidents'], axis=1)
state_year_off['N/A Age'] = state_year_off['Incidents'] - state_year_off['OffAge_Count']
print(state_year_off.head())
state_year_off.to_csv('csv/state_year_offender.csv', index=False)

#Analysis of Victim's Age per Date per State
# state_date = data.groupby(['State', 'Date']).agg({'VicAge': ['count', 'mean', 'min', 'max'], 'Incident': 'count'})
# state_date.reset_index(inplace=True)
# state_date = state_date.set_axis(['State', 'Date', 'VicAge_Count', 'VicAge_Mean', 'VicAge_Min', 'VicAge_Max', 'Incidents'], axis=1)
# state_date['N/A Age'] = state_date['Incidents'] - state_date['VicAge_Count']
# print(state_date.head())
# state_date.to_csv('csv/state_date_victim.csv', index=False)

#Analysis of Offender's Age per Date per State
# state_date_off = data.groupby(['State', 'Date']).agg({'OffAge': ['count', 'mean', 'min', 'max'], 'Incident': 'count'})
# state_date_off.reset_index(inplace=True)
# state_date_off = state_date_off.set_axis(['State', 'Date', 'OffAge_Count', 'OffAge_Mean', 'OffAge_Min', 'OffAge_Max', 'Incidents'], axis=1)
# state_date_off['N/A Age'] = state_date_off['Incidents'] - state_date_off['OffAge_Count']
# print(state_date_off.head())
# state_date_off.to_csv('csv/state_date_offender.csv', index=False)

#Analysis of type of murder per state
state_homicide = data.groupby(['State', 'Homicide']).agg({'Incident': 'count'})
state_homicide.reset_index(inplace=True)
print(state_homicide.head())
state_homicide.to_csv('csv/state_homicide.csv', index=False)

#Analysis of relationship between offender ansd victim per state
state_relationship = data.groupby(['State', 'Relationship']).agg({'Incident': 'count'})
state_relationship.reset_index(inplace=True)
print(state_relationship.head())
state_relationship.to_csv('csv/state_relationship.csv', index=False)