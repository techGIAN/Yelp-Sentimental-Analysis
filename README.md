# Yelp-Sentimental-Analysis
An NLP project for analyzing sentiments (positive, neutral, negative) of a review from the Yelp Open Dataset.

## Datasets

Download the datasets here: https://yuoffice-my.sharepoint.com/:f:/r/personal/gcalix_yorku_ca/Documents/Yelp-Sentimental-Datasets?csf=1&web=1&e=y8z4fz

## Summary

Here's a quick summary of this work:

* The dataset used in question was a subset of 70K reviews from the Yelp Open Dataset.

* The problem we aim to address is to be able to construct a classifier that is able to determiine whether a given review from the Yelp dataset, based on its text, had a positive sentiment, neutral, or negative.

* The first step (the zeroth step is basically securing the datasets and identifying the problem of interest) is to basically perform data preprocessing. This is includes cleaning the dataset, removing any noisy data or null values, removing stopwords (porter stemmer), tokenizing, taking only the key words in each review, encoding the words/texts to vectors (word2vec and String2Wordvec), etc.

* The next step is to consider some popular classifiers for this work. Several models have been tried to test which model is the most successful and superior against the others. Some models include: neural networks, random forests, logistic regression, naive bayes classifier, support vector machines, etc.

* The model chosen to have the top performance was the ***Discriminative Multinomial Naive Bayes Classifier***. which was able to achieve a good 82.2% accuracy, against all the other classifier models.

* All work was done using Weka, an open-source data mining software.

* The sentiment analysis in review datasets (not just Yelp) is important and has many useful applications.

