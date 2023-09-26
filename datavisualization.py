import os
import pandas as pd
from matplotlib import pyplot as plt
import numpy as np

if not os.path.exists('img'):
    os.mkdir('img')

data = pd.read_csv('csv/cleandata.csv')

data.replace(999, np.NaN, inplace=True)

state_year_victim = data.groupby(['State', 'Year'])[['VicAge']].aggregate(pd.DataFrame.mean)
state_year_victim.boxplot(by = 'State', figsize=(32,32))
plt.xticks(rotation = 90)
plt.savefig("img/boxplot_State.png")
plt.close()

state_year_offender = data.groupby(['State', 'Year'])[['OffAge']].aggregate(pd.DataFrame.mean)
state_year_offender.boxplot(by = 'State', figsize=(32,32))
plt.xticks(rotation = 90)
plt.savefig("img/boxplot_State_Off.png")
plt.close()

state_homicide = pd.read_csv('csv/state_homicide.csv')
state_relationship = pd.read_csv('csv/state_relationship.csv')
state_homicide.set_index('Homicide', inplace=True)
state_relationship.set_index('Relationship', inplace=True)
# state_relationship[state_relationship['State'] == 'Colorado'].plot.pie(y='Incident', title='Colorado', figsize=(15,10))
# plt.savefig("img/strp_Colorado.png")
# state_homicide[state_homicide['State'] == 'Alaska'].plot.pie(y='Incident', title='Alaska')
# plt.savefig("img/sthm_Alaska.png")
for state in set(state_homicide["State"]):
    state_homicide[state_homicide['State'] == state].plot.pie(y='Incident', title=state)
    plt.savefig(f"img/sthm_{state}.png")
    state_relationship[state_relationship['State'] == state].plot.pie(y='Incident', title=state, figsize=(15,10))
    plt.savefig(f"img/strp{state}.png")
    plt.close()

plt.close()