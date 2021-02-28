# Written Analysis of the Surfs_up challenge Module 9

## Overview of Analysis
W.Avy is the prospective investor interested to open up a Surf and Icecream shop is island of Oahu, Hawaii. Before taking the final decision he wants to analyze the tempreture trends for the months of June and December to unders the overall sustainability on this investment decision. Using Python, Pandas, SQLite, SQLAlchemy we can use the weather data from the stations to provide meaningful insights to our investor. 

Data Source: hawaii.sqlite

## Deliverable/Results: This analysis consists of two technical analysis deliverables and this written report:

Deliverable 1: Summary Statistics for June
https://github.com/archinarula/surfs_up/blob/main/Challenge%20files/SurfsUp_Challenge.ipynb

Deliverable 2: Summary Statistics for December
https://github.com/archinarula/surfs_up/blob/main/Challenge%20files/SurfsUp_Challenge.ipynb

Deliverable 3: Written report for the Statistical analysis 
<insert link>


## Results

- June temperatures are higher(avg=74.9 degF) than December (avg=71.04 degF)
- June station activity is also higher than December
- Min temperatures in Dec is lower than June but not so low and still great for surfing and icecreams shop business
-50% of June and December temperatures are above 70 degF (75 degF for June and 71 for Dec) which is a reliable indicator that surf shop business has good sustainability prospects in Oahu


<change this image link>   ![moviesQuery](/Resources/movies_query.png)



## Results
Temperature trends analysis from June and Dec show that surf shop business is sustainable in Oahu and W. Avy can proceed with investment decisions.

Few additional queries can provide him with more details around precipitation and station activity for June and December to further strengthen this analysis

- Total precipitation for June and December
addresults1= session.query(Measurement.date, Measurement.prcp).filter(extract('month', Measurement.date) == 6).all()
addresults2= session.query(Measurement.date, Measurement.prcp).filter(extract('month', Measurement.date) == 12).all()

- Precipitation at most active station for June and December
addresults3= session.query(Measurement.prcp).filter(Measurement.station == 'USC00519281').filter(extract('month', Measurement.date) == 6).all()
addresults4= session.query(Measurement.prcp).filter(Measurement.station == 'USC00519281').filter(extract('month', Measurement.date) == 12).all()
