# Weather Data System

In this project, We are collecting the weather data from *2006* to *2014* in a file and we extracting these different data files in Data Folder. To make our data meaningful, we are removing the redundant and meaningless data. We are storing the meaningful data for each year in a .csv file and then we merge all these files to create a combined report . Basically, we are making Weather Report for years 2006-2014 and combining the meaningful data.


In this project i am collecting data from [CCAT Weather data](http://www.submm.caltech.edu/submm.org/site/weather/) Website by scrapping through BeautifulSoup library 

In `Download.py` I have scrapped data from above website and stored in [Data folder](data/) directory . But this data is in different file . we need to combine this data and make it meaningful So i am merging all data in single csv [merge_data csv file](ccat_site_weather_data_2006_to_2014.csv) file 


## How To run this Project
`git clone https://github.com/olgaarkadieva/weather-data-merge.git`
`cd weather-data-merge`

Run  `pip install -r requirements.txt`
 in console or terminal to install all the dependencies

1. `first run download.py file`

2. `after that run merge_data.py file`

That's all.

### If you want to improve this project by contributing:

1. Fork the repository
2. Make changes
3. Create a Pull Request.

