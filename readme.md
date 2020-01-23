![hawaii](https://cdn.travelpulse.com/images/54aaedf4-a957-df11-b491-006073e71405/ee952e9e-f09c-49c2-bc5d-4303c880173a/630x355.jpg)
# *__CLIMATE ANALYSIS OF HAWAII__*
## Background
Use Python (Pandas, and Matplotlib) and SQLAlchemy (ORM queries) to conduct basic climate analysis and data exploration of Hawaii climate database.
## Tools

## Objectives
1. Climate analysis and exploration
* Precipitation Analysis
* Station Analysis
* Temperature Analysis
2. Climate App
* Design a Flask API based on the queries that have just developed.
* Routes
  * `/`
    * Home page.
    * List all routes that are available.
  * `/api/v1.0/precipitation`
    * Convert the query results to a Dictionary using date as the key and prcp as the value.
    * Return the JSON representation of your dictionary.
  * `/api/v1.0/stations`
    * Return a JSON list of stations from the dataset.
  * `/api/v1.0/tobs`
	* query for the dates and temperature observations from a year from the last data point.
	* Return a JSON list of Temperature Observations (tobs) for the previous year.
  * `/api/v1.0/<start>` and `/api/v1.0/<start>/<end>`
	* Return a JSON list of the minimum temperature, the average temperature, and the max temperature for a given start or start-end range.
	* When given the start only, calculate `TMIN`, `TAVG`, and `TMAX` for all dates greater than and equal to the start date.
	* When given the start and the end date, calculate the `TMIN`, `TAVG`, and `TMAX` for dates between the start and end date inclusive.

## Results
1. Precipitation Analysis

   ![prcp vs date](Images/Daily_Precipitation_in_Hawaii_last_12_months.png)

2. Station Analysis

   ![histogram](Images/histogram.png)


3. Temperature Analysis I

     | Test           | P value                | 
     | -------------  |:----------------------:| 
     | Paired T test  | 6.580289883689127e-41  | 

    Paire T test was used to comopare June and December temperatures in Hawaii. The mean of all measurements at all stations was used to represent daily tempperature. Because we were comparing two measurements of one spot at different times, which fits the definition of a paried T test. P value is less than 0.05 indicating a significant difference existed between tempratures in June and December.

4. Temperature Analysis II

    ![barplot](Images/avg_temp_barplot.png)

    ![areaplot](Images/est_temp_vaction.png)

5. Climate App
* `/`
  ![main](Images/app_images/main.png)
* `/api/v1.0/precipitation`
  ![preci](Images/app_images/precipitation.png)
* `/api/v1.0/stations`
   ![station](Images/app_images/station.png) 
* `/api/v1.0/tobs`
	![tobs](Images/app_images/tobs.png)
* `/api/v1.0/<start>` 
  ![start](Images/app_images/start.png)
* `/api/v1.0/<start>/<end>`
  ![start_end](Images/app_images/start_end.png)
	

