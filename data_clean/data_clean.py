import pandas as pd
import numpy as np

def buying_condition_clean():
    raw_buying = pd.read_csv('Buying conditions.csv', low_memory=False)
    raw_buying.replace(' ', np.nan, inplace=True)
    raw_buying.replace('  ', np.nan, inplace=True)
    raw_buying.replace('   ', np.nan, inplace=True)
    raw_buying.replace('    ', np.nan, inplace=True)
    raw_buying.replace('     ', np.nan, inplace=True)
    raw_buying.replace('      ', np.nan, inplace=True)
    df_buying = raw_buying.groupby('YYYYQ', as_index=False).mean()
    df_buying = df_buying[['YYYYQ', 'DUR', 'HOM', 'CAR']]  # get the three columns DUR, HOM ,CAR
    output_path = 'cleaned_buying_condition.csv'
    df_buying.to_csv(output_path, sep=',', index=False, header=True)

def finance_clean():
    raw_finance = pd.read_csv('Finance.csv', low_memory=False)
    # replace empty string with NaN
    raw_finance.replace(' ', np.nan, inplace=True)
    raw_finance.replace('  ', np.nan, inplace=True)
    raw_finance.replace('   ', np.nan, inplace=True)
    raw_finance.replace('    ', np.nan, inplace=True)
    raw_finance.replace('     ', np.nan, inplace=True)
    raw_finance.replace('      ', np.nan, inplace=True)
    df_finance = raw_finance.groupby('YYYYQ', as_index=False).mean()
    df_finance = df_finance[['YYYYQ', 'PAGO', 'PEXP', 'RINC']]  # get the three columns PAGO, PEXP ,RINC
    output_path = 'cleaned_finance.csv'
    df_finance.to_csv(output_path, sep=',', index=False, header=True)

def gas_clean():
    v = pd.read_csv('GAS PRICE EXPECTATIONS.csv', low_memory=False)
    v = v.loc[(v['YYYY'] <= 2022) & (v['YYYY'] >= 1978)]
    v.replace(r'^\s*$', np.nan, regex=True, inplace=True)
    v = v.astype(float)
    convert_dict = {'YYYYQ': int,
                    'GASPX1': float,
                    'GASPX2': float,
                    'GAS1': float,
                    'GAS1PX1': float,
                    'GAS1PX2': float,
                    'GAS5': float
                    }
    v = v.astype(convert_dict)

    def porpotion(x):
        dic = {}
        for i in x:
            if i not in dic:
                dic[i] = 1
            else:
                dic[i] += 1
        return pd.Series(list(map(lambda x: x / sum(dic.values()), dic.values()))[0])

    v2 = v[['YYYYQ', 'GASPX1', 'GAS1PX1']].groupby('YYYYQ', as_index=False).aggregate(porpotion)

    v3 = v.groupby('YYYYQ', as_index=False).mean()
    v3 = v3[['YYYYQ', 'GASPX2', 'GAS1', 'GAS1PX2', 'GAS5']]
    final_df = pd.concat([v3.set_index('YYYYQ'), v2.set_index('YYYYQ')], axis=1)
    final_df.reset_index(inplace=True)
    output_path = 'cleaned_gase.csv'
    final_df.to_csv(output_path, sep=',', index=False, header=True)


def probability_clean():
    p = pd.read_csv('PROBABILITIES.csv',low_memory=False)
    p = p.loc[(p['YYYY'] <= 2022) & (p['YYYY'] >= 1978)]
    p.replace(r'^\s*$', np.nan, regex=True, inplace=True)
    p1 = p.dropna(subset=list(p.columns[7:-1]), axis=0, how='all')
    p1.drop(['CASEID', 'YYYYMM', 'YYYY', 'ID', 'IDPREV', 'DATEPR'], axis=1, inplace=True)
    type_dict = {'YYYYQ': int,
                 'PINC': float,
                 'PINC2': float,
                 'PJOB': float,
                 'PSSA': float,
                 'PCRY': float,
                 'PSTK': float,
                 'POLAFF': float
                 }
    p1 = p1.astype(type_dict)
    colnames = list(p1.columns[1:])
    for i in colnames:
        df = p1[i]
        df = df.replace([996, 998, 999], [100] * 3, inplace=True)
    p2 = p1.groupby('YYYYQ', as_index=False).agg({'PINC': ['mean'], 'PINC2': ['mean'],
                                                  'PJOB': ['median'], 'PSSA': ['mean'],
                                                  'PCRY': ['mean'], 'PSTK': ['mean']})
    PCN = ['YYYYQ', 'PINC', 'PINC2', 'PJOB', 'PSSA', 'PCRY', 'PSTK']
    p2 = p2.set_axis(PCN, axis=1, inplace=False)
    output_path = 'cleaned_probabilities.csv'
    p2.to_csv(output_path, sep=',', index=False, header=True)

def business_clean():
    raw_business = pd.read_csv("AAKOFmh7.csv", low_memory=False)
    df_business = raw_business[(raw_business['YYYY'] >= 1978) & (raw_business['YYYY'] <= 2022)]
    df_business = df_business.groupby('YYYYQ', as_index=False).mean()
    df_business = df_business[['YYYYQ', 'BAGO', 'BEXP', 'BUS12', 'BUS5', 'NEWS1', 'NEWS2', 'UNEMP', 'GOVT', 'RATEX']]
    output_path = 'cleaned_business_condition.csv'
    df_business.to_csv(output_path, sep=',', index=False, header=True)

def inflation_clean():
    raw_inflation = pd.read_csv("AAEXbYH5.csv", low_memory=False)
    col_list = ['PX1Q1', 'PX1Q2', 'PX1', 'PX5Q1', 'PX5Q2', 'PX5']
    for col in col_list:    # convert the spaces ('   ', ' ') in the data to np.nan
        raw_inflation[col] = raw_inflation[col].astype(str)
        raw_inflation[col] = raw_inflation[col].apply(lambda x: x.strip())
        raw_inflation[col] = raw_inflation[col].replace('', np.nan)
        raw_inflation.loc[pd.notna(raw_inflation[col]), col] = raw_inflation.loc[pd.notna(raw_inflation[col]), col].astype(int)
    raw_inflation.to_csv('AAEXbYH5_converted.csv', sep = ',', index = False, header = True)

    raw_inflation = pd.read_csv("AAEXbYH5_converted.csv", low_memory=False)
    raw_inflation = raw_inflation[(raw_inflation['YYYY'] >= 1978) & (raw_inflation['YYYY'] <= 2022)]
    df_inflation = raw_inflation.groupby('YYYYQ', as_index = False).mean()
    df_inflation = df_inflation[['YYYYQ'] + col_list]

    output_path = 'cleaned_inflation_expectation.csv'
    df_inflation.to_csv(output_path, sep = ',', index = False, header = True)

def clean_demographics(genrep=0):
    # if genrep is low, generate report, else print report to terminal

    # file names (original, cleaned, analaysis)
    csv = "demographics.csv"
    csv_filter_out = "cleaned_demographics_filter.csv"
    csv_analysis_out = "cleaned_demographics_analysis.csv"

    # col types
    type_dict = {'YYYY': int,
                 'AGE': int,
                 'BIRTHM': int,
                 'BIRTHY': int,
                 'REGION': int,
                 'SEX': int,
                 'MARRY': int,
                 'NUMKID': int,
                 'NUMADT': int,
                 'EDUC': int,
                 'ECLGRD': int,
                 'EHSGRD': int,
                 'EGRADE': int
                 }
    colnames = ['CASEID', 'YYYYMM', 'YYYYQ', 'YYYY', 'ID', 'IDPREV', 'DATEPR', 'AGE', 'BIRTHM', 'BIRTHY', 'REGION',
                'SEX', 'MARRY', 'NUMKID', 'NUMADT', 'EDUC', 'ECLGRD', 'EHSGRD', 'EGRADE']

    df = pd.read_csv(csv, names=colnames, low_memory=False)
    df = df.drop(index=0)  # drop first row containing partial headers

    for col in colnames:  # thanks Kejia!
        df[col] = df[col].astype(str)
        df[col] = df[col].apply(lambda x: x.strip())
        df[col] = df[col].replace('', np.nan)
        df.loc[pd.notna(df[col]), col] = df.loc[pd.notna(df[col]), col].astype(int)

    df.drop(['CASEID', 'YYYYMM', 'ID', 'IDPREV', 'DATEPR'], axis=1, inplace=True)  # drop useless cols
    df = df.dropna(axis=0)
    df = df.astype(type_dict)

    # filter valid responses only
    df = df.loc[(df['YYYYQ'] < 20231) & (df['YYYYQ'] > 19774)]
    df = df.loc[(df['AGE'] <= 97) & (df['AGE'] > 17)]  # Age range from 18-97(anyone older is lumped to 97)
    df = df.loc[(df['BIRTHM'] <= 12) & (df['BIRTHM'] > 0)]  # valid range is from 1-12
    df = df.loc[(df['REGION'] <= 4) & (df['REGION'] > 0)]  # valid range from 1-4
    df = df.loc[(df['SEX'] == 2) | (df['SEX'] == 1)]  # 1 or 2 valid
    df = df.loc[(df['MARRY'] <= 5) & (df['MARRY'] > 0)]  # valid range from 1-5
    df = df.loc[(df['EDUC'] <= 6) & (df['EDUC'] > 0)]  # valid range from 1-6
    df = df.loc[(df['EHSGRD'] == 1) | (df['EHSGRD'] == 5) | (df['EHSGRD'] == 8) | (df['EHSGRD'] == 9)]  # 1,5,8,9 valid
    df = df.loc[(df['EGRADE'] <= 24) | (df['EGRADE'] == 98) | (
                df['EGRADE'] == 99)]  # grades 0-24 (assuming long phd), 98,99 valid
    df.drop(['YYYY'], axis=1, inplace=True)
    if genrep == 0:
        df.to_csv(csv_filter_out, sep=',', index=False, header=True)
    df = df.loc[(df['EGRADE'] <= 24)]  # filter for averaging

    
    df_temp = df[['YYYYQ', 'BIRTHM', 'REGION', 'SEX', 'MARRY', 'EDUC', 'ECLGRD', 'EHSGRD']]
    df_mode = df_temp.groupby('YYYYQ', as_index=False).agg({'YYYYQ': lambda x: x.mode()[0],
                                                   'BIRTHM': lambda x: x.mode()[0],
                                                   'REGION': lambda x: x.mode()[0],
                                                   'SEX': lambda x: x.mode()[0],
                                                   'MARRY': lambda x: x.mode()[0],
                                                   'EDUC': lambda x: x.mode()[0],
                                                   'ECLGRD': lambda x: x.mode()[0],
                                                   'EHSGRD': lambda x: x.mode()[0]})
    
    #df_mode = df.groupby('YYYYQ', as_index=False).agg(pd.Series.mode)
    df_mean = df.groupby('YYYYQ', as_index=False).mean().round()
    
    df_mean['YYYYQ'] = df_mean['YYYYQ'].astype(int)
    df_mean['AGE'] = df_mean['AGE'].astype(int)
    df_mean['BIRTHY'] = df_mean['BIRTHY'].astype(int)
    df_mean['NUMKID'] = df_mean['NUMKID'].astype(int)
    df_mean['NUMADT'] = df_mean['NUMADT'].astype(int)
    df_mean['EGRADE'] = df_mean['EGRADE'].astype(int)

    # If the response was a number range, mean was taken. If discrete, mode was used
    df_analysis = pd.DataFrame(
        [df_mean.YYYYQ, df_mean.AGE, df_mode.BIRTHM, df_mean.BIRTHY, df_mode.REGION, df_mode.SEX, df_mode.MARRY,
         df_mean.NUMKID, df_mean.NUMADT, df_mode.EDUC, df_mode.ECLGRD, df_mode.EHSGRD, df_mean.EGRADE]).transpose()
    
    
    if genrep == 0:
        df_analysis.to_csv(csv_analysis_out, sep=',', index=False, header=True)

    else:
        print(f"Here is the cleaned dataframe for demographics:\n\n{df}\n")
        print(f"Here is the analysis dataframe for demographics:\n\n{df_analysis}\n")



def clean_political(genrep=0):
    # file names
    csv = "political.csv"
    csv_filter_out = "cleaned_political_filter.csv"
    csv_analysis_out = "cleaned_political_analysis.csv"

    # col types
    type_dict = {'YYYYQ': int,
                 'POLAFF': float,
                 'POLREP': float,
                 'POLDEM': float,
                 'POLCRD': float
                 }
    colnames = ['CASEID', 'YYYYMM', 'YYYYQ', 'YYYY', 'ID', 'IDPREV', 'DATEPR', 'POLAFF', 'POLREP', 'POLDEM', 'POLCRD']

    df = pd.read_csv(csv, names=colnames, low_memory=False)
    df = df.drop(index=0)  # drop first row containing partial headers

    for col in colnames:  # thanks Kejia!
        df[col] = df[col].astype(str)
        df[col] = df[col].apply(lambda x: x.strip())
        df[col] = df[col].replace('', np.nan)
        df.loc[pd.notna(df[col]), col] = df.loc[pd.notna(df[col]), col].astype(int)

    df.drop(['CASEID', 'YYYYMM', 'ID', 'IDPREV', 'DATEPR'], axis=1, inplace=True)  # drop useless cols
    # df=df.dropna(axis=0)
    #df = df.dropna(thresh=3)  # drops if 3 NaNs - Only two NaN should be present in a row for a given affiliation
    #df = df.dropna(subset=['POLREP', 'POLDEM', 'POLCRD'], inplace=True)
    df = df.dropna(subset=['POLREP', 'POLDEM', 'POLCRD'], how='all')
    df = df.astype(type_dict)
    df = df.loc[(df['YYYYQ'] < 20231) & (df['YYYYQ'] > 19774)]
    df.drop(['YYYY'], axis=1, inplace=True)
    #df_analysis = df.groupby('YYYYQ', as_index=False).agg(pd.Series.mode)
    
    df_analysis = df.groupby('YYYYQ', as_index=False).agg({'YYYYQ': lambda x: x.mode()[0],
                                                   'POLAFF': lambda x: x.mode()[0],
                                                   'POLREP': lambda x: x.mode()[0],
                                                   'POLDEM': lambda x: x.mode()[0],
                                                   'POLCRD': lambda x: x.mode()[0]})
    
    df_analysis['YYYYQ'] = df_analysis['YYYYQ'].astype(int)
    df_analysis['POLAFF'] = df_analysis['POLAFF'].astype(int)
    df_analysis['POLREP'] = df_analysis['POLREP'].astype(int)
    df_analysis['POLDEM'] = df_analysis['POLDEM'].astype(int)
    df_analysis['POLCRD'] = df_analysis['POLCRD'].astype(int)

    if genrep == 0:
        df.to_csv(csv_filter_out, sep=',', index=False, header=True)
        df_analysis.to_csv(csv_analysis_out, sep=',', index=False, header=True)

    else:  # print out
        print(f"Here is the cleaned dataframe for demographics:\n\n{df}\n")
        print(f"Here is the analysis dataframe for demographics:\n\n{df_analysis}\n")
        
        
def income_clean():
    df3 = pd.read_csv("AA6BMOLF.csv", low_memory=False)
    df3 = df3[['YYYYQ', 'INCOME']]
    df3.replace('', np.nan, inplace=True)
    df3.replace(' ', np.nan, inplace=True)
    df3.replace('  ', np.nan, inplace=True)
    df3.replace('   ', np.nan, inplace=True)
    df3.replace('    ', np.nan, inplace=True)
    df3.replace('     ', np.nan, inplace=True)
    df3.replace('      ', np.nan, inplace=True)
    df3 = df3.astype(float)
    convert_dict = {'YYYYQ': int,
                    'INCOME': float
                    }
    df3 = df3.astype(convert_dict)
    df3 = df3.groupby('YYYYQ', as_index=False).mean()
    df3.to_csv("cleaned_income_wealth.csv")

def wealth_clean():
    raw_wealth = pd.read_csv('Wealth.csv', low_memory=False)
    raw_wealth.replace(' ', np.nan, inplace=True)
    raw_wealth.replace('  ', np.nan, inplace=True)
    raw_wealth.replace('   ', np.nan, inplace=True)
    raw_wealth.replace('    ', np.nan, inplace=True)
    raw_wealth.replace('     ', np.nan, inplace=True)
    raw_wealth.replace('      ', np.nan, inplace=True)
    raw_wealth.replace(9999998, np.nan, inplace=True)
    raw_wealth.replace(99999998, np.nan, inplace=True)
    df_wealth = raw_wealth.groupby('YYYYQ', as_index=False).mean()
    df_wealth = df_wealth[['YYYYQ', 'HOMEAMT', 'INVAMT']]
    output_path = 'cleaned_wealth.csv'
    df_wealth.to_csv(output_path, sep=',', index=False, header=True)

def vehicle_clean():
    v = pd.read_csv('Vehicle_Ownership.csv')
    v = v.loc[(v['YYYY'] <= 2022) & (v['YYYY'] >= 1978)]  # need to remove data in year 2023
    v.drop(['YYYY','YYYYMM','IDPREV', 'DATEPR','CASEID','ID'], axis=1, inplace=True)

    v.replace(r'^\s*$', np.nan, regex=True, inplace=True)
    v['VEHOWN'] = v['VEHOWN'].replace(['1', '5', '8', '9'], ['Yes', 'No', np.nan, np.nan])
    v['VEHNUM'] = v['VEHNUM'].replace(['98', '99'], [np.nan, np.nan])
    v.dropna(how='all', subset=['VEHOWN', 'VEHNUM'], inplace=True)
    v['VEHNUM'] = v['VEHNUM'].fillna('0')
    v = v.astype({'YYYYQ': int, 'VEHNUM': int})
    v = v.reset_index(drop=True)
    v1 = v[['YYYYQ','VEHOWN']].copy(deep=True)
    output_path = 'cleaned_vechicle.csv'
    def porpotion(x):
        dic = {}
        for i in x:
            if i not in dic:
                dic[i] = 1
            else:
                dic[i] += 1
        return pd.Series(list(map(lambda x: x / sum(dic.values()), dic.values()))[0])
    yearly_v = v1.groupby('YYYYQ', as_index=False).aggregate(porpotion)
    yearly_v.rename(columns={"VEHOWN": '[Porpotion of Yes]'})
    df2 = v[['YYYYQ','VEHNUM']]
    df2 = df2.groupby('YYYYQ', as_index=False).mean()
    df3 = pd.concat([yearly_v.set_index('YYYYQ'),df2.set_index('YYYYQ')], axis=1)
    df3.reset_index(inplace=True)
    df3.to_csv(output_path, sep=',', index=False, header=True)



def consumer_clean():
    raw_consumer = pd.read_csv('AAiskPal.csv')
    raw_consumer = raw_consumer.loc[(raw_consumer['YYYY'] >= 1978) & (raw_consumer['YYYY'] <= 2022)]
    df_consumer = raw_consumer.groupby('YYYYQ', as_index=False).mean()
    df_consumer = df_consumer.loc[:, ['YYYYQ', 'ICS', 'ICC', 'ICE']]  # get the three columns ICS, ICC ,ICE
    df_consumer = df_consumer.astype(float)
    convert_dict = {'YYYYQ': int,
                    'ICS': float,
                    'ICC': float,
                    'ICE': float
                    }
    df_consumer = df_consumer.astype(convert_dict)  # convert the data type of each column
    output_path = 'cleaned_consumer_sentiment.csv'
    df_consumer.to_csv(output_path, sep=',', index=False, header=True)


def gdp_clean():
    df_gdp = pd.read_csv('GDP.csv')
    df_gdp['gdp_increase_rate'] = df_gdp['GDP'].pct_change()
    df_gdp['DATE'] = pd.to_datetime(df_gdp['DATE'])
    df_gdp['YYYYQ'] = df_gdp['DATE'].dt.year.astype(str) + df_gdp['DATE'].dt.quarter.astype(str)
    convert_dict = {'YYYYQ': int,
                    'GDP': float
                    }
    df_gdp.drop(['DATE'], axis=1, inplace=True)
    df_gdp = df_gdp.astype(convert_dict)
    df_gdp['YYYYQ'] = df_gdp['YYYYQ']
    output_path = 'cleaned_gdp.csv'
    df_gdp.to_csv(output_path, sep=',', index=False, header=True)


def aggregate_data():
    df1 = pd.read_csv('cleaned_buying_condition.csv')
    df2 = pd.read_csv('cleaned_finance.csv')
    df3 = pd.read_csv('cleaned_gase.csv')
    df4 = pd.read_csv('cleaned_probabilities.csv')
    df5 = pd.read_csv('cleaned_business_condition.csv')
    df6 = pd.read_csv('cleaned_inflation_expectation.csv')
    df8 = pd.read_csv('cleaned_demographics_analysis.csv')
    df9 = pd.read_csv('cleaned_wealth.csv')
    df10 = pd.read_csv('cleaned_political_analysis.csv')
    df11 = pd.read_csv('cleaned_income_wealth.csv')
    df12 = pd.read_csv('cleaned_vechicle.csv')
    df13 = pd.read_csv('cleaned_consumer_sentiment.csv')
    df_gdp = pd.read_csv('cleaned_gdp.csv')
    dfs = [df1, df2, df3, df4, df5, df6, df8, df9, df10, df11, df12, df13, df_gdp]

    def using_concat(dfs):
        return pd.concat([df.set_index('YYYYQ') for df in dfs], axis=1)
    final = using_concat(dfs)
    final.reset_index(inplace=True)
    final = final.astype({'YYYYQ': int})
    output_path = 'final_cleaned_data.csv'
    final.to_csv(output_path, sep=',', index=False, header=True)



if __name__ == '__main__':
    buying_condition_clean()
    finance_clean()
    gas_clean()
    probability_clean()
    business_clean()
    inflation_clean()
    clean_demographics()
    clean_political()
    income_clean()
    wealth_clean()
    vehicle_clean()
    consumer_clean()
    gdp_clean()
    aggregate_data()
