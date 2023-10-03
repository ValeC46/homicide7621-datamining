import pandas as pd
import numpy as np
from statsmodels.formula.api import ols
import statsmodels.api as sm

data = pd.read_csv('csv/cleandata.csv')

data.replace(999, np.NaN, inplace=True)

#ANOVA Victim Age per State per Year
print('\nVictim Age per State per Year\n')
state_year_victim = data.groupby(['State', 'Year'])[['VicAge']].aggregate(pd.DataFrame.mean)
state_year_victim.reset_index(inplace=True)
aux = state_year_victim.drop(['Year'], axis=1)
modl = ols("VicAge ~ State", data=aux).fit()
anova1 = sm.stats.anova_lm(modl, typ=2)
if anova1["PR(>F)"][0] < 0.005 :
    print('Hay Diferencia entre las distribuciones!!\n')
    print(anova1)
else:
    print('No hay Diferencia!!\n')

#Louisiana v Missouri
print('\nLouisiana vs Missouri\n')
state_year_victim = data.groupby(['State', 'Year'])[['VicAge']].aggregate(pd.DataFrame.mean)
state_year_victim.reset_index(inplace=True)
aux = state_year_victim.drop(['Year'], axis=1)
aux = aux[(aux['State'] == 'Missouri') | (aux['State'] == 'Louisiana')]
modl = ols("VicAge ~ State", data=aux).fit()
anova1 = sm.stats.anova_lm(modl, typ=2)
if anova1["PR(>F)"][0] < 0.005 :
    print('Hay Diferencia entre las distribuciones!!\n')
    print(anova1)
else:
    print('No hay Diferencia!!\n')

#ANOVA Offender Age per State per Year
print('\nOffender Age per State per Year\n')
state_year_offender = data.groupby(['State', 'Year'])[['OffAge']].aggregate(pd.DataFrame.mean)
state_year_offender.reset_index(inplace=True)
aux = state_year_offender.drop(['Year'], axis=1)
modl = ols("OffAge ~ State", data=aux).fit()
anova3 = sm.stats.anova_lm(modl, typ=2)
if anova3["PR(>F)"][0] < 0.005 :
    print('Hay Diferencia entre las distribuciones!!\n')
    print(anova3)
else:
    print('No hay Diferencia!!\n')

#Michigan v Missouri
print('\nMichigan vs Missouri\n')
state_year_victim = data.groupby(['State', 'Year'])[['OffAge']].aggregate(pd.DataFrame.mean)
state_year_victim.reset_index(inplace=True)
aux = state_year_victim.drop(['Year'], axis=1)
aux = aux[(aux['State'] == 'Missouri') | (aux['State'] == 'Michigan')]
modl = ols("OffAge ~ State", data=aux).fit()
anova1 = sm.stats.anova_lm(modl, typ=2)
if anova1["PR(>F)"][0] < 0.005 :
    print('Hay Diferencia entre las distribuciones!!\n')
    print(anova1)
else:
    print('No hay Diferencia!!\n')
