# import pandas package
import pandas as pd

# read the airbnb NYC listings csv file
airbnb = pd.read_csv("listings.csv")



airbnb.head() #to view the first entries in the dataframe
airbnb.tail() #to view the last entries in the dataframe
airbnb["name"] #to get the results from a single column
airbnb[["host_id", "host_name"]] #to get the results for multiple columns
airbnb.dtypes #Show the data types for each column
airbnb["last_review"] = pd.to_datetime(airbnb["last_review"]) # Change the type of a column to datetime
airbnb['year'] = airbnb['last_review'].dt.year # extract the year from a datetime series
airbnb['name'] = airbnb['name'].str.strip() # Strip leading and trailing spaces from a string series
airbnb['name_lower'] = airbnb['name'].str.lower() # lowercase all strings in a series
airbnb['min_revenue'] = airbnb['minimum_nights'] * airbnb['price']  # calculate using two columns 
airbnb['price'].mean() # get the mean price
airbnb['price'].median() # get the median price
airbnb[['room_type', 'price']].groupby('room_type', as_index=False).mean() # get the mean grouped by type of room
airbnb[['room_type', 'price']].groupby('room_type', as_index=False).median() # get the median grouped by type of room
airbnb[['room_type', 'year', 'price']].groupby(['room_type', 'year'], as_index=False).median() # get the median grouped by type of room and year
airbnb_under_1000 = airbnb[airbnb['price'] < 1000] # get all rows with price < 1000
airbnb_2019_under_1000 = airbnb[(airbnb['price'] < 1000) & (airbnb['year'] == 2020)] # get all rows with price < 1000 and year equal to 2020
ax = airbnb_under_1000['price'].plot.hist(bins=40) # distribution of prices under $1000
print(airbnb) 