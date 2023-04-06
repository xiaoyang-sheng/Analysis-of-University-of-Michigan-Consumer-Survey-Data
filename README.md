# Analysis-of-University-of-Michigan-Consumer-Survey-Data
Project of STATS 507: Data Science and Analytics using Python

## Group 9 Members:
Xiaoyang Sheng, Zihan Ye, Songwen Chen, Kejia Jin, Anqi Sun, Peter Hevrdejs, Jeffrey Hatch

## Summary:
We try to find the relation between the United States GDP quartely increase rate and the consumer survey data, and come up with a regression model.
Through the EDA analysis, we select 13 significant variables from the survey data, including BUS5, NEWS1, UNEMP, PX1Q1, NUMKID, EGRADE, HOM, CAR, INCOME, VEHNUM, PSSA, PCRY, GAS1. 

Based on these variables, we trained and fitted three machine learning models, which are ridge regression, random forest and xgboost. For all the three models, we used validation method to come up with the best model parameters under the smaller validation MSE. Then we compared the performance of the three models, and Xgboost did the best. 

Therefore, we use the trained Xgboost to predict the future responses using the simulated future survey data. The simulation is based on the assumption and the change rate of each survey data variables follow a normal distribution, and by calculating the mean and standard deviation from historical survey data, we are able to come up with future simulation of them. Upon these simulation results, we can use Xgboost to get the prediction of US GDP increase rate in future certain quarters. By default, the maximum of future quarters is 12, which means the largest year and quarter is ' 20261', first quarter in 2026.


## Data source:
Surveys of Consumers - University of Michigan:
https://data.sca.isr.umich.edu/survey-info.php

## Dash plot:
The analysis dashboard uses Plotly Dash on Google App Engine, and could be accessed by：
https://stats-507-375117.wn.r.appspot.com
(probably go expire now)

## Quick Start
```shell
python Dashbaord_setup/main.py
```
