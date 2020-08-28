# Weather Data System

In this project, We are collecting the weather data from *2006* to *2014* in a file and we extracting these different data files in Data Folder. To make our data meaningful, we are removing the redundant and meaningless data. We are storing the meaningful data for each year in a .csv file and then we merge all these files to create a combined report . Basically, we are making Weather Report for years 2006-2014 and combining the meaningful data.


In this project i am collecting data from [CCAT Weather data](http://www.submm.caltech.edu/submm.org/site/weather/) website by scrapping through BeautifulSoup library 

in Download.py i have scrapped data from above wesbite and stored in [Data folder](data/) directory . But this data is in different file . we need to combine this data and make it meaningful So i am merging all data in single csv [merge_data csv file](ccat_site_weather_data_2006_to_2014.csv) file 


## How To run this Project

To install all the dependencies just write "pip install -r requirements.txt" in console or terminal


first run download.py file 

after that run merge_data.py file 






