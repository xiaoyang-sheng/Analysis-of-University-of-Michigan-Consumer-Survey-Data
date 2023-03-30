import dash
from dash import dcc
from dash import html
import plotly.express as px
import matplotlib.pyplot as plt
from scipy import stats
import numpy as np
import pandas as pd
import io
import matplotlib.pyplot as plt
import base64
import seaborn as sns
from dash.dependencies import Input, Output


app = dash.Dash(__name__)
server = app.server

# see https://plotly.com/python/px-arguments/ for more options
#https://data.sca.isr.umich.edu/sda-public/sca/Doc/scafx0.htm

colors = {
    'title': '#0020A0',
    'tabs': '#A08000',
    'text': '#111111'
}

listofplot_names = [
"csi_counts",
"csi_bwp",
"csi_gdp",
"pf_counts",
"pf_bwp",
"pf_gdp",
"pa_counts",
"pa_scatter",
"bc_counts",
"bc_gdp",
"ie_counts",

"ie_gdp",
"demo_counts",
"demo_gdp",
"buyc_counts",
"buyc_bwp",
"buyc_gdp",
"id_counts",
"id_bwp",
"id_gdp",
"wd_counts",

"wd_bwp",
"wd_gdp",
"veh1",
"veh2",
"veh4",
"prob1",
"gas_counts",
"gas_bwp",
"gas_line",
"gas_gdp",

"RF1",
"XG1"
]

tabs = [
"Consumer Sentiment Indices",
"Personal Finance",
"Political Affiliation",
"Business Condition",
"Inflation Expectations",
"Demographic Information",
"Buying Conditions",
"Income Demographics",
"Wealth Demographics",
"Vehicle Information",
"Probabilities",
"Gas Expectations"
]

df = pd.read_csv('https://raw.githubusercontent.com/jhatch04/STATS-507-Group-Project/main/datanew.csv', on_bad_lines='skip')

#Consumer Sentment Indices
df_consumer = df[['YYYYQ','ICS','ICC','ICE','gdp_increase_rate']]
df_consumer = df_consumer.dropna()
df_consumer = df_consumer.reset_index(drop=True)

iterator = 0
csi_counts, axs = plt.subplots(ncols=3, figsize=(15, 5))
sns.histplot(df_consumer["ICS"], kde=True, ax=axs[0])
sns.histplot(df_consumer["ICC"], kde=True, ax=axs[1])
sns.histplot(df_consumer["ICE"], kde=True, ax=axs[2])
fontsize = 11
axs[0].set_title('Index of Consumer Sentiment Count', fontsize=fontsize)
axs[1].set_title('Index of Current Economic Conditions Count', fontsize=fontsize)
axs[2].set_title('Index of Consumer Expectations Count', fontsize=fontsize)

buf = io.BytesIO() # create an in-memory buffer
csi_counts.savefig(buf, format = "png")
listofplot_names[iterator] = "data:image/png;base64,{}".format(base64.b64encode(buf.getbuffer()).decode("utf8"))
buf.close()
iterator += 1
csi_counts.clf()

csi_bwp, axs = plt.subplots(ncols=3, figsize=(15, 5))
sns.boxplot(x = df_consumer["ICS"], ax=axs[0])
sns.boxplot(x = df_consumer["ICC"], ax=axs[1])
sns.boxplot(x = df_consumer["ICE"], ax=axs[2])
fontsize = 11
axs[0].set_title('Index of Consumer Sentiment Distribution', fontsize=fontsize)
axs[1].set_title('Index of Current Economic Conditions Distribution', fontsize=fontsize)
axs[2].set_title('Index of Consumer Expectations Distribution', fontsize=fontsize)

buf = io.BytesIO() # create an in-memory buffer
csi_bwp.savefig(buf, format = "png")
listofplot_names[iterator] = "data:image/png;base64,{}".format(base64.b64encode(buf.getbuffer()).decode("utf8"))
buf.close()
iterator += 1
csi_bwp.clf()

df_consumer_std = df_consumer.copy(deep=True)
df_consumer_std["ICS"] = stats.zscore(df_consumer["ICS"])
df_consumer_std["ICC"] = stats.zscore(df_consumer["ICC"])
df_consumer_std["ICE"] = stats.zscore(df_consumer["ICE"])
df_consumer_std["gdp_increase_rate"] = stats.zscore(df_consumer["gdp_increase_rate"])
csi_gdp, axs = plt.subplots(ncols=3, figsize=(15, 5))
sns.regplot(x = df_consumer_std["ICS"], y = df_consumer_std['gdp_increase_rate'], ax=axs[0])
sns.regplot(x = df_consumer_std["ICC"], y = df_consumer_std['gdp_increase_rate'],ax=axs[1])
sns.regplot(x = df_consumer_std["ICE"], y = df_consumer_std['gdp_increase_rate'],ax=axs[2])
fontsize = 10
axs[0].set_title('GDP Rate vs. Index of Consumer Sentiment', fontsize=fontsize)
axs[1].set_title('GDP Rate vs. Index of Current Economic Conditions', fontsize=fontsize)
axs[2].set_title('GDP Rate vs. Index of Consumer Expectations', fontsize=fontsize)

buf = io.BytesIO() # create an in-memory buffer
csi_gdp.savefig(buf, format = "png")
listofplot_names[iterator] = "data:image/png;base64,{}".format(base64.b64encode(buf.getbuffer()).decode("utf8"))
buf.close()
iterator += 1
csi_gdp.clf()

#Finance
df_finance = df[['YYYYQ','PAGO','PEXP','RINC','gdp_increase_rate']]
df_finance = df_finance.dropna()
df_finance = df_finance.reset_index(drop=True)

pf_counts, axs = plt.subplots(ncols=3, figsize=(15, 5))
sns.histplot(df_finance["PAGO"], kde=True, ax=axs[0])
sns.histplot(df_finance["PEXP"], kde=True, ax=axs[1])
sns.histplot(df_finance["RINC"], kde=True, ax=axs[2])
fontsize=11
axs[0].set_title('Personal Finaces A Year Ago', fontsize=fontsize)
axs[1].set_title('Personal Finances Next Year', fontsize=fontsize)
axs[2].set_title('Real Family Income Next 1-2 Years', fontsize=fontsize)

buf = io.BytesIO() # create an in-memory buffer
pf_counts.savefig(buf, format = "png")
listofplot_names[iterator] = "data:image/png;base64,{}".format(base64.b64encode(buf.getbuffer()).decode("utf8"))
buf.close()
iterator += 1
pf_counts.clf()

pf_bwp, axs = plt.subplots(ncols=3, figsize=(15, 5))
sns.boxplot(x = df_finance["PAGO"], ax=axs[0])
sns.boxplot(x = df_finance["PEXP"], ax=axs[1])
sns.boxplot(x = df_finance["RINC"], ax=axs[2])
fontsize=10
axs[0].set_title('Personal Finaces A Year Ago Distribution', fontsize=fontsize)
axs[1].set_title('Personal Finances Next Year Distribution', fontsize=fontsize)
axs[2].set_title('Real Family Income Next 1-2 Years Distribution', fontsize=fontsize)

buf = io.BytesIO() # create an in-memory buffer
pf_bwp.savefig(buf, format = "png")
listofplot_names[iterator] = "data:image/png;base64,{}".format(base64.b64encode(buf.getbuffer()).decode("utf8"))
buf.close()
iterator += 1
pf_bwp.clf()

df_finance_std = df_finance.copy(deep=True)
df_finance_std["PAGO"] = stats.zscore(df_finance_std["PAGO"])
df_finance_std["PEXP"] = stats.zscore(df_finance_std["PEXP"])
df_finance_std["RINC"] = stats.zscore(df_finance_std["RINC"])
df_finance_std["gdp_increase_rate"] = stats.zscore(df_finance_std["gdp_increase_rate"])
pf_gdp, axs = plt.subplots(ncols=3, figsize=(15, 5))
sns.regplot(x = df_finance_std["PAGO"], y = df_finance_std['gdp_increase_rate'], ax=axs[0])
sns.regplot(x = df_finance_std["PEXP"], y = df_finance_std['gdp_increase_rate'],ax=axs[1])
sns.regplot(x = df_finance_std["RINC"], y = df_finance_std['gdp_increase_rate'],ax=axs[2])
fontsize=10
axs[0].set_title('GDP Rate vs. Personal Finaces A Year Ago', fontsize=fontsize)
axs[1].set_title('GDP Rate vs. Personal Finances Next Year', fontsize=fontsize)
axs[2].set_title('GDP Rate vs. Real Family Income Next 1-2 Years', fontsize=fontsize)

buf = io.BytesIO() # create an in-memory buffer
pf_gdp.savefig(buf, format = "png")
listofplot_names[iterator] = "data:image/png;base64,{}".format(base64.b64encode(buf.getbuffer()).decode("utf8"))
buf.close()
iterator += 1
pf_gdp.clf()

#Plotical Affiliation
df_political = df[['YYYYQ','POLAFF','POLREP','POLDEM','POLCRD','gdp_increase_rate']]
df_political = df_political.dropna()
df_political = df_political.reset_index(drop=True)

pa_counts, axs = plt.subplots(1,4,figsize=(20, 8))
sns.histplot(df_political["POLAFF"], kde=True, ax=axs[0])
sns.histplot(df_political["POLREP"], kde=True, ax=axs[1])
sns.histplot(df_political["POLDEM"], kde=True, ax=axs[2])
sns.histplot(df_political["POLCRD"], kde=True, ax=axs[3])
fontsize=11
axs[0].set_title('Political Affiliation', fontsize=fontsize)
axs[1].set_title('Strong or Not Strong Republican', fontsize=fontsize)
axs[2].set_title('Strong or not Strong Democrat', fontsize=fontsize)
axs[3].set_title('Closer to Republican or Democrat', fontsize=fontsize)
pa_counts.subplots_adjust(left=0.1, right=0.9, top=0.8, bottom=0.1, hspace=0.3, wspace=0.5)

buf = io.BytesIO() # create an in-memory buffer
pa_counts.savefig(buf, format = "png")
listofplot_names[iterator] = "data:image/png;base64,{}".format(base64.b64encode(buf.getbuffer()).decode("utf8"))
buf.close()
iterator += 1
pa_counts.clf()

df_political_std = df_political.copy(deep=True)
df_political_std["gdp_increase_rate"] = stats.zscore(df_political_std["gdp_increase_rate"])
pa_scatter, axs = plt.subplots(1,4,figsize=(20, 8))
sns.scatterplot(x = df_political_std["POLAFF"], y = df_political_std['gdp_increase_rate'],ax=axs[0])
sns.scatterplot(x = df_political_std["POLREP"], y = df_political_std['gdp_increase_rate'],ax=axs[1])
sns.scatterplot(x = df_political_std["POLDEM"], y = df_political_std['gdp_increase_rate'],ax=axs[2])
sns.scatterplot(x = df_political_std["POLCRD"], y = df_political_std['gdp_increase_rate'],ax=axs[3])
fontsize=11
axs[0].set_title('GDP Rate vs. Political Affiliation', fontsize=fontsize)
axs[1].set_title('GDP Rate vs. Strong or Not Strong Republican', fontsize=fontsize)
axs[2].set_title('GDP Rate vs. Strong or not Strong Democrat', fontsize=fontsize)
axs[3].set_title('GDP Rate vs. Closer to Republican or Democrat', fontsize=fontsize)
pa_scatter.subplots_adjust(left=0.1, right=0.9, top=0.8, bottom=0.1, hspace=0.3, wspace=0.5)

buf = io.BytesIO() # create an in-memory buffer
pa_scatter.savefig(buf, format = "png")
listofplot_names[iterator] = "data:image/png;base64,{}".format(base64.b64encode(buf.getbuffer()).decode("utf8"))
buf.close()
iterator += 1
pa_scatter.clf()

#Business Condition
business_col = ['BAGO', 'BEXP', 'BUS12', 'BUS5', 'NEWS1', 'NEWS2', 'UNEMP', 'GOVT', 'RATEX']
df_business = df[['YYYYQ', 'gdp_increase_rate'] + business_col]
# df_business = df_business[pd.notna(df_business['gdp_increase_rate'])]
df_business = df_business.dropna()
bc_counts, axs = plt.subplots(nrows = 3, ncols = 3, figsize = (20, 15))
for i in range(len(business_col)):
    sns.histplot(df_business[business_col[i]], kde = True, ax = axs[i // 3, i % 3])
fontsize=11
axs[0,0].set_title('Present Economy Sentiment Compared to Last Year', fontsize=fontsize)
axs[0,1].set_title('Economy Sentiment for Next Year Compared to Present', fontsize=fontsize)
axs[0,2].set_title('Sentiment of Economy for Next 12 Months', fontsize=fontsize)
axs[1,0].set_title('Sentiment of Economy for Next 5 Years', fontsize=fontsize)
axs[1,1].set_title('News Heard Reflecting Economy - 1', fontsize=fontsize)
axs[1,2].set_title('News Heard Reflecting Economy - 2', fontsize=fontsize)
axs[2,0].set_title('Unemployment Sentiment for Next Year', fontsize=fontsize)
axs[2,1].set_title('Government Economic Policy Sentiment', fontsize=fontsize)
axs[2,2].set_title('Interest Rates Sentiment for Next Year', fontsize=fontsize)
bc_counts.subplots_adjust(left=0.1, right=0.9, top=0.8, bottom=0.1, hspace=0.3, wspace=0.5)

buf = io.BytesIO() # create an in-memory buffer
bc_counts.savefig(buf, format = "png")
listofplot_names[iterator] = "data:image/png;base64,{}".format(base64.b64encode(buf.getbuffer()).decode("utf8"))
buf.close()
iterator += 1
bc_counts.clf()

df_business_std = df_business.copy(deep = True)
for col in business_col:
    df_business_std[col] = stats.zscore(df_business_std[col])

bc_gdp, axs = plt.subplots(nrows = 3, ncols = 3, figsize = (20, 15))
for i in range(len(business_col)):
    sns.regplot(x = df_business_std[business_col[i]], y = df_business_std['gdp_increase_rate'], ax = axs[i // 3, i % 3])
fontsize=9
axs[0,0].set_title('GDP Rate vs. Present Economy Sentiment Compared to Last Year', fontsize=fontsize)
axs[0,1].set_title('GDP Rate vs. Economy Sentiment for Next Year Compared to Present', fontsize=fontsize)
axs[0,2].set_title('GDP Rate vs. Sentiment of Economy for Next 12 Months', fontsize=fontsize)
axs[1,0].set_title('GDP Rate vs. Sentiment of Economy for Next 5 Years', fontsize=fontsize)
axs[1,1].set_title('GDP Rate vs. News Heard Reflecting Economy - 1', fontsize=fontsize)
axs[1,2].set_title('GDP Rate vs. News Heard Reflecting Economy - 2', fontsize=fontsize)
axs[2,0].set_title('GDP Rate vs. Unemployment Sentiment for Next Year', fontsize=fontsize)
axs[2,1].set_title('GDP Rate vs. Government Economic Policy Sentiment', fontsize=fontsize)
axs[2,2].set_title('GDP Rate vs. Interest Rates Sentiment for Next Year', fontsize=fontsize)
bc_gdp.subplots_adjust(left=0.1, right=0.9, top=0.8, bottom=0.1, hspace=0.25, wspace=0.5)

buf = io.BytesIO() # create an in-memory buffer
bc_gdp.savefig(buf, format = "png")
listofplot_names[iterator] = "data:image/png;base64,{}".format(base64.b64encode(buf.getbuffer()).decode("utf8"))
buf.close()
iterator += 1
bc_gdp.clf()

#Inflation Expectation
inflation_col = ['PX1Q1', 'PX1Q2', 'PX1', 'PX5Q1', 'PX5Q2', 'PX5']
df_inflation = df[['YYYYQ', 'gdp_increase_rate'] + inflation_col]
# df_inflation = df_inflation[pd.notna(df_inflation['gdp_increase_rate'])]
df_inflation = df_inflation.dropna()

ie_counts, axs = plt.subplots(nrows = 2, ncols = 3, figsize = (15, 10))
for i in range(len(inflation_col)):
    sns.histplot(df_inflation[inflation_col[i]], kde = True, ax = axs[i // 3, i % 3])
fontsize=11
axs[0,0].set_title('General Price Direction In The Next 12 Months', fontsize=fontsize)
axs[0,1].set_title('Price Percentage Difference In The Next 12 Months', fontsize=fontsize)
axs[0,2].set_title('Price Expectations For Next Year', fontsize=fontsize)
axs[1,0].set_title('Price Expectations For Next 5-10 Years', fontsize=fontsize)
axs[1,1].set_title('Prince Percentage Difference For Next 5-10 Years', fontsize=fontsize)
axs[1,2].set_title('Prince Expectation for Next 5 Years', fontsize=fontsize)
ie_counts.subplots_adjust(left=0.1, right=0.9, top=0.8, bottom=0.1, hspace=0.3, wspace=0.5)

buf = io.BytesIO() # create an in-memory buffer
ie_counts.savefig(buf, format = "png")
listofplot_names[iterator] = "data:image/png;base64,{}".format(base64.b64encode(buf.getbuffer()).decode("utf8"))
buf.close()
iterator += 1
ie_counts.clf()

df_inflation_std = df_inflation.copy(deep = True)
for col in inflation_col:
    df_inflation_std[col] = stats.zscore(df_inflation_std[col])

ie_gdp, axs = plt.subplots(nrows = 2, ncols = 3, figsize = (20, 15))
for i in range(len(inflation_col)):
    sns.regplot(x = df_inflation_std[inflation_col[i]], y = df_inflation_std['gdp_increase_rate'], ax = axs[i // 3, i % 3])
fontsize=10
axs[0,0].set_title('GDP Rate vs. General Price Direction In The Next 12 Months', fontsize=fontsize)
axs[0,1].set_title('GDP Rate vs. Price Percentage Difference In The Next 12 Months', fontsize=fontsize)
axs[0,2].set_title('GDP Rate vs. Price Expectations For Next Year', fontsize=fontsize)
axs[1,0].set_title('GDP Rate vs. Price Expectations For Next 5-10 Years', fontsize=fontsize)
axs[1,1].set_title('GDP Rate vs. Prince Percentage Difference For Next 5-10 Years', fontsize=fontsize)
axs[1,2].set_title('GDP Rate vs. Prince Expectation for Next 5 Years', fontsize=fontsize)
ie_gdp.subplots_adjust(left=0.1, right=0.9, top=0.8, bottom=0.1, hspace=0.3, wspace=0.5)

buf = io.BytesIO() # create an in-memory buffer
ie_gdp.savefig(buf, format = "png")
listofplot_names[iterator] = "data:image/png;base64,{}".format(base64.b64encode(buf.getbuffer()).decode("utf8"))
buf.close()
iterator += 1
ie_gdp.clf()

# demographic
demographic_col = ['AGE', 'BIRTHM', 'BIRTHY', 'REGION', 'SEX', 'MARRY', 'NUMKID', 'NUMADT', 'EDUC', 'ECLGRD', 'EHSGRD', 'EGRADE']
df_demographic = df[['YYYYQ', 'gdp_increase_rate'] + demographic_col]
df_demographic = df_demographic.dropna()

demo_counts, axs = plt.subplots(nrows = 4, ncols = 3, figsize = (20, 20))
for i in range(len(demographic_col)):
    sns.histplot(df_demographic[demographic_col[i]], kde = True, ax = axs[i // 3, i % 3])
for ax in axs.flatten():
    for label in ax.get_xticklabels():
        label.set_rotation(60)
fontsize=11
axs[0,0].set_title('Age of Respondent', fontsize=fontsize)
axs[0,1].set_title('Month of Birth', fontsize=fontsize)
#axs[0,1].tick_params(axis='x', labelsize=5)
axs[0,2].set_title('Year of Birth', fontsize=fontsize)
axs[1,0].set_title('Region of Residence', fontsize=fontsize)
axs[1,1].set_title('Sex of Respondent', fontsize=fontsize)
axs[1,2].set_title('Marital Status of Respondent', fontsize=fontsize)
axs[2,0].set_title('Number of Residents Less than 18 in Household', fontsize=fontsize)
axs[2,1].set_title('Number of Residents 18 or Older in Household', fontsize=fontsize)
axs[2,2].set_title('Education Level of Respondent', fontsize=fontsize)
axs[3,0].set_title('Does Respondent Have a College Degree', fontsize=fontsize)
axs[3,1].set_title('Does Respondent Have a High School Degree', fontsize=fontsize)
axs[3,2].set_title('Highest Level of Education Completed', fontsize=fontsize)
demo_counts.subplots_adjust(left=0.1, right=0.9, top=0.8, bottom=0.1, hspace=0.3, wspace=0.2)

buf = io.BytesIO() # create an in-memory buffer
demo_counts.savefig(buf, format = "png")
listofplot_names[iterator] = "data:image/png;base64,{}".format(base64.b64encode(buf.getbuffer()).decode("utf8"))
buf.close()
iterator += 1
demo_counts.clf()

df_demographic_std = df_demographic.copy(deep = True)
for col in demographic_col:
    if col == 'BIRTHM':
        continue
    df_demographic_std[col] = stats.zscore(df_demographic_std[col])

demo_gdp, axs = plt.subplots(nrows = 4, ncols = 3, figsize = (20, 20))
for i in range(len(demographic_col)):
    if demographic_col[i] == 'BIRTHM':
        continue
    sns.regplot(x = df_demographic_std[demographic_col[i]], y = df_demographic_std['gdp_increase_rate'], ax = axs[i // 3, i % 3])
fontsize=11
axs[0,0].set_title('Age of Respondent', fontsize=fontsize)
axs[0,1].set_title('Month of Birth', fontsize=fontsize)
#axs[0,1].tick_params(axis='x', labelsize=5)
axs[0,2].set_title('Year of Birth', fontsize=fontsize)
axs[1,0].set_title('Region of Residence', fontsize=fontsize)
axs[1,1].set_title('Sex of Respondent', fontsize=fontsize)
axs[1,2].set_title('Marital Status of Respondent', fontsize=fontsize)
axs[2,0].set_title('Number of Residents Less than 18 in Household', fontsize=fontsize)
axs[2,1].set_title('Number of Residents 18 or Older in Household', fontsize=fontsize)
axs[2,2].set_title('Education Level of Respondent', fontsize=fontsize)
axs[3,0].set_title('Does Respondent Have a College Degree', fontsize=fontsize)
axs[3,1].set_title('Does Respondent Have a High School Degree', fontsize=fontsize)
axs[3,2].set_title('Highest Level of Education Completed', fontsize=fontsize)
demo_gdp.subplots_adjust(left=0.1, right=0.9, top=0.8, bottom=0.1, hspace=0.3, wspace=0.4)

buf = io.BytesIO() # create an in-memory buffer
demo_gdp.savefig(buf, format = "png")
listofplot_names[iterator] = "data:image/png;base64,{}".format(base64.b64encode(buf.getbuffer()).decode("utf8"))
buf.close()
iterator += 1
demo_gdp.clf()

# Buying Conditions:
df_buying = df[['YYYYQ','DUR','HOM','CAR','gdp_increase_rate']]
df_buying = df_buying.dropna()
df_buying = df_buying.reset_index(drop=True)

buyc_counts, axs = plt.subplots(ncols=3, figsize=(15, 5))
sns.histplot(df_buying["DUR"], kde=True, ax=axs[0])
sns.histplot(df_buying["HOM"], kde=True, ax=axs[1])
sns.histplot(df_buying["CAR"], kde=True, ax=axs[2])
fontsize=11
axs[0].set_title('Sentiment on Buying Major Household Items', fontsize=fontsize)
axs[1].set_title('Sentiment on Buying a Home Now', fontsize=fontsize)
axs[2].set_title('Sentiment on Buying a Vehicle Within the Year', fontsize=fontsize)
buyc_counts.subplots_adjust(left=0.1, right=0.9, top=0.8, bottom=0.1, hspace=0.3, wspace=0.4)

buf = io.BytesIO() # create an in-memory buffer
buyc_counts.savefig(buf, format = "png")
listofplot_names[iterator] = "data:image/png;base64,{}".format(base64.b64encode(buf.getbuffer()).decode("utf8"))
buf.close()
iterator += 1
buyc_counts.clf()

buyc_bwp, axs = plt.subplots(ncols=3, figsize=(15, 5))
sns.boxplot(x = df_buying["DUR"], ax=axs[0])
sns.boxplot(x = df_buying["HOM"], ax=axs[1])
sns.boxplot(x = df_buying["CAR"], ax=axs[2])
fontsize=9
axs[0].set_title('Sentiment on Buying Major Household Items Distribution', fontsize=fontsize)
axs[1].set_title('Sentiment on Buying a Home Now Distribution', fontsize=fontsize)
axs[2].set_title('Sentiment on Buying a Vehicle Within the Year Distribution', fontsize=fontsize)

buf = io.BytesIO() # create an in-memory buffer
buyc_bwp.savefig(buf, format = "png")
listofplot_names[iterator] = "data:image/png;base64,{}".format(base64.b64encode(buf.getbuffer()).decode("utf8"))
buf.close()
iterator += 1
buyc_bwp.clf()

df_buying_std = df_buying.copy(deep=True)
df_buying_std["DUR"] = stats.zscore(df_buying["DUR"])
df_buying_std["HOM"] = stats.zscore(df_buying["HOM"])
df_buying_std["CAR"] = stats.zscore(df_buying["CAR"])
df_buying_std["gdp_increase_rate"] = stats.zscore(df_buying["gdp_increase_rate"])
buyc_gdp, axs = plt.subplots(ncols=3, figsize=(15, 5))
sns.regplot(x = df_buying_std["DUR"], y = df_buying_std['gdp_increase_rate'],ax=axs[0])
sns.regplot(x = df_buying_std["HOM"], y = df_buying_std['gdp_increase_rate'],ax=axs[1])
sns.regplot(x = df_buying_std["CAR"], y = df_buying_std['gdp_increase_rate'],ax=axs[2])
fontsize=11
axs[0].set_title('GDP Rate vs. Sentiment on Buying Major Household Items', fontsize=fontsize)
axs[1].set_title('GDP Rate vs. Sentiment on Buying a Home Now', fontsize=fontsize)
axs[2].set_title('GDP Rate vs. Sentiment on Buying a Vehicle Within the Year', fontsize=fontsize)
buyc_gdp.subplots_adjust(left=0.1, right=0.9, top=0.8, bottom=0.1, hspace=0.3, wspace=0.4)

buf = io.BytesIO() # create an in-memory buffer
buyc_gdp.savefig(buf, format = "png")
listofplot_names[iterator] = "data:image/png;base64,{}".format(base64.b64encode(buf.getbuffer()).decode("utf8"))
buf.close()
iterator += 1
buyc_gdp.clf()

# Income Demographics:
df_income = df[['YYYYQ','INCOME','gdp_increase_rate']]
df_income = df_income.dropna()
df_income = df_income.reset_index(drop=True)

id_counts, axs = plt.subplots(ncols=1, figsize=(5, 5))
sns.histplot(df_income["INCOME"], kde=True)
axs.set_title('Total Household Income of Previous Year', fontsize=fontsize)

buf = io.BytesIO() # create an in-memory buffer
id_counts.savefig(buf, format = "png")
listofplot_names[iterator] = "data:image/png;base64,{}".format(base64.b64encode(buf.getbuffer()).decode("utf8"))
buf.close()
iterator += 1
id_counts.clf()

id_bwp, axs = plt.subplots(ncols=1, figsize=(5, 5))
sns.boxplot(x = df_income["INCOME"])
axs.set_title('Total Household Income of Previous Year Distribution', fontsize=fontsize)

buf = io.BytesIO() # create an in-memory buffer
id_bwp.savefig(buf, format = "png")
listofplot_names[iterator] = "data:image/png;base64,{}".format(base64.b64encode(buf.getbuffer()).decode("utf8"))
buf.close()
iterator += 1
id_bwp.clf()

df_income_std = df_income.copy(deep=True)
df_income_std["INCOME"] = stats.zscore(df_income_std["INCOME"])
df_income_std["gdp_increase_rate"] = stats.zscore(df_income_std["gdp_increase_rate"])
id_gdp, axs = plt.subplots(ncols=1, figsize=(5, 5))
sns.regplot(x = df_income_std["INCOME"], y = df_income_std['gdp_increase_rate'])
axs.set_title('GDP Rate vs. Total Household Income of Previous Year', fontsize=fontsize)

buf = io.BytesIO() # create an in-memory buffer
id_gdp.savefig(buf, format = "png")
listofplot_names[iterator] = "data:image/png;base64,{}".format(base64.b64encode(buf.getbuffer()).decode("utf8"))
buf.close()
iterator += 1
id_gdp.clf()

#wealth_demographics
df_wealth = df[['YYYYQ','HOMEAMT','INVAMT','gdp_increase_rate']]
df_wealth = df_wealth.dropna()
df_wealth = df_wealth.reset_index(drop=True)

wd_counts, axs = plt.subplots(ncols=2, figsize=(10, 5))
sns.histplot(df_wealth["HOMEAMT"], kde=True, ax=axs[0])
sns.histplot(df_wealth["INVAMT"], kde=True, ax=axs[1])
fontsize=11
axs[0].set_title('Current Market Value of Home', fontsize=fontsize)
axs[1].set_title('Current Total Investment Worth', fontsize=fontsize)
wd_counts.subplots_adjust(left=0.1, right=0.9, top=0.8, bottom=0.1, hspace=0.3, wspace=0.4)

buf = io.BytesIO() # create an in-memory buffer
wd_counts.savefig(buf, format = "png")
listofplot_names[iterator] = "data:image/png;base64,{}".format(base64.b64encode(buf.getbuffer()).decode("utf8"))
buf.close()
iterator += 1
wd_counts.clf()

wd_bwp, axs = plt.subplots(ncols=2, figsize=(10, 5))
sns.boxplot(x = df_wealth["HOMEAMT"], ax=axs[0])
sns.boxplot(x = df_wealth["INVAMT"], ax=axs[1])
fontsize=11
axs[0].set_title('Current Market Value of Home Distribution', fontsize=fontsize)
axs[1].set_title('Current Total Investment Worth Distribution', fontsize=fontsize)
wd_bwp.subplots_adjust(left=0.1, right=0.9, top=0.8, bottom=0.1, hspace=0.3, wspace=0.4)

buf = io.BytesIO() # create an in-memory buffer
wd_bwp.savefig(buf, format = "png")
listofplot_names[iterator] = "data:image/png;base64,{}".format(base64.b64encode(buf.getbuffer()).decode("utf8"))
buf.close()
iterator += 1
wd_bwp.clf()

df_wealth_std = df_wealth.copy(deep=True)
df_wealth_std["HOMEAMT"] = stats.zscore(df_wealth["HOMEAMT"])
df_wealth_std["INVAMT"] = stats.zscore(df_wealth["INVAMT"])
df_wealth_std["gdp_increase_rate"] = stats.zscore(df_wealth["gdp_increase_rate"])
wd_gdp, axs = plt.subplots(ncols=2, figsize=(10, 5))
sns.regplot(x = df_wealth_std["HOMEAMT"], y = df_wealth_std['gdp_increase_rate'],ax=axs[0])
sns.regplot(x = df_wealth_std["INVAMT"], y = df_wealth_std['gdp_increase_rate'],ax=axs[1])
fontsize=11
axs[0].set_title('GDP Rate vs. Current Market Value of Home', fontsize=fontsize)
axs[1].set_title('GDP Rate vs. Current Total Investment Worth', fontsize=fontsize)
wd_gdp.subplots_adjust(left=0.1, right=0.9, top=0.8, bottom=0.1, hspace=0.3, wspace=0.4)

buf = io.BytesIO() # create an in-memory buffer
wd_gdp.savefig(buf, format = "png")
listofplot_names[iterator] = "data:image/png;base64,{}".format(base64.b64encode(buf.getbuffer()).decode("utf8"))
buf.close()
iterator += 1
wd_gdp.clf()

#Vehicle
df2=df.loc[(df['VEHNUM']>0)]
veh1, axs = plt.subplots(ncols=1, figsize=(10,10))
plt.title('Average number of vehicles owned/leased',fontsize=18)
plt.xlabel('YYYYQ',fontsize=14)
plt.plot(df2['YYYYQ'],df2['VEHNUM'],'y^',alpha = 0.5)
locs, labs = plt.xticks()
plt.grid(True)
plt.xticks(locs)

buf = io.BytesIO() # create an in-memory buffer
veh1.savefig(buf, format = "png")
listofplot_names[iterator] = "data:image/png;base64,{}".format(base64.b64encode(buf.getbuffer()).decode("utf8"))
buf.close()
iterator += 1
veh1.clf()

veh2, axs = plt.subplots(ncols=1, figsize=(10,10))
plt.title('Average number of vehicles owned/leased',fontsize=18)
plt.xlabel('YYYYQ',fontsize=14)
plt.bar(df2['YYYYQ'],df2['VEHNUM'],alpha = 0.5)

buf = io.BytesIO() # create an in-memory buffer
veh2.savefig(buf, format = "png")
listofplot_names[iterator] = "data:image/png;base64,{}".format(base64.b64encode(buf.getbuffer()).decode("utf8"))
buf.close()
iterator += 1
veh2.clf()

df2 = df2[['YYYYQ','VEHNUM','GDP', 'gdp_increase_rate']]
corr = pd.DataFrame(df2).corr()
buf2 = io.BytesIO() # create an in-memory buffer
veh_heatmap = sns.heatmap(corr,vmin=-1,vmax=1,center=0,cmap=sns.diverging_palette(200,20,n=100))
veh_heatmap = veh_heatmap.get_figure()
veh_heatmap.savefig(buf2, format = "png",bbox_inches = 'tight')
veh_heatmap = "data:image/png;base64,{}".format(base64.b64encode(buf2.getbuffer()).decode("utf8"))
plt.clf()
buf2.close()
dfH = df2.loc[(df2['VEHNUM']>1.5)]
# veh3 = sns.lmplot(x='YYYYQ',y='VEHNUM',data=dfH)


veh4, axs = plt.subplots(1,3,figsize=(15, 10))
sns.regplot(y=dfH['GDP'],x=dfH['VEHNUM'],ax=axs[0])
sns.regplot(y=dfH['gdp_increase_rate'],x=dfH['VEHNUM'],ax=axs[1])
sns.regplot(x=dfH['YYYYQ'],y=dfH['VEHNUM'],ax=axs[2])
axs[0].set_title('GDP vs. Number of Vehicles Owned or Leased', fontsize=fontsize)
axs[1].set_title('GDP Rate vs. Number of Vehicles Owned or Leased', fontsize=fontsize)
axs[2].set_title('Number of Vehicles Owned or Leased vs Year', fontsize=fontsize)
veh4.subplots_adjust(left=0.1, right=0.9, top=0.8, bottom=0.1, hspace=0.3, wspace=0.4)

buf = io.BytesIO() # create an in-memory buffer
veh4.savefig(buf, format = "png")
listofplot_names[iterator] = "data:image/png;base64,{}".format(base64.b64encode(buf.getbuffer()).decode("utf8"))
buf.close()
iterator += 1
veh4.clf()

#Probabilities
p1 = df[['YYYYQ', 'PINC', 'PINC2', 'PJOB', 'PSSA', 'PCRY', 'PSTK','gdp_increase_rate']]
p1 = p1.dropna()
prob1, axs = plt.subplots(nrows=2,ncols=3, figsize=(15, 10))
PCN = ['PINC', 'PINC2','PJOB', 'PSSA', 'PCRY', 'PSTK']
for i in range(6):
     sns.histplot(p1[PCN[i]], kde=True, ax=axs[i//3,i%3])
fontsize=11
axs[0,0].set_title('Chance Income Will Outpace Inflation', fontsize=fontsize)
axs[0,1].set_title('Percent Change of Income Increase', fontsize=fontsize)
axs[0,2].set_title('Chance to Lose Job in 5 Years', fontsize=fontsize)
axs[1,0].set_title('Chance to Have Social Security', fontsize=fontsize)
axs[1,1].set_title('Sentiment of Having Comfortable Retirement', fontsize=fontsize)
axs[1,2].set_title('Percent Chance of Investment Increase Within Year', fontsize=fontsize)
prob1.subplots_adjust(left=0.1, right=0.9, top=0.8, bottom=0.1, hspace=0.4, wspace=0.5)

buf = io.BytesIO() # create an in-memory buffer
prob1.savefig(buf, format = "png")
listofplot_names[iterator] = "data:image/png;base64,{}".format(base64.b64encode(buf.getbuffer()).decode("utf8"))
buf.close()
iterator += 1
prob1.clf()

#Gas
E = df[['YYYYQ', 'GASPX2','GAS1','GAS1PX2','GAS5','GASPX1','GAS1PX1', 'gdp_increase_rate']]
E1 = E.loc[(E['GAS5']<=500) &(E['GAS5']>=-250) & (E['GAS1']<=250)&(E['GAS1']>=-250)]
gas_counts, axs = plt.subplots(ncols=2, figsize=(15, 5))
sns.histplot(E1['GAS5'], kde=True, ax=axs[0])
sns.histplot(E1['GAS1'], kde=True, ax=axs[1])
fontsize=11
axs[0].set_title('Gas Price Change For The Next 5 Years', fontsize=fontsize)
axs[1].set_title('Gas Price Change Within The Next Year', fontsize=fontsize)
gas_counts.subplots_adjust(left=0.1, right=0.9, top=0.8, bottom=0.1, hspace=0.4, wspace=0.2)

buf = io.BytesIO() # create an in-memory buffer
gas_counts.savefig(buf, format = "png")
listofplot_names[iterator] = "data:image/png;base64,{}".format(base64.b64encode(buf.getbuffer()).decode("utf8"))
buf.close()
iterator += 1
gas_counts.clf()

gas_bwp, axs = plt.subplots(ncols=2, figsize=(15, 5))
sns.boxplot(x = E1["GAS5"], ax=axs[0])
sns.boxplot(x = E1["GAS1"], ax=axs[1])
fontsize=11
axs[0].set_title('Gas Price Change For The Next 5 Years Distribution', fontsize=fontsize)
axs[1].set_title('Gas Price Change Within The Next Year Distribution', fontsize=fontsize)
gas_bwp.subplots_adjust(left=0.1, right=0.9, top=0.8, bottom=0.1, hspace=0.4, wspace=0.2)

buf = io.BytesIO() # create an in-memory buffer
gas_bwp.savefig(buf, format = "png")
listofplot_names[iterator] = "data:image/png;base64,{}".format(base64.b64encode(buf.getbuffer()).decode("utf8"))
buf.close()
iterator += 1
gas_bwp.clf()

gas_line, axs = plt.subplots(ncols=2, figsize=(15, 5))
sns.lineplot(x = E1['YYYYQ'],y = E1['GASPX1'], ax=axs[0])
sns.lineplot(x = E1['YYYYQ'],y = E1['GAS1PX1'], ax=axs[1])
fontsize=11
axs[0].set_title('Gas Price Change For The Next 5 Years vs. Year', fontsize=fontsize)
axs[1].set_title('Gas Price Change Within The Next Year vs. Year', fontsize=fontsize)
gas_line.subplots_adjust(left=0.1, right=0.9, top=0.8, bottom=0.1, hspace=0.4, wspace=0.2)

buf = io.BytesIO() # create an in-memory buffer
gas_line.savefig(buf, format = "png")
listofplot_names[iterator] = "data:image/png;base64,{}".format(base64.b64encode(buf.getbuffer()).decode("utf8"))
buf.close()
iterator += 1
gas_line.clf()

dfgdp = df[['YYYYQ','gdp_increase_rate']].dropna()
dfgdp = dfgdp.reset_index(drop=True)
df_consumer_std = E1.copy(deep=True)
df_consumer_std["GAS5"] = stats.zscore(E1["GAS5"])
df_consumer_std["GAS1"] = stats.zscore(E1["GAS1"])
# df_consumer_std["gdp_increase_rate"] = stats.zscore(dfgdp["gdp_increase_rate"])
gas_gdp, axs = plt.subplots(ncols=2, figsize=(15, 5))
sns.regplot(x = df_consumer_std["GAS5"], y = df_consumer_std['gdp_increase_rate'], ax=axs[0])
sns.regplot(x = df_consumer_std["GAS1"], y = df_consumer_std['gdp_increase_rate'],ax=axs[1])
df_consumer_std["gdp_increase_rate"]
fontsize=11
axs[0].set_title('GDP Rate vs. Gas Price Change For The Next 5 Years', fontsize=fontsize)
axs[1].set_title('GDP Rate vs. Gas Price Change Within The Next Year', fontsize=fontsize)
gas_gdp.subplots_adjust(left=0.1, right=0.9, top=0.8, bottom=0.1, hspace=0.4, wspace=0.2)


buf = io.BytesIO() # create an in-memory buffer
gas_gdp.savefig(buf, format = "png")
listofplot_names[iterator] = "data:image/png;base64,{}".format(base64.b64encode(buf.getbuffer()).decode("utf8"))
buf.close()
iterator += 1
gas_gdp.clf()

#ML Section
preds = [0.0038189576, 0.0035301175, 0.0017585831, 0.0024566867, 0.0041350494, 0.016022118, 0.012911082, 0.015083434, 0.018932827, -0.008756744, 0.0047494387, -0.08710402]

dict_preds = {
    "20232":preds[0],
    "20233":preds[1],
    "20234":preds[2],
    "20241":preds[3],
    "20242":preds[4],
    "20243":preds[5],
    "20244":preds[6],
    "20251":preds[7],
    "20252":preds[8],
    "20253":preds[9],
    "20254":preds[10],
    "20261":preds[11]
}
def predict(yearq):
    if yearq in dict_preds.keys():
        return dict_preds[yearq]
    else:
        raise(ValueError)


mserid=0.000043
r2rid=0.393953

mserf=0.000038
r2rf=0.462958

msexg=0.000033
r2xg=0.534914


business_corr = df_business.iloc[:, 1:].corr()
buf = io.BytesIO() # create an in-memory buffer
bc_heatmap = sns.heatmap(business_corr, vmin = -1, vmax = 1, center = 0, cmap = sns.diverging_palette(200, 20, n = 100))
bc_heatmap = bc_heatmap.get_figure()
bc_heatmap.savefig(buf, format = "png")
bc_heatmap = "data:image/png;base64,{}".format(base64.b64encode(buf.getbuffer()).decode("utf8"))
plt.clf()
buf.close()

demographic_corr = df_demographic.iloc[:, 1:].corr()
buf2 = io.BytesIO() # create an in-memory buffer
demo_heatmap = sns.heatmap(demographic_corr, vmin = -1, vmax = 1, center = 0, cmap = sns.diverging_palette(200, 20, n = 100))
demo_heatmap = demo_heatmap.get_figure()
demo_heatmap.savefig(buf2, format = "png",bbox_inches = 'tight')
demo_heatmap = "data:image/png;base64,{}".format(base64.b64encode(buf2.getbuffer()).decode("utf8"))
plt.clf()
buf2.close()

corr = pd.DataFrame(p1).corr()
buf3 = io.BytesIO() # create an in-memory buffer
prob_heatmap = sns.heatmap(corr,vmin=-1,vmax=1,center=0,cmap=sns.diverging_palette(200,20,n=100))
prob_heatmap = prob_heatmap.get_figure()
prob_heatmap.savefig(buf3, format = "png",bbox_inches = 'tight')
prob_heatmap = "data:image/png;base64,{}".format(base64.b64encode(buf3.getbuffer()).decode("utf8"))
plt.clf()
buf3.close()


app.layout = html.Div([
    html.H1('Analysis of University of Michigan Consumer Survey Data Using Exploratory Data Analytics and Machine Learning',style={
            'textAlign': 'center',
            'color': colors['title']
        }),
    dcc.Markdown(children = '''
    #### The following allows one to predict the change in GDP of the US based on our findings. Please input a YYYYQ between now and  20261.
    '''),
    dcc.Input(children="callback not executed",
            id="input1",
            type="number",
            placeholder=20234,
            ),
    html.Div(id="output"),
    html.Br(),
    html.Br(),
    dcc.Tabs(id='tabs-example-1', value='tab-0', children=[
        dcc.Tab(label="Introduction",style={'color': colors['tabs']}, value='tab-0'),
        dcc.Tab(label=tabs[0],style={'color': colors['tabs']}, value='tab-1'),
        dcc.Tab(label=tabs[1],style={'color': colors['tabs']}, value='tab-2'),
        dcc.Tab(label=tabs[2],style={'color': colors['tabs']}, value='tab-3'),
        dcc.Tab(label=tabs[3],style={'color': colors['tabs']}, value='tab-4'),
        dcc.Tab(label=tabs[4],style={'color': colors['tabs']}, value='tab-5'),
        dcc.Tab(label=tabs[5],style={'color': colors['tabs']}, value='tab-6'),
        dcc.Tab(label=tabs[6],style={'color': colors['tabs']}, value='tab-7'),
        dcc.Tab(label=tabs[7],style={'color': colors['tabs']}, value='tab-8'),
        dcc.Tab(label=tabs[8],style={'color': colors['tabs']}, value='tab-9'),
        dcc.Tab(label=tabs[9],style={'color': colors['tabs']}, value='tab-10'),
        dcc.Tab(label=tabs[10],style={'color': colors['tabs']}, value='tab-11'),
        dcc.Tab(label=tabs[11],style={'color': colors['tabs']}, value='tab-12'),
        dcc.Tab(label="Machine Learning",style={'color': colors['tabs']}, value='tab-13'),
        dcc.Tab(label="Conclusions",style={'color': colors['tabs']}, value='tab-14'),
    ]),
    html.Div(id='tabs-example-content-1'),

])

@app.callback(
    Output("output", "children"),
    Input("input1", "value"),
)

def find_new(input1):
    try:
        gdp_inc = predict(str(input1))
        return 'US GDP change in the quarter YYYYQ: {} is  {}'.format(input1,gdp_inc)
    except:
        return "Not A valid YYYYQ. Please Try Again"

@app.callback(
    Output('tabs-example-content-1', 'children'),
    Input('tabs-example-1', 'value'),
)

def render_content(tab):
    if tab == 'tab-0':
        return html.Div([
            dcc.Markdown(children = '''
            ## Authors

            Zihan Ye

            Songwen Chen

            Kejia Jin

            Xiaoyang Sheng

            Anqi Sun

            Peter Hevrdejs

            Jeffrey Hatch
            ''',style={'textAlign': 'Left','color': colors['text']}),
            dcc.Markdown(children = '''

            ## Introduction
            The University of Michigan established the Survey Research Center in 1946. The Center has
            conducted a national survey of consumers for over 50 years, consisting of approximately 50 questions involving how consumers view
            their current financial situation, and how they view the general economy in both the short and long term. The data
            from these surveys have been shown to accurately indicate the health of the national economy. For more information please visit
            <https://data.sca.isr.umich.edu/survey-info.php>.

            Link to Example Survey: <https://data.sca.isr.umich.edu/fetchdoc.php?docid=24774>
            ''',style={'textAlign': 'Left','color': colors['text']}),

            # html.A("Link to Umich Consumer Index",href='https://data.sca.isr.umich.edu/survey-info.php',target="_blank"),


            dcc.Markdown(children = '''

            The authors listed above have used the data from the consumer survey as well as data from the world bank
            to evaluate the historic accuracy of these survey data to predict the change in the Gross Domestic Product (GDP) of the
            United States. The following tabs showcase the Exploratory Data Analytics our team used to find these connections.
            Machine learning models were then employed to allow us to predict future trends of the US GDP based on current survey data.

            The data from the survey have been abbreviated. For simplicity, the plots on this website used the same abbreviations.
            The following website provides additional information on each of the abbreviations if desired: <https://data.sca.isr.umich.edu/sda-public/sca/Doc/scafx0.htm>
            ''',style={'textAlign': 'Left','color': colors['text'],"border":"2px"}),
        ])
    if tab == 'tab-1':
        return html.Div([
            dcc.Markdown(children = '''
            ## Consumer Sentiment Indices
            ##### ICS: INDEX OF CONSUMER SENTIMENT
            ##### ICC: INDEX OF CURRENT ECONOMIC CONDITIONS
            ##### ICE: INDEX OF CONSUMER EXPECTATIONS
            '''),

            html.Img(id='csi1', src=listofplot_names[0]),

            dcc.Markdown(children = '''
            Counts of each survey data above grouped by quarter.
            '''),

            html.Img(id='csi2', src=listofplot_names[1]),

            dcc.Markdown(children = '''
            Distribution of the above counts for each survey data above
            '''),

            html.Img(id='csi3', src=listofplot_names[2]),

            dcc.Markdown(children = '''
            Comparison of GDP rate of increase with given survey data
            '''),
        ])
    elif tab == 'tab-2':
        return html.Div([
            dcc.Markdown(children = '''
            ## Personal Finances
            ##### PAGO: PERSONAL FINANCES B/W YEAR AGO
            ##### PEXP: PERSONAL FINANCES B/W NEXT YEAR
            ##### RINC: REAL FAMILY INCOME NEXT 1-2 YEARS
            '''),

            html.Img(id='pf1', src=listofplot_names[3]),

            html.Div('''
            Counts of each survey data above grouped by quarter.
            '''),

            html.Img(id='pf2', src=listofplot_names[4]),

            html.Div('''
            Distribution of the above counts for each survey data above
            '''),

            html.Img(id='pf3', src=listofplot_names[5]),

            dcc.Markdown(children = '''
            Comparison of GDP rate of increase with given survey data
            '''),
        ])
    elif tab == 'tab-3':
        return html.Div([
            dcc.Markdown(children = '''
            ## Political Affiliation
            ##### POLAFF: POLITICAL AFFILIATION
            ##### POLREP: STRONG OR NOT SO STRONG REPUBLICAN
            ##### POLDEM: STRONG OR NOT SO STRONG DEMOCRAT
            ##### POLCRD: CLOSER TO REPUBLICAN OR DEMOCRAT
            '''),

            html.Img(id='pa1', src=listofplot_names[6]),

            html.Div('''
            Counts of each survey data above grouped by quarter.
            '''),

            html.Img(id='pa2', src=listofplot_names[7]),

            html.Div('''
            Distribution of the above counts for each survey data above
            '''),

        ])
    elif tab == 'tab-4':
        return html.Div([
            dcc.Markdown(children = '''
            ## Business Condition
            ##### BAGO: ECONOMY BETTER/WORSE YEAR AGO
            ##### BEXP: ECONOMY BETTER/WORSE NEXT YEAR
            ##### BUS12: ECONOMY GOOD/BAD NEXT YEAR
            ##### BUS5: ECONOMY GOOD/BAD NEXT 5 YEARS
            ##### NEWS1: NEWS HEARD OF CHANGES IN BUS COND (1)
            ##### NEWS2: NEWS HEARD OF CHANGES IN BUS COND (2)
            ##### UNEMP: UNEMPLOYMENT MORE/LESS NEXT YEAR
            ##### GOVT: GOVERNMENT ECONOMIC POLICY
            ##### RATEX: INTEREST RATES UP/DOWN NEXT YEAR
            '''),

            html.Img(id='bc1', src=listofplot_names[8]),

            html.Div('''
            Counts of each survey data above grouped by quarter.
            '''),

            html.Img(id='bc2', src=listofplot_names[9]),
            html.Div('''
            Comparison of GDP rate of increase with given survey data
            '''),

            html.Img(id='bc3', src=bc_heatmap),

            html.Div('''
            Heatmap comparing above survey data and GDP rate of increase
            '''),
        ])
    elif tab == 'tab-5':
        return html.Div([
            dcc.Markdown(children = '''
            ## Inflation Expectations
            ##### PX1Q1: PRICES UP/DOWN NEXT YEAR
            ##### PX1Q2: PRICES PCT UP/DOWN NEXT YEAR
            ##### PX1: PRICE EXPECTATIONS 1YR RECODED
            ##### PX5Q1: PRICES UP/DOWN NEXT 5 YEARS
            ##### PX5Q2: PRICES PCT UP/DOWN NEXT 5 YEARS
            ##### PX5: PRICE EXPECTATIONS 5YR RECODED
            '''),

            html.Img(id='ie1', src=listofplot_names[10]),

            html.Div('''
            Counts of each survey data above grouped by quarter.
            '''),

            html.Img(id='ie2', src=listofplot_names[11]),
            html.Div('''
            Comparison of GDP rate of increase with given survey data
            '''),
        ])
    elif tab == 'tab-6':
        return html.Div([
            dcc.Markdown(children = '''
            ## Demographic Information
            ##### AGE: AGE OF RESPONDENT
            ##### BIRTHM: MONTH OF BIRTH
            ##### BIRTHY: YEAR OF BIRTH
            ##### REGION: REGION OF RESIDENCE
            ##### SEX: SEX OF RESPONDENT
            ##### MARRY: MARITAL STATUS OF RESPONDENT
            ##### NUMKID: NUMBER OF CHILDREN <18 IN HOUSEHOLD
            ##### NUMADT: NUMBER OF ADULTS 18+ IN HOUSEHOLD
            ##### EDUC: EDUCATION OF RESPONDENT
            ##### ECLGRD: EDUCATION: COLLEGE GRADUATE
            ##### EHSGRD: EDUCATION: HIGH SCHOOL GRADUATE
            ##### EGRADE: EDUCATION: HIGHEST GRADE COMPLETED
            '''),

            html.Img(id='demo1', src=listofplot_names[12]),

            html.Div('''
            Counts of each survey data above grouped by quarter.
            '''),

            html.Img(id='demo2', src=listofplot_names[13]),
            html.Div('''
            Comparison of GDP rate of increase with given survey data
            '''),
            html.Img(id='demo3', src=demo_heatmap),

            html.Div('''
            Heatmap comparing above survey data and GDP rate of increase
            '''),

        ])
    elif tab == 'tab-7':
        return html.Div([
            dcc.Markdown(children = '''
            ## Buying Conditions
            ##### DUR: DURABLES BUYING ATTITUDES
            ##### HOM: HOME BUYING ATTITUDES
            ##### CAR: VEHICLE BUYING ATTITUDES
            '''),

            html.Img(id='buyc1', src=listofplot_names[14]),

            html.Div('''
            Counts of each survey data above grouped by quarter.
            '''),

            html.Img(id='buyc2', src=listofplot_names[15]),
            html.Div('''
            Distribution of the above counts for each survey data above
            '''),

            html.Img(id='buyc3', src=listofplot_names[16]),
            html.Div('''
            Comparison of GDP rate of increase with given survey data
            '''),
        ])
    elif tab == 'tab-8':
        return html.Div([
            dcc.Markdown(children ='''
            ## Income Demographics:
            ##### INCOME: :TOTAL HOUSEHOLD INCOME - CURRENT DOLLARS
            '''),

            html.Img(id='id1', src=listofplot_names[17]),

            html.Div('''
            Counts of each survey data above grouped by quarter.
            '''),

            html.Img(id='id2', src=listofplot_names[18]),
            html.Div('''
            Distribution of the above counts for each survey data above
            '''),
            html.Img(id='id3', src=listofplot_names[19]),
            html.Div('''
            Comparison of GDP rate of increase with given survey data
            '''),
        ])
    elif tab == 'tab-9':
        return html.Div([
            dcc.Markdown(children ='''
            ## Wealth Demographics
            ##### HOMEAMT: MARKET VALUE OF HOME
            ##### INVAMT: INVESTMENT VALUE
            '''),

            html.Img(id='wd1', src=listofplot_names[20]),

            html.Div('''
            Counts of each survey data above grouped by quarter.
            '''),

            html.Img(id='wd2', src=listofplot_names[21]),
            html.Div('''
            Distribution of the above counts for each survey data above
            '''),
            html.Img(id='wd3', src=listofplot_names[22]),
            html.Div('''
            Comparison of GDP rate of increase with given survey data
            '''),
        ])
    elif tab == 'tab-10':
        return html.Div([
            dcc.Markdown(children ='''
            ## Vehicle Information
            ##### VEHNUM: NUMBER OF VEHICLES OWNED/LEASED
            '''),

            html.Img(id='veh1', src=listofplot_names[23]),

            html.Div('''
            Average number of vehicles owned/leased by quarter.
            '''),
            html.Img(id='vehhm', src=veh_heatmap),
            html.Div('''
            Heatmap comparing above survey data and GDP rate of increase
            '''),
            # html.Img(id='veh2', src=listofplot_names[24]),

            html.Img(id='veh4', src=listofplot_names[25]),
            html.Div('''
            Comparison of GDP rate of increase with given survey data
            '''),
        ])
    elif tab == 'tab-11':
        return html.Div([
            dcc.Markdown(children ='''
            ## Probabilities
            ##### PINC: CHANCE OF Y INCREASE IN 5 YEARS
            ##### PINC2: PERCENT CHANCE OF INCOME INCREASE
            ##### PJOB: CHANCE WILL LOSE JOB IN 5 YEARS
            ##### PSSA: CHANCE WILL HAVE SOCIAL SECURITY
            ##### PCRY: CHANCE WILL HAVE COMFORTABLE RETIREMENT
            ##### PSTK: PERCENT CHANCE OF INVEST INCREASE 1 YEAR
            '''),

            html.Img(id='prob1', src=listofplot_names[26]),

            html.Div('''
            Counts of each survey data above grouped by quarter.
            '''),
            html.Img(id='probhm', src=prob_heatmap),
            html.Div('''
            Heatmap comparing above survey data and GDP rate of increase
            '''),
        ])
    elif tab == 'tab-12':
        return html.Div([
            dcc.Markdown(children ='''
            ## Gas Expectations
            ##### GASPX2: PERCENT GAS PRICES UP/DOWN 5 YR
            ##### GAS1: GAS PRICE EXPECTATIONS 12 MO RECODED
            ##### GAS1PX2: PERCENT GAS PRICES UP/DOWN 12 MO
            ##### GAS5: GAS PRICE EXPECTATIONS 5 YR RECODED
            ##### GASPX1: GAS PRICES UP/DOWN NEXT 5 YEARS
            ##### GAS1PX1: GAS PRICES UP/DOWN NEXT 12 MONTHS
            '''),

            html.Img(id='gas1', src=listofplot_names[27]),

            html.Div('''
            Distribution of the above counts for each survey data above
            '''),

            html.Img(id='gas2', src=listofplot_names[28]),
            html.Div('''
            Gas price change by year by quarter
            '''),
            html.Img(id='gas3', src=listofplot_names[29]),
            html.Div('''
            Comparison of GDP rate of increase with given survey data
            '''),
            html.Img(id='gas4', src=listofplot_names[30]),
        ])
    elif tab == 'tab-13':
        return html.Div([
            dcc.Markdown(children ='''
            ## Machine Learning GDP Prediction
            We performed an analysis of the data using three different machine learning models, Ridge, Random Forest and XG Boost.
            We wanted to see if we could predict the GDP change using the data from the University of Michigan Survey.
            Below are our results. We have displayed the Mean Stadard Error (MSE) and R2 values for each of these models based on historic trends.
            This allowed us to provide the prediction listed above. You can put in future YYYYQ and see what the change in GDP will be based on current survey data.
            '''),
            dcc.Markdown(children ='''
            ### Ridge Model
            MSE: {}

            R2 value: {}
            '''.format(mserid,r2rid)),
            dcc.Markdown(children ='''
            ### Random Forest Model
            MSE: {}

            R2 value: {}
            '''.format(mserf,r2rf)),
            html.Img(id='rf1', src='https://github.com/jhatch04/STATS-507-Group-Project/blob/main/rf_new.png?raw=true'),
            dcc.Markdown(children ='''
            ### XG Boost Model
            MSE: {}

            R2 value: {}
            '''.format(msexg,r2xg)),
            html.Img(id='xg1', src='https://github.com/jhatch04/STATS-507-Group-Project/blob/main/xg_new.png?raw=true'),
            dcc.Markdown(children ='''
            These plots allowed us to choose the best parameters by which to make our prediciton.
            ''')
    ])
    elif tab == 'tab-14':
        return html.Div([
            dcc.Markdown(children ='''
            ## Conclusions
            After we did the EDA analysis, we select 13 significant variables from the survey data,
            including BUS5, NEWS1, UNEMP, PX1Q1, NUMKID, EGRADE, HOM, CAR, INCOME, VEHNUM, PSSA, PCRY,
            GAS1. Based on these variables, we trained and fitted three machine learning models, which
            are ridge regression, random forest and xgboost. For all the three models, we used validation
            method to come up with the best model parameters under the smaller validation MSE. Then we
            compared the performance of the three models, and Xgboost did the best. Therefore, we use the
            trained Xgboost to predict the future responses using the simulated future survey data. The
            simulation is based on the assumption and the change rate of each survey data variables follow
            a normal distribution, and by calculating the mean and standard deviation from historical survey
            data, we are able to come up with future simulation of them. Upon these simulation results,
            we can use Xgboost to get the prediction of US GDP increase rate in future certain quarters.
            By default, the maximum of future quarters is 12, which means the largest year and quarter is '
            20261',  first quarter in 2026
            '''),
        ])


if __name__ == '__main__':
    app.run_server(debug=True, port=8080)