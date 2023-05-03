from dataframes import Agg_Trans, Map_Trans, Top_Trans, Agg_User, Map_User, Top_User
import mysql.connector
from sqlalchemy import create_engine
import pandas as pd

# Connecting to Sql And importing DataFrames
# Dropping databse if exists

connection = mysql.connector.connect(host='localhost', user='root', password='pass123')

# Create a cursor object for executing SQL statements
cursor = connection.cursor()

# Execute the DROP DATABASE statement to delete the database
cursor.execute("DROP DATABASE IF EXISTS project2")
print("Database 'project2' dropped successfully.")

# Close the connection
connection.close()

# Set up a connection to the MySQL server
connection = mysql.connector.connect(host='localhost', user='root', password='pass123')

# Create a cursor object for executing SQL statements
cursor = connection.cursor()

# Create a new database
database_name = 'project2'
cursor.execute(f"CREATE DATABASE IF NOT EXISTS {database_name}")
print(f"Database '{database_name}' created successfully.")
# Select the new database
cursor.execute(f"USE {database_name}")

# Importing data to SQL database
engine = create_engine('mysql+mysqlconnector://root:pass123@localhost/project2', echo=False)
Agg_Trans.to_sql('Agg_Trans', engine)
Top_Trans.to_sql('Top_Trans', engine)
Map_Trans.to_sql('Map_Trans', engine)
Agg_User.to_sql('Agg_User', engine)
Top_User.to_sql('Top_User', engine)
Map_User.to_sql('Map_User', engine)

# Configuring engine to fetch all data
conn = mysql.connector.connect(
  host="localhost",
  user="root",
  password="pass123",
  database="project2"
)
# create an SQLAlchemy engine to use with pandas' to_sql method
engine = create_engine('mysql+mysqlconnector://root:pass123@localhost/project2', echo=False)

# define SQL queries to fetch data from MySQL tables
agg_trans_query = 'SELECT * FROM Agg_Trans'
top_trans_query = 'SELECT * FROM Top_Trans'
map_trans_query = 'SELECT * FROM Map_Trans'
agg_user_query = 'SELECT * FROM Agg_User'
top_user_query = 'SELECT * FROM Top_User'
map_user_query = 'SELECT * FROM Map_User'

# fetch data from MySQL tables into dataframes
agg_trans = pd.read_sql(agg_trans_query, con=conn)
top_trans = pd.read_sql(top_trans_query, con=conn)
map_trans = pd.read_sql(map_trans_query, con=conn)
agg_user = pd.read_sql(agg_user_query, con=conn)
top_user = pd.read_sql(top_user_query, con=conn)
map_user = pd.read_sql(map_user_query, con=conn)
# close the database connection
conn.close()
