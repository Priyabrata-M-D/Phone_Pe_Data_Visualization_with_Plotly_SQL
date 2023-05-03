import git, os, json
import pandas as pd

# Cloneing the PhonePe Pulse repository
git.Git('path').clone('https://github.com/PhonePe/pulse.git')

# Getting Data as Dataframes for Agg_Trans
# This is to direct the path to get the data of Agg_Tran

path = "path\\pulse\\data\\aggregated\\transaction\\country\\india\\state\\"
Agg_state_list = os.listdir(path)
Agg_state_list
clm = {'State': [], 'Year': [], 'Quater': [], 'Transaction_type': [], 'Transaction_count': [], 'Transaction_amount': []}
for i in Agg_state_list:
    p_i = path + i + "/"
    Agg_yr = os.listdir(p_i)
    for j in Agg_yr:
        p_j = p_i + j + "/"
        Agg_yr_list = os.listdir(p_j)
        for k in Agg_yr_list:
            p_k = p_j + k
            Data = open(p_k, 'r')
            D = json.load(Data)
            for z in D['data']['transactionData']:
                Name = z['name']
                count = z['paymentInstruments'][0]['count']
                amount = z['paymentInstruments'][0]['amount']
                clm['Transaction_type'].append(Name)
                clm['Transaction_count'].append(count)
                clm['Transaction_amount'].append(amount)
                clm['State'].append(i)
                clm['Year'].append(j)
                clm['Quater'].append(int(k.strip('.json')))
Agg_Trans = pd.DataFrame(clm)

# Getting Data as Dataframes for Top_Trans
path = "path\\pulse\\data\\top\\transaction\\country\\india\\state\\"
Top_state_list = os.listdir(path)
Top_state_list
clm = {'State': [], 'Year': [], 'Quater': [], 'District_name': [], 'Transaction_count': [], 'Transaction_amount': []}
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
                clm['District_name'].append(Name)
                clm['Transaction_count'].append(count)
                clm['Transaction_amount'].append(amount)
                clm['State'].append(i)
                clm['Year'].append(j)
                clm['Quater'].append(int(k.strip('.json')))
Top_Trans = pd.DataFrame(clm)

# Getting Data as Dataframes for Map_Trans
# Similarly Map_Trans
path = "path\\pulse\\data\\map\\transaction\\hover\\country\\india\\state\\"
Map_state_list = os.listdir(path)
Map_state_list
clm = {'State': [], 'Year': [], 'Quater': [], 'District_name': [], 'Transaction_count': [], 'Transaction_amount': []}
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
Map_Trans = pd.DataFrame(clm)

# Getting Data as Dataframes for Agg_User
# Similarly Agg_user
path = "path\\pulse\\data\\aggregated\\user\\country\\india\\state\\"
Agg_state_list = os.listdir(path)
Agg_state_list
clm = {'State': [], 'Year': [], 'Quater': [], 'Device_Brand': [],
       'User_count': [], 'User_percentage': []}
for i in Agg_state_list:
    p_i = path + i + "/"
    Agg_yr = os.listdir(p_i)
    for j in Agg_yr:
        p_j = p_i + j + "/"
        Agg_yr_list = os.listdir(p_j)
        for k in Agg_yr_list:
            p_k = p_j + k
            Data = open(p_k, 'r')
            D = json.load(Data)
            try:
                for z in D['data']['usersByDevice']:
                    Name = z['brand']
                    count = z['count']
                    percentage = z['percentage']
                    clm['Device_Brand'].append(Name)
                    clm['User_count'].append(count)
                    clm['User_percentage'].append(percentage)
                    clm['State'].append(i)
                    clm['Year'].append(j)
                    clm['Quater'].append(int(k.strip('.json')))
            except:
                pass
# Succesfully created a dataframe
Agg_User = pd.DataFrame(clm)
Agg_User.info()

# Getting Data as Dataframes for Top_User

# Similarly Top_User
path = "path\\pulse\\data\\top\\user\\country\\india\\state\\"

Top_state_list = os.listdir(path)
Top_state_list
clm = {'State': [], 'Year': [], 'Quater': [], 'District_name': [], 'Reg_users': [], 'Pincodes': [], 'Reg_users_p': []}
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
                clm['Reg_users_p'].append(Users2)
                clm['Pincodes'].append(name2)
                clm['State'].append(i)
                clm['Year'].append(j)
                clm['Quater'].append(int(k.strip('.json')))
# Succesfully created a dataframe
Top_User = pd.DataFrame(clm)

# Getting Data as Dataframes for Map_User
# Similarly Map_User
path = "path\\pulse\\data\\map\\user\\hover\\country\\india\\state\\"
Map_state_list = os.listdir(path)
Map_state_list

clm = {'State': [], 'Year': [], 'Quater': [], 'District_name': [], 'Reg_User_count': [], 'App_Opened': []}
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
                clm['District_name'].append(Name)
                clm['Reg_User_count'].append(User_count)
                clm['App_Opened'].append(AppOpenCountt)
                clm['State'].append(i)
                clm['Year'].append(j)
                clm['Quater'].append(int(k.strip('.json')))
# Succesfully created a dataframe
Map_User = pd.DataFrame(clm)
