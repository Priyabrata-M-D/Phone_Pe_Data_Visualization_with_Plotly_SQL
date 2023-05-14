# PhonePe Pulse Dashboard

This repository contains code for a PhonePe Pulse Dashboard (Repo: (https://github.com/PhonePe/pulse), which allows users to select from a range of options to explore data insights and visualizations related to PhonePe transactions and users from 2018-2022 for every state in India.

## How to Use
1. Install python 3.x and pycharm 2022.x in your system (if installed already ignore the step)
1. Clone this repository to your local machine.
2. Install the required dependencies using `pip install -r requirements.txt`.
3. Run the app by running `streamlit run finalapp.py` in your terminal.
4. Use the dropdown menu to select one of the available options.
5. Explore the data insights and visualizations for the selected option.

## Options (Regarding Available Graphs)

The following options are available for user selection:

1 GEO-VISUALIZATION

    1  Plotlys scatter_geo for plotting districts along with the conent
    2 Plotlys coropleth for drawing the states in India map 
    
2 TRANSACTIONS ANALYSIS

    1 State-wise study
      The above bar graph shows the increasing order of PhonePe Transactions according to the states of India, Here we can observe the top states with the highest Transaction by looking at graph

    2 District-wise study
      User can observe how transactions are happening in districts of a selected state.We can observe the leading distric in a state

    3 Year-wise study   
      We can observe the states with total transactions in particular mode in the selected year

    4 Overall Analysis
    To show how the transactions drastically increased with time

3 USERS ANALYSIS

    1 State-wise study
      User can observe how the App Openings are growing and how Registered users are growing in a state

    2 District-wise study
      User can observe how App Openings are happening in districts of a selected state

    3 Year-wise study   
      User can observe the top leading brands in a particular state in given year

    4 Overall Analysis
      We can see that the Registered Users and App openings are increasing year by year

4 TOP STATES DATA

    1 States with top Registered users
    2 States with top Total Amount Transacted
    3 States with highest Trabsactions count
    4 States with top app openings

## Code
1. Remember to change path (replace 'path' with your own specified path and check 'sql user' and 'password' before running 'finalapp.py'
2. 'Extraction_to_sql.ipynb' contains the code for extraction of data, connection to your sql database and upload dataframes to it
3. `finalapp.py` file contains the code for the Streamlit app, including the dropdown menu and the Plotly figures for each option.

## Data

The data used for this dashboard is not included in this repository. The code assumes that the necessary data is available in the correct format> Please refer to the following link for more information on the required data.
Link : https://github.com/PhonePe/pulse
