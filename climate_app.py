# import dependencies
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
from flask import Flask, jsonify
import datetime as dt
engine = create_engine('sqlite:///Resources/hawaii.sqlite')
Base = automap_base()
Base.prepare(engine, reflect=True)
Measurement = Base.classes.measurement
Station = Base.classes.station
app = Flask(__name__)
@app.route('/')
def home():
    return (
        f'Available routes<br/>'
        f"/api/v1.0/precipitation<br/>"
        f'/api/v1.0/stations<br/>'
        f'/api/v1.0/tobs<br/>'
        f'/api/v1.0/&ltstart&gt<br/>'
        f'/api/v1.0/&ltstart&gt/&ltend&gt<br/>'
        f'*&ltstart&gt and &ltend&gt should be between 2010-01-01 and 2017-08-23 in the form of YYYY-MM-DD '
    )
@app.route('/api/v1.0/precipitation')
def prcp():
    session=Session(engine)
    dp_dict={}
    results=session.query(Measurement.date,func.avg(Measurement.prcp)).group_by(Measurement.date).all()
    session.close
# results return a list of tuples. result is an element of results, thus, a tuple. 
# exact items in a tuple and add to the empty dictionary created above.
    for result in results:
        (date, prcp)=result
        dp_dict[date]=prcp
    return jsonify(dp_dict)

@app.route('/api/v1.0/stations')
def station():
    session=Session(engine)
    st_dict={}
    results=session.query(Station.station, Station.name).all()
    session.close
    for result in results:
        (st_no,name)=result
        st_dict[st_no]=name
    return jsonify(st_dict)

@app.route('/api/v1.0/tobs')
def tobs():
    session=Session(engine)
    dt_dict={}
    start_date=dt.date(2017,8,23)-dt.timedelta(days=365)
    results=session.query(Measurement.date, func.avg(Measurement.tobs)).\
            filter(Measurement.date>=start_date).\
            filter(Measurement.date<='2017-08-23').\
            group_by(Measurement.date).all()
    session.close
    for result in results:
        (date, tobs)=result
        dt_dict[date]=tobs
    return jsonify(dt_dict)

@app.route('/api/v1.0/<start>')
def summary(start):
    session=Session(engine)
    s_dict={}
    results=session.query(func.min(Measurement.tobs),func.avg(Measurement.tobs),func.max(Measurement.tobs)).\
            filter(Measurement.date>=start).all()
    session.close
    for i in results:
        (min, avg, max)=i
        s_dict['Min Temp']=min
        s_dict['Avg Temp']=avg
        s_dict['Max Temp']=max
    return jsonify(s_dict)

@app.route('/api/v1.0/<start>/<end>')
def cal(start,end):
    session=Session(engine)
    s_dict={}
    results=session.query(func.min(Measurement.tobs),func.avg(Measurement.tobs),func.max(Measurement.tobs)).\
            filter(Measurement.date>=start).\
            filter(Measurement.date<=end).all()
    session.close
    for i in results:
        (min, avg, max)=i
        s_dict['Min Temp']=min
        s_dict['Avg Temp']=avg
        s_dict['Max Temp']=max
    return jsonify(s_dict)
app.run()