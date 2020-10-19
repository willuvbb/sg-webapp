import mysql.connector
import pandas as pd

cnx = mysql.connector.connect(user='willuvbb', password='zoedoodle',
                              host='wlc-database-1014.clqcwgm5yctd.us-east-2.rds.amazonaws.com',
                              database='WLC_Database', port = 3306)
cursor = cnx.cursor()

## defining the Query
tweet_query = "SELECT timestamp, tweet, content, emotion, username, followers, location, state FROM AllTweets_WithStates_csv"
## getting records from the table
cursor.execute(tweet_query)
## fetching all records from the 'cursor' object
records = cursor.fetchall()
print(type(records[0]))
print(records[0])

# query from mysql and put in datafrae
tweet_data = pd.read_sql("SELECT timestamp, tweet, content, emotion, username, followers, location, state FROM AllTweets_WithStates_csv", cnx)

pd.set_option('display.expand_frame_repr', False)

# print(tweet_data.head)

# convert dataframe to list of dictionaries (called "tabledata since that's what my old app used...")
tabledata = tweet_data.to_dict('records')
print(tabledata[0])

# now query the State info
## defining the Query

state_data = pd.read_sql("SELECT State, Abbreviation, count FROM StatesWithCounts_csv", cnx)

states = state_data.to_dict('records')
print(states[0])

cursor.close()
cnx.close()