# To Vaccinate or Not to Vaccinate: It’s not a Question by #ZindiWeekendz

## Analysing social media sentiment towards vaccines

The data comes from tweets collected and classified through Crowdbreaks.org [Muller, Martin M., and Marcel Salathe. "Crowdbreaks: Tracking Health Trends Using Public Social Media Data and Crowdsourcing." Frontiers in public health 7 (2019).]. Tweets have been classified as pro-vaccine (1), neutral (0) or anti-vaccine (-1). The tweets have had usernames and web addresses removed.

The objective of this challenge is to develop a machine learning model to assess if a twitter post that is related to vaccinations is positive, neutral, or negative.

### Variable definition:

* **tweet_id**: Unique identifier of the tweet
* **safe_tweet**: Text contained in the tweet. Some sensitive information has been removed like usernames and urls
* **label**: Sentiment of the tweet (-1 for negative, 0 for neutral, 1 for positive)
agreement: The tweets were labeled by three people. Agreement indicates the percentage of the three reviewers that agreed on the given label. You may use this column in your training, but agreement data will not be shared for the test set.

**Files available for download are:**

* **Train.csv **- Labelled tweets on which to train your model
* **Test.csv** - Tweets that you must classify using your trained model
* **SampleSubmission.csv** - is an example of what your submission file should look like. The order of the rows does not matter, but the names of the ID must be correct. Values in the 'label' column should range between -1 and 1.

## Leaderboard

* **[Private LB](https://zindi.africa/hackathons/to-vaccinate-or-not-to-vaccinate-its-not-a-question/leaderboard)** : **4th/122 Rank**
