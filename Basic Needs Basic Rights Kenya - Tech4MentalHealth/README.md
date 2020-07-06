
# Basic Needs Basic Rights Kenya - Tech4MentalHealth

## Classify text from university students in Kenya towards a mental health chatbot

Around 1 in 4 people will experience a mental health problem this year. Low-income countries have an estimated treatment gap of 85% (as compared with high-income countries with a gap of 35% to 50%). While Kenya has a mental illness prevalence rate that is comparable to that of high-income countries, there are still less than 500 healthcare professionals serving the country.

In Kenya, there are growing concerns about mental health among young people, particularly university students that face a challenging and unique conflation of stressors that put them at risk of challenges like depression and substance abuse.

From the use of app-based solutions for screening to electronically delivered therapies, the use of technologies including machine learning and AI will potentially transform the delivery of mental health services in the coming years.

The objective of this challenge is to develop a machine learning model that classifies statements and questions expressed by university students in Kenya when speaking about the mental health challenges they struggle with. The four categories are depression, suicide, alchoholism, and drug abuse.

This solution will be used for a prototype of a mental health chatbot designed specifically for university students. This initiative is a first step in leveraging technology to make mental health services more accessible and more user-friendly for young people in Kenya and around the world.

### Variable definition:

The data consists of statements and questions expressed by students from multiple universities across Kenya who reported suffering from these different mental health challenges.

The wording of the statements is intended to respond to the prompting question, “What is on your mind?”

Note that the written statements may include some spelling or grammatical errors, as well as slang. Also note that labels were not assigned to the statements, but rather students provided statements and questions about their particular experience.

The labels for the training set are contained in Train.csv, corresponding to one of the four categories of mental health problems (depression, suicide, alchoholism, and drug abuse). Your task is to develop a machine learning model to predict the labels for the test set, following the format in sample_submission.csv.

Files available for download

* Train.csv - has the unique ID of each statement along with the label. You will use this file to train your model on.
* Test.csv - has the unique IDs you will be testing your model on.
* SampleSubmission.csv - is an example of what your submission file should look like. The order of the rows does not matter, but the order of the columns (Depression, Alcohol, Suicide, Drugs) must be the same as the sample submission. Your submission should contain probabilities that the ID is of each category (with values between 0 and 1 inclusive). The values across the columns do not have to add up to 1.

## Leaderboard

* **[Private LB](https://zindi.africa/competitions/basic-needs-basic-rights-kenya-tech4mentalhealth/leaderboard)** : **26rd/454 Rank**

## Solution Link
* **Simple SVM Classifier** [Kaggle V17](https://www.kaggle.com/rajatranjan/basic-needs-zindi-simple) `0.4389`
* **Roberta Base** [Kaggle V15](https://www.kaggle.com/rajatranjan/basic-needs-zindi-simple) `0.331116048638159`
