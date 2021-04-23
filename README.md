# FinalProject
This is a simple data visualization project that used my Top Songs of 2020 retrived from Spotify's API. That data was then used to make a scatter plot and kmeans cluster to see correlations in the data

# functions
This folder contains three functions. The audioanalysis.py file uses the Spotify API to retrive the data of one (1) playlist and stores it in a .csv file. This .csv file will have 50 entries but if you would like to capture more data, you can use loops.

# data
This is the .csv file created from running the audioanalysis.py. You can link to it by saving the url as a variable and using df.read_csv(url). You can also run the audioanalysis script with your own code and then save your own .csv. 

# proof
PNG files that show what will be produced with a proper running of the scripts. 

# references
The following are example projects used to craft this one:
https://medium.com/analytics-vidhya/analyzing-spotify-dataset-with-python-6ba9cb82a486
https://towardsdatascience.com/analysis-of-top-50-spotify-songs-using-python-5a278dee980c
