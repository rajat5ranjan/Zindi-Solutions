# SANSA AWS Informal Settlements in South Africa by #ZindiWeekendz

## Use high resolution satellite imagery from urban South Africa to identify the locations of informal settlements

During the COVID-19 crisis, it is more critical than ever for governments to be able to identify the locations of informal settlements. Knowing where informal settlements are located will help governments make more appropriate policies and ensure that all people have access to the services they need. Satellite imagery can help do this at scale across the country.

The South African National Space Agency (SANSA) collects high-resolution satellite imagery from a number of international earth observation satellites. A machine learning model trained on this imagery would help SANSA to locate informal settlements more efficiently, providing the South African government with up-to-date information about the location and size of informal settlements.

In this hackathon, you’re invited to use SANSA’s high-resolution satellite imagery to develop a machine learning model to identify whether an image of an area in South Africa contains informal settlements or not. All participants will use Amazon AWS virtual machines (VMs) to access the data and do all their work during the hackathon.

Only 300 data scientists will be able to participate in this hackathon.

The hackathon opens on Friday 12 June 2020 12:00 GMT.

### Variable definition:

The goal of this competition is to classify imagery at different locations, predicting whether a given location is within an informal settlement (1) or not (0). The imagery is 1.5m resolution SPOT imagery, covering the areas of interest. Both the imagery and the labels are from 2017.

Files available for download

* **Train.csv** - contains locations and the associated label (1 for informal settlements). The starter notebook shows an example of accessing imagery for a given location.
* **Test.csv** -is similar to train, but without the label column. For these locations, you must predict whether or not they fall within an informal settlement. Test data is sourced from a different province to the training data - make sure that your model is able to generalize well.
* **Shapefiles** - In addition to the Train.csv file, you are provided with a shapefile outlining informal settlements in the Gauteng province. You may use this data to generate additional training inputs for your model.
* **SampleSubmission.csv** - Shows the required submission format, with predicted labels for each location in the test set. The order of the rows does not matter, but the names of the IDs must be correct.

## Leaderboard

Team **Old Timers**
@Salil-Gtm
* **[Private LB](https://zindi.africa/hackathons/sansa-informal-settlements-in-south-africa/leaderboard)** : **17th/69 Rank**
