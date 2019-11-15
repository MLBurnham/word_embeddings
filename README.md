# Measuring ideology via word embeddings
This project is exploring the use of word embeddings to measure ideology.
For my test case I'm using twitter data from US congress members as well as the Russian Troll Tweet Dataset found here: https://github.com/fivethirtyeight/russian-troll-tweets

## To do:
0. Configure environment

    - [x] Init git repo
    - [ ] Init remote repo
    - [ ] Set up virtual env
    - [x] Create README.md
    - [ ] Ensure reproducability of scripts
    

1. Get list of all congess members
    - [x] Get keys and access tokens
    - [x] Put keys/tokens in a file
    - [x] Pull cspan list: 


2. scrape meta data for congress members

    - [x] Fields: screen name, user id, about, 
    - [x] mandually add: party, gender, district

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

5. Clean twitter data
    - [ ] Merge meta data with text data
    - [x] Convert date strings to datetime and subset to date range
    - [ ] Examine lemmas for key political words
    - [ ] Recode PrepDocs class
    
6. Get list of key words
    - [x] Create initial list of 100
    - [ ] Revise list based on lemmas

7. Get troll data


## Sources:
### Data:
Congressional meta data: https://github.com/unitedstates/congress-legislators
CSPAN list of congress memebers on twitter: https://twitter.com/cspan/lists/members-of-congress/members?lang=en
Russian troll tweets: https://github.com/fivethirtyeight/russian-troll-tweets

### Packages:
Speed reader package: https://github.com/matthewjdenny/SpeedReader

### Lit:
Fightin words: https://www.cambridge.org/core/services/aop-cambridge-core/content/view/81B3703230D21620B81EB6E2266C7A66/S1047198700002291a.pdf/div-class-title-fightinandapos-words-lexical-feature-selection-and-evaluation-for-identifying-the-content-of-political-conflict-div.pdf
word2vec: https://code.google.com/archive/p/word2vec/
word2vec explained: https://arxiv.org/pdf/1402.3722.pdf
Diachronic word embeddings: https://arxiv.org/pdf/1605.09096.pdf
Words are Malleable: https://arxiv.org/pdf/1711.05603.pdf

