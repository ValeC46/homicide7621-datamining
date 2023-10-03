# Homicide Reports 1976-2021
Analysis over a dataset with all the homicide reports made in between 1976 and 2021 in the United States

## Columns Details
This are the columns encased in the clean data file:<br/>
***City:*** name of the _city_ in which it happened<br/>
***State:*** name of the _state_ in which it happened<br/>
***Agency:*** type of agency that reported the case<br/>
***Solved:*** whether offender was identified or not<br/>
***Year:*** year in which the victim´s body was recovered<br/>
***Month:*** month in which the body was recovered<br/>
***Incident:*** number describing the case number within the month and agency<br/>
***Homicide:*** whether the report was _Murder or Non-negligent manslaughter_ or _Manslaughter by Negligence_ <br/>
***Situation:*** whether it had a single or multiple victims and whether it had single, multiple or unknown number of offenders<br/>
***VicAge:*** age of the victim<br/>
***VicSex:*** sex of the victim<br/>
***VicRace:*** race of the victim<br/>
***OffAge:*** age of the offender<br/>
***OffSex:*** sex of the offender<br/>
***OffRace:*** race of the offender<br/>
***Weapon:*** weapon used<br/>
***Relationship:*** relationship between the victim and offender<br/>
***Circumstance:*** the circumstance for the crime<br/>
***VicCount:*** number of additional victims<br/>
***OffCount:*** number of additional offenders<br/>
***Date:*** Date of when the body was recovered in _datetime_ format<br/>

## File Directory
Here is a brief description of what each file does and the order to run it:<br/>
1. ***dataprep.py:*** downloads the data from the web<br/>
2. ***datacleaning.py:*** cleans the _City_ column and creates a _Date_ column<br/>
3. ***descstats.py:*** creates files with the stats for both victim and offender age, as well as the count of type of murder and relationship between victim and offender<br/>
4. ***datavisualization.py:*** creates boxplot and pie charts for the results of the previous file<br/>
5. ***anova.py:*** check the variance in between the victim's age distributions as well as the offender's, can compare to the image created previously titled _boxplot\_State\_Off.png_ and _boxplot\_State.png_<br/>