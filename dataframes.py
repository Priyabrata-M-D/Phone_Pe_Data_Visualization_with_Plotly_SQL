import mysql.connector
from sqlalchemy import create_engine
#import git
import os
import json
import warnings
from os import walk
from pathlib import Path
import pandas as pd
warnings.filterwarnings("ignore")
# Cloneing the PhonePe Pulse repository (as it is already cloned so commented out)
# git.Git(r'C:\Users\Username\Desktop\Pulse\').clone('https://github.com/PhonePe/pulse.git')

# Aggregated Transaction and User Table
Agg_Trans_Table = pd.DataFrame({})
Agg_Trans_Summary_Table = pd.DataFrame({})


def data_func(state, year, quarter, path):
    global Agg_Trans_Table
    global Agg_Trans_Summary_Table
    ats = pd.read_json(path)

    Agg_Trans_Summary_Table = Agg_Trans_Summary_Table.append(
        {'State': state, 'Year': year, 'Quarter': quarter, 'Data From': ats['data']['from'], 'Data To': ats['data']['to']}, ignore_index=True)

    atd = ats['data']['transactionData']
    if atd:
        for i in atd:
            Agg_Trans_Table = Agg_Trans_Table.append(
                {'Payment Mode': i['name'], 'Total Transactions count': i['paymentInstruments'][0]['count'],
                 'Total Amount': i['paymentInstruments'][0]['amount'], 'Quarter': quarter, 'Year': year, 'State': state}, ignore_index=True)


s = r'path\pulse\data\aggregated\transaction\country\india\state'
s_p = os.listdir(
    r'path\pulse\data\aggregated\transaction\country\india\state')
for i in s_p:
    p = s+'\\'+i
    for j in os.listdir(p):
        p_t = p+'\\'+j
        f1 = []
        for (dirpath, dirnames, filenames) in walk(p_t):
            f1.extend(filenames)
            break
        for k in f1:
            x = p_t+'\\'+k
            y = Path(x).stem
            data_func(i, j, y, x)

Agg_User_Table = pd.DataFrame({})
Agg_User_Summary_Table = pd.DataFrame({})


def data_func2(state, year, quarter, path):

    global Agg_User_Table
    global Agg_User_Summary_Table

    df1 = pd.read_json(path)
    Agg_User_Summary_Table = Agg_User_Summary_Table.append(
        {'State': state, 'Year': year, 'Quarter': quarter, 'Registered Users': df1['data']['aggregated']['registeredUsers'],
         'AppOpenings': df1['data']['aggregated']['appOpens']}, ignore_index=True)

    if df1['data']['usersByDevice']:
        for i in df1['data']['usersByDevice']:
            Agg_User_Table = Agg_User_Table.append(
                {'Brand Name': i['brand'], 'Registered Users Count': i['count'], 'Percentage Share of Brand': i['percentage'],
                 'Quarter': quarter, 'Year': year, 'State': state}, ignore_index=True)


s1 = r'path\pulse\data\aggregated\user\country\india\state'
s1_p = os.listdir(
    r'path\pulse\data\aggregated\user\country\india\state')

for i in s1_p:
    p1 = s1+'\\'+i
    for j in os.listdir(p1):
        p1_t = p1+'\\'+j
        f2 = []
        for (dirpath, dirnames, filenames) in walk(p1_t):
            f2.extend(filenames)
            break
        for k in f2:
            pf = p1_t+'\\'+k
            pn = Path(pf).stem
            data_func2(i, j, pn, pf)

# Map Transaction & User Table

path = r"path\pulse\data\map\transaction\hover\country\india\state\"
Map_state_list = os.listdir(path)
Map_state_list
clm = {'District_name': [], 'Transaction_count': [],
       'Transaction_amount': [], 'Quater': [], 'Year': [], 'State': []}
for i in Map_state_list:
    p_i = path + i + "/"
    Map_yr = os.listdir(p_i)
    for j in Map_yr:
        p_j = p_i + j + "/"
        Map_yr_list = os.listdir(p_j)
        for k in Map_yr_list:
            p_k = p_j + k
            Data = open(p_k, 'r')
            D = json.load(Data)
            for z in D['data']['hoverDataList']:
                Name = z['name']
                count = z['metric'][0]['count']
                amount = z['metric'][0]['amount']
                clm['District_name'].append(Name)
                clm['Transaction_count'].append(count)
                clm['Transaction_amount'].append(amount)
                clm['State'].append(i)
                clm['Year'].append(j)
                clm['Quater'].append(int(k.strip('.json')))


path='path\\pulse\\data\\map\\user\\hover\\country\\india\\state\\'
Map_state_list = os.listdir(path)

clm = {'District Name': [], 'Registered Users Count': [], 'App Openings': [],  'Quater': [],'Year': [],'State': []}
for i in Map_state_list:
    p_i = path + i + "/"
    Map_yr = os.listdir(p_i)
    for j in Map_yr:
        p_j = p_i + j + "/"
        Map_yr_list = os.listdir(p_j)
        for k in Map_yr_list:
            p_k = p_j + k
            Data = open(p_k, 'r')
            D = json.load(Data)
            for districts, z in D['data']['hoverData'].items():
                Name = districts
                User_count = z['registeredUsers']
                AppOpenCountt = z['appOpens']
                clm['District Name'].append(Name)
                clm['Registered Users Count'].append(User_count)
                clm['App Openings'].append(AppOpenCountt)
                clm['State'].append(i)
                clm['Year'].append(j)
                clm['Quater'].append(int(k.strip('.json')))


# Top Transaction & User
path = "path\\pulse\\data\\top\\user\\country\\india\\state\\"

Top_state_list = os.listdir(path)
clm = {'District_name': [], 'Reg_users': [], 'Pincodes': [],
       'Reg_users_pin': [],  'Quater': [], 'Year': [], 'State': []}
for i in Top_state_list:
    p_i = path + i + "/"
    Top_yr = os.listdir(p_i)
    for j in Top_yr:
        p_j = p_i + j + "/"
        Top_yr_list = os.listdir(p_j)
        for k in Top_yr_list:
            p_k = p_j + k
            Data = open(p_k, 'r')
            D = json.load(Data)
            for z in D['data']['districts']:
                name1 = z['name']
                Users1 = z['registeredUsers']
            for a in D['data']['pincodes']:
                name2 = a['name']
                Users2 = a['registeredUsers']
                clm['District_name'].append(name1)
                clm['Reg_users'].append(Users1)
                clm['Reg_users_pin'].append(Users2)
                clm['Pincodes'].append(name2)
                clm['State'].append(i)
                clm['Year'].append(j)
                clm['Quater'].append(int(k.strip('.json')))

path = "path\\pulse\\data\\top\\transaction\\country\\india\\state\\"
Top_state_list = os.listdir(path)
clm = {'District Name': [], 'Transaction count': [],
       'Transaction amount': [],   'Quater': [], 'Year': [], 'State': []}
for i in Top_state_list:
    p_i = path + i + "/"
    Top_yr = os.listdir(p_i)
    for j in Top_yr:
        p_j = p_i + j + "/"
        Top_yr_list = os.listdir(p_j)
        for k in Top_yr_list:
            p_k = p_j + k
            Data = open(p_k, 'r')
            D = json.load(Data)
            for z in D['data']['districts']:
                name = z['entityName']
                count = z['metric']['count']
                amount = z['metric']['amount']
                clm['District Name'].append(name)
                clm['Transaction count'].append(count)
                clm['Transaction amount'].append(amount)
                clm['State'].append(i)
                clm['Year'].append(j)
                clm['Quater'].append(int(k.strip('.json')))
                

Map_Trans_Table = pd.DataFrame(clm)
Mapp_User_Table = pd.DataFrame(clm)
Top_User_Table = pd.DataFrame(clm)
Top_Trans_Table = pd.DataFrame(clm)
Longitude_Latitude_State_Table = pd.read_csv(
    'path\\Data\\Longitude_Latitude_State_Table.csv')
Map_Districts_Longitude_Latitude = pd.read_csv(
    'C:\\Users\\Priyabrata\\Desktop\\Pulse2project\\Data\\Map_Districts_Longitude_Latitude.csv')
Map_IndiaStates_TU=pd.read_csv(
    'path\\Data\\Map_IndiaStates_TU.csv')

conn = mysql.connector.connect(
    host='localhost', user='root', password='root')
cursor = conn.cursor()
cursor.execute("DROP DATABASE IF EXISTS project2")
print("Database 'project2' dropped successfully.")

conn = mysql.connector.connect(
    host='localhost', user='root', password='root')
cursor = conn.cursor()
database_name = 'project2'
cursor.execute(f"CREATE DATABASE IF NOT EXISTS {database_name}")
print(f"Database '{database_name}' created successfully.")
cursor.execute(f"USE {database_name}")

engine = create_engine(
    'mysql+mysqlconnector://root:root@localhost/project2', echo=False)
Agg_Trans_Table.to_sql('data_Agg_Trans_Table', engine)
Agg_Trans_Summary_Table.to_sql('data_Agg_Trans_Summary_Table', engine)
Agg_User_Summary_Table.to_sql('data_Agg_User_Summary_Table', engine)
Agg_User_Table.to_sql('data_Agg_User_Table', engine)
Map_Trans_Table.to_sql('data_Map_Trans_Table', engine)
Mapp_User_Table.to_sql('data_Map_User_Table', engine)
Top_Trans_Table.to_sql('data_Top_Trans_Table', engine)
Top_User_Table.to_sql('data_Top_User_Table', engine)
Longitude_Latitude_State_Table.to_sql(
    'data_Longitude_Latitude_State_Table', engine)
Map_Districts_Longitude_Latitude.to_sql(
    'data_Map_Districts_Longitude_Latitude', engine)
Map_IndiaStates_TU.to_sql('data_Map_IndiaStates_TU',engine)
print('All Tables Uploaded Sucessfully')

Data_Aggregated_Transaction_df = pd.read_sql(
    'SELECT * FROM data_Agg_Trans_Table', con=conn)
Data_Aggregated_User_Summary_df = pd.read_sql(
    'SELECT * FROM data_Agg_User_Summary_Table', con=conn)
Data_Aggregated_User_df = pd.read_sql(
    'SELECT * FROM data_Agg_User_Table', con=conn)
Data_Map_Transaction_df = pd.read_sql(
    'SELECT * FROM data_Map_Trans_Table', con=conn)
Data_Map_User_Table = pd.read_sql(
    'SELECT * FROM data_Map_User_Table', con=conn)
Indian_States = pd.read_sql(
    'SELECT * FROM data_Longitude_Latitude_State_Table', con=conn)
Scatter_Geo_Dataset = pd.read_sql(
    'SELECT * FROM data_Map_Districts_Longitude_Latitude', con=conn)
Coropleth_Dataset=pd.read_sql(
    'SELECT * FROM data_Map_IndiaStates_TU', con=conn)
Data_Aggragated_Transaction_Summary_Table = pd.read_sql(
    'SELECT * FROM data_Agg_Trans_Summary_Table', con=conn)
Data_Top_Transaction_Table = pd.read_sql(
    'SELECT * FROM data_Top_Trans_Table', con=conn)
Data_Top_User_Table = pd.read_sql(
    'SELECT * FROM data_Top_User_Table', con=conn)
