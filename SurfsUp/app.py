# Import the dependencies.
import numpy as np

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify
import datetime as dt

#################################################
# Database Setup
#################################################

# Create engine using the `hawaii.sqlite` database file
engine = create_engine("sqlite:///Resources/hawaii.sqlite")

# Declare a Base using `automap_base()`
Base = automap_base()

# Use the Base class to reflect the database tables
Base.prepare(autoload_with=engine)

# Assign the measurement class to a variable called `Measurement` and
# the station class to a variable called `Station`
Measurement = Base.classes.measurement
Station = Base.classes.station 

# Create a session
session = Session(engine)

#################################################
# Flask Setup
#################################################
app = Flask(__name__)

#################################################
# Flask Routes
#################################################
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

# Route for Precipitation
@app.route("/api/v1.0/precipitation")
def precipitation():
    session = Session(engine)
    one_year = dt.date(2017,8,23) - dt.timedelta(days=365)
    scores = session.query(Measurement.date, Measurement.prcp).filter(Measurement.date >= one_year).all()

    session.close() 

    precipitation_dict = list(np.ravel(scores))
    return jsonify(precipitation_dict)

# Route for Stations
@app.route("/api/v1.0/stations")
def stations():
    session = Session(engine)
    stations_data = session.query(Station.station).all()

    session.close()

    stations_list = list(np.ravel(stations_data))
    return jsonify(stations_list)

# Route for Tobs
@app.route("/api/v1.0/tobs")
def tobs():
    session = Session(engine)
    one_year = dt.date(2017,8,23) - dt.timedelta(days=365)
    observed_temperature = session.query(Measurement.date, Measurement.tobs)\
    .filter(Measurement.station == 'USC00519281')\
    .filter(Measurement.date >= one_year).all()

    session.close()

    observed_temps = list(np.ravel(observed_temperature))
    return jsonify(observed_temps)

# Routes for 'start' and 'end' API's
@app.route("/api/v1.0/<start>")
@app.route("/api/v1.0/<start>/<end>")
def temperature(start=None, end=None):
    session = Session(engine)
    select = [func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)]
    if not end:
        results = session.query(*select).filter(Measurement.date <= start).all()

        session.close()

        temps_result = list(np.ravel(results))
        return jsonify(temps_result)

# Debug statements
if __name__ == '__main__':
    app.run(debug=True)