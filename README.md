# PhonePe Pulse Dashboard

## App Link : https://priyabrata-m-d-phone-pe-data-visualization-with-finalapp-0ipr3j.streamlit.app/
## App Video :
This repository contains code for a PhonePe Pulse Dashboard which allows users to select from a range of options to explore data insights and visualizations related to PhonePe transactions and users from 2018-2022 for every state in India.

## How to Use
1. Install python 3.x and pycharm 2022.x in your system (if installed already ignore the step)
1. Clone this repository to your local machine.
2. Install the required dependencies using `pip install -r requirements.txt`.
3. Run the app by running `streamlit run finalapp.py` in your terminal.
4. Use the dropdown menu to select one of the available options.
5. Explore the data insights and visualizations for selected options.

## What to Visualize??

The following options can be visualized:
- Transaction Type by Year and Quarter
- District-level Analysis of Transactions
- Insights on Transaction Count and Amount by State in India
- Quarterly Transaction Amount Trends in India
- Quarterly Transaction Count Trends in India
- Top Registered Users by State
- Device Brand Loyalty Over Time
- PhonePe User Adoption over Year and across States
- Device Brands Popularity Among PhonePe Users
- Registered Users Over Time
- State-level Analysis of Registered Users
- State-wise App Engagement: A deep dive into App Opened data
- Top Performing States

## Code
1. Remember to change path (replace 'path' with your own specified path and check 'sql user' and 'password' before running 'finalapp.py'
2. 'dataframes.py' contains the code for extraction of data, connection to your sql database and upload dataframes to it
3. `finalapp.py` file contains the code for the Streamlit app, including the dropdown menu and the Plotly figures for each option.

## Data

The data used for this dashboard is not included in this repository. The code assumes that the necessary data is available in the correct format> Please refer to the following link for more information on the required data.
Link : https://github.com/PhonePe/pulse
