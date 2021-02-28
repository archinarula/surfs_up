#################################################
# Import Dependencies
#################################################

import pandas as pd
import datetime as dt
import numpy as np

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
from sqlalchemy import extract

from flask import Flask, jsonify

#################################################
# Database Setup
#################################################
engine = create_engine("sqlite:///hawaii.sqlite")

# reflect an existing database into a new model
Base = automap_base()

# reflect the tables
Base.prepare(engine, reflect=True)

# Save reference to the table
Measurement = Base.classes.measurement
Station = Base.classes.station

#create a session link from Python to our database
session=Session(engine)

#################################################
# Flask Setup
#################################################
app = Flask(__name__)


#################################################
# Flask Routes
#################################################
@app.route('/')
def welcome():
    """List all available api routes."""
    return(
        f"Hello World! <br/>"
        f"Welcome to the Climate Analysis API! <br/>"
        f"Available Routes: <br/>"
        f"/api/v1.0/June_stats <br/>"
        f"/api/v1.0/Dec_stats<br/>"
    )

@app.route("/api/v1.0/June_stats")
def June_stats():
   results_june = session.query(Measurement.date, Measurement.tobs).\
       filter(extract ('month', Measurement.date)==6).all()
   tempsj = list(np.ravel(results_june))
   return jsonify(tempsj=tempsj)

@app.route("/api/v1.0/Dec_stats")
def Dec_stats():
   results_dec = session.query(Measurement.date, Measurement.tobs).\
       filter(extract ('month', Measurement.date)==12).all()
   tempsd = list(np.ravel(results_dec))
   return jsonify(tempsd=tempsd)


if __name__ == "__main__":
    app.run(debug=True)