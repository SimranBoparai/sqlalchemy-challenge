Week 10 Assignment

# SQLAlchemy-Challenge

The SQLAlchemy-Challenge will harness the capabilities of SQLAlchemy Python-Pandas, Matplotlib and JSON to analyze and examine precipitation and temperature data of Honolulu, Hawaii. Additionally, you will be required to build a Flask API based on given queries to explore climate trends. 


## Prerequisites

Before working on the SQLAlchemy-Challenge, ensure you complete the following requirements:

- Install VS Code and Python or Jyputer Notebook on your machine 
- Import Pandas, matplotlib, numpy, sqlalchemy, Flask, and datetime 
- Create a new repository called 'sqlalchemy-challenge' in GitHub with README and .gitignore files.


## Repository Setup

Repository Setup:
  - Create a new repository called 'sqlalchemy-challenge' in GitHub with a README file
  - Copy the SSH key in GitHub
  - Navigate into the working directory 
  - Clone SSH key in directory
  - Create a new folder named 'SurfsUp'
    - Import the Starter_Code folder with the climate_starter and app files and the Resources folder  
  - Git add, commit, and push changes into the repository

```
Example:
cd 'sqlalchemy-challenge'
mkdir 'SurfsUp'
cd 'SurfsUp 
git add .
git commit -m "Pushing challenge work"
git push 
```


## Instructions

Ensure you have downloaded the starter code file to start the challenge.

The challenge is separated into two parts:

 - Part 1: Analyze and Explore the Climate Data

    - Precipitation Analysis
    - Station Analysis 

- Part 2: Design Your Climate App 


PART 1: Analyze and Explore the Climate Data

Create a Python and SQLAlchemy script to visualize and conduct basic climate analysis and exploration. Use SQLAlchemy, ORM queries, Pandas, and Matplotlib to complete the following steps.

1. Use SQLAlchemy ```create_engine()``` function to connect to the SQLite database ```hawaii.sqlite```
2. Use the SQLAlchemy ```automap_base()``` function to reflect the tables into classes 
3. Save the classes to variables called ```Measurement``` and ```Station```
4. Create a ```session```

5. Precipitation Analysis: 
   
  - Find the most recent date in the dataset.
  - Use the recent date and retrieve the previous 12 months of precipitation data by queries
  - Perform a query to retrieve the data and precipitation scores and save the results as a Pandas dataframe with accurate column names.
  - Sort the dataframe dates and use Matplotlib to plot the data into a bar chart. 
  - Print the summary statistics for the precipitation data. 

6. Station Analysis: 
   
  - Perform a query to calculate the total number of stations in the dataset.
  - Perform a query to find the most active stations and list the results in descending order.
  - Perform a query to calculate the lowest, highest, and average temperature of the most active station id from the previous query.
  - Perform a query for the last 12 months of temperature observation data for the most active station. 
  - Plot the results from the previous query as a histogram with ```bins=12``` 
  - Close the session


PART 2: Design Your Climate App 

Design a Flask API based on the queries performed in the analysis. Use Flask to create your routes as follows:

1. Create Flask API:
  - Use the 'app.py' file to create various routes for the API.
  - Start at the homepage ```/```
  - List all available routes:
    
        "/api/v1.0/precipitation"
        "/api/v1.0/stations"
        "/api/v1.0/tobs"
        "/api/v1.0/<start>"
        "/api/v1.0/<start>/<end>"

2. Precipitation Route:
  - Return JSON data of precipitation for the last year.
3. Stations Route:
  - Return JSON data of all stations.
4. Temperature Observations (TOBS) Route:
  - Return JSON data for the most active station.
5. Dynamic Route:
  - Return JSON data for the minimum, average, and maximum temperatures for specified start or start-end ranges. 
6. Create a debug code. 
7. Run the Flask app and test the API's. 
    

## Precipitation Analysis Example 

```VS Code
# Find the most recent date in the data set.  
recent_date = session.query(func.max(Measurement.date)).scalar()
recent_date

# Use Pandas to calculate the summary statistics for the precipitation data. 
summary_stats = df.describe()
summary_stats

```

## Station Analysis Example

```VS Code
# Design a query to find the most active stations (i.e., which stations have the most rows?)
# List the stations and their counts in descending order.

active_stations = session.query(Measurement.station, func.count(Measurement.station))\
.group_by(Measurement.station)\
.order_by(func.count(Measurement.station).desc()).all())

active_stations

```

## Flask App Example

```VS Code
# Flask Setup

app = Flask(__name__)

# Flask Routes

@app.route("/")
def welcome():
    return(
        f"All Available Routes:<br/>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/stations<br/>"
        f"/api/v1.0/tobs<br/>"
        f"/api/v1.0/&lt;start&gt;<br/>"
        f"/api/v1.0/&lt;start&gt;/&lt;end&gt;"
    )

```


## Acknowledgements

I want to mention the following individuals and resources for their assistance and support throughout this assignment: 
- Study group members
    - Omid Khan - omidk414@gmail.com - omidk414
    - Evan Wall - - ewall@escoffier.edu - Ewall24
- Class instructor Elias and Class TA Brian
- Xpert Learning Assistant and ChatGPT
- SQLAlchemy Documentation (https://docs.sqlalchemy.org/en/20/)
- Flask Documentation (https://flask.palletsprojects.com/en/3.0.x/)

