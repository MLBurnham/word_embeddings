# Measuring ideology via word embeddings

This project is exploring the use of word embeddings to measure ideology.
For my test case I'm using twitter data from US congress members as well as the Russian Troll Tweet Dataset found here: https://github.com/fivethirtyeight/russian-troll-tweets

## To do:
0. Configure environment

    - [x] Init git repo
    - [ ] Init remote repo
    - [ ] Set up virtual env
    - [x] Create README.md
    

1. Get list of all congess members
    - [x] Get keys and access tokens
    - [x] Put keys/tokens in a file
    - [x] Pull cspan list: https://twitter.com/cspan/lists/members-of-congress/members?lang=en


2. scrape meta data for congress members

    - [x] Fields: screen name, user id, about, party, gender, district

3. Create listener to stream data
    - [x] Filter for original tweets
    - [x] Test and execute
    - [ ] Stream data to csv
    - [ ] Clean up encoding/emoji

4. Create script to request from REST API
    - [x] function to pull the data. Pull max 200 tweets or pull from most recent.
    - [x] function to subset returned tweets to original tweets.
    - [x] function to extract tweets from data and convert to dataframe
    - [x] group functions into class
    - [x] write to csv with twitter id
    - [x] Loop through all members
    - [x] Convert from notebook to modules
    - [ ] Automate daily pull

3. Get troll data