import plotly.express as px, streamlit as st
from sqlconn import agg_user, agg_trans, top_trans, top_user, map_user, map_trans

# define dropdown options for user selection
options = ['Transaction Type by Year and Quarter', 'District-level Analysis of Transactions',
           'Insights on Transaction Count and Amount by State in India', 'Quarterly Transaction Amount Trends in India',
           'Quarterly Transaction Count Trends in India', 'Top Registered Users by State',
           'Device Brand Loyalty Over Time',
           'PhonePe User Adoption over Year and across States', 'Device Brands Popularity Among PhonePe Users',
           'Registered Users Over Time', 'State-level Analysis of Registered Users',
           'State-wise App Engagement: A deep dive into App Opened data']

# create Streamlit app
st.title('Phonepe Pulse Dashboard')
selected_option = st.selectbox('Select an option', options, label_visibility="visible")
# define Plotly figure based on selected option
if selected_option == 'State level Analysis of mode of Transactions':
    agg_trans_unique = agg_trans.groupby(['Transaction_type', 'Year'], as_index=False)['Transaction_count'].sum()
    fig = px.imshow(agg_trans_unique.pivot(index='Transaction_type', columns='Year', values='Transaction_count'),
                    x=agg_trans_unique['Year'].unique(), y=agg_trans_unique['Transaction_type'].unique(),
                    color_continuous_scale='Blues', title='State level Analysis of mode of Transactions')

elif selected_option == 'District-level Analysis of Transactions':
    fig = px.histogram(top_trans, x='Year', y=['Transaction_count'], barmode='stack',
                       color='Year', title='District-level Analysis of Transactions')

elif selected_option == 'Insights on Transaction Count and Amount by State in India':
    fig = px.bar(map_trans, x='State', y=['Transaction_count', 'Transaction_amount'], barmode='stack',
                 title='Insights on Transaction Count and Amount by State in India')

elif selected_option == 'Quarterly Transaction Amount Trends in India':
    map_trans_unique = map_trans.groupby(['Year', 'Quater'], as_index=False)['Transaction_amount'].sum()
    fig = px.imshow(map_trans_unique.pivot(index='Year', columns='Quater', values='Transaction_amount'),
                    x=map_trans_unique['Quater'].unique(), y=map_trans_unique['Year'].unique(),
                    color_continuous_scale='Blues', title='Quarterly Transaction Amount Trends in India')

elif selected_option == 'Quarterly Transaction Count Trends in India':
    map_trans_unique = map_trans.groupby(['Year', 'Quater'], as_index=False)['Transaction_count'].sum()
    fig = px.imshow(map_trans_unique.pivot(index='Year', columns='Quater', values='Transaction_count'),
                    x=map_trans_unique['Quater'].unique(), y=map_trans_unique['Year'].unique(),
                    color_continuous_scale='Reds', title='Quarterly Transaction Count Trends in India')

elif selected_option == 'Top Registered Users by State':
    fig = px.line(top_user, x='State', y='Reg_users',
                  title='Top Registered Users by State')

elif selected_option == 'Device Brand Loyalty Over Time':
    fig = px.pie(agg_user, names='Device_Brand', values='Year',
                 title='Device Brand Loyalty Over Time')

elif selected_option == 'PhonePe User Adoption over Year and across States':
    fig = px.bar(agg_user, x='User_percentage', y='Year', color='State',
                 title='PhonePe User Adoption over Year and across States')

elif selected_option == 'Device Brands Popularity Among PhonePe Users':
    fig = px.bar(agg_user, x='Device_Brand', y='User_count',
                 title='Device Brands Popularity Among PhonePe Users')

elif selected_option == 'Registered Users Over Time':
    map_user_unique = map_user.groupby(['Year', 'Quater'], as_index=False)['Reg_User_count'].sum()
    fig = px.imshow(map_user_unique.pivot(index='Year', columns='Quater', values='Reg_User_count'),
                    x=map_user_unique['Quater'].unique(), y=map_user_unique['Year'].unique(),
                    color_continuous_scale='Blues', title='Registered Users Over Time')

elif selected_option == 'State-level Analysis of Registered Users':
    fig = px.histogram(map_user, x='State', y=['Reg_User_count'], barmode='stack',
                       color='Year', title='State-level Analysis of Registered Users')

elif selected_option == 'State-wise App Engagement: A deep dive into App Opened data':
    fig = px.bar(map_user, x='State', y=['App_Opened'], barmode='stack',
                 color='Year', title='State-wise App Engagement: A deep dive into App Opened data')

# display the Plotly figure in Streamlit
st.plotly_chart(fig.show())