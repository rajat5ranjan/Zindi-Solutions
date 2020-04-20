# Spot the Mask Challenge by #ZindiWeekendz

## Can you predict whether a person in an image is wearing a face mask? #masks4all

Face masks have become a common public sight in the last few months. The Centers for Disease Control (CDC) recently advised the use of simple cloth face coverings to slow the spread of the virus and help people who may have the virus and do not know it from transmitting it to others. Wearing masks is broadly recognised as critical to reducing community transmission and limiting touching of the face.

In a time of concerns about slowing the transmission of COVID-19, increased surveillance combined with AI solutions can improve monitoring and reduce the human effort needed to limit the spread of this disease. The objective of this challenge is to create an image classification machine learning model to accurately predict the likelihood that an image contains a person wearing a face mask, or not. The total dataset contains 1,800+ images of people either wearing masks or not.

Your machine learning solution will help policymakers, law enforcement, hospitals, and even commercial businesses ensure that masks are being worn appropriately in public. These solutions can help in the battle to reduce community transmission of COVID-19.

### Variables
The data have been split into a test and training set. The training set contains ~1300 images and the test set contains 509 images. There are two types of images in this dataset, people or images with face masks and people or images without.

Your task is to provide the probability that an image contains at least one mask. For each unique image ID you should estimate the likelihood that the image contains at least one mask, with an estimated probability value between 0 and 1.

The files you have for download here are:
* **images.zip** (~193mb): zip file containing all the images, train and test images. You will need to use train_labels.csv to split the data into the train and test sets.
* **train_labels.csv**: This is the list of images in the train set, 1 indicates an image with a person with a mask, 0 indicates a person without a mask.
* **sample_submission.csv**: is an example of what your submission file should look like, including a list of unique image IDs. Your submission file should have all of the Image IDs in this file along with estimates of the corresponding probabilities of observing a person with a mask.

## Leaderboard

* **[Private LB](https://zindi.africa/hackathons/spot-the-mask-challenge/leaderboard)** : **24th/136 Rank**
