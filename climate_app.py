import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
from flask import Flask, jsonify
engine = create_engine('sqlite:///Resources/hawaii.sqlite')
Base = automap_base()
Base.prepare(engine, reflect=True)
app = Flask(__name__)
@app.route('/')
def home():
    return (
        f"/api/v1.0/precipitation<br/>"
        f'/api/v1.0/stations'
    )
    
app.run()