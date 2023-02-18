# EECS 4412 - Data Mining
# Stage 5 Preprocessing: data_split.py
# Author: Gian Carlo Alix

# import necessary libraries
import pandas as pd

# split into the training and testing sets
# order was maintained, so the first 56K is the training
# and the remaining 14K is the testing
s2wv = pd.read_csv("s2wv.csv")
training_dataset = s2wv.head(56000)
testing_dataset = s2wv.tail(14000)

# grab the original training dataset to get the class attribute
df = pd.read_csv("data/train3.csv")
training_dataset = pd.concat([training_dataset, df['class']], axis=1)

# define a new column in the testing set called 'class'
# randomize an int(0,1,2) and assign to each review
# then replace (0,1,2) with (positive, negative, neutral)
# note that this only a pseudo-column for the correctness of syntax in Weka
testing_dataset['class'] = np.random.randint(0,3,size=(len(testing_dataset),1))
testing_dataset['class'] = testing_dataset['class'].replace(0, 'negative')
testing_dataset['class'] = testing_dataset['class'].replace(1, 'neutral')
testing_dataset['class'] = testing_dataset['class'].replace(2, 'positive')

# further split the training set into 75% training and 25% validation
validation_dataset = training_dataset.sample(frac=0.25)
training_dataset = training_dataset.drop(validation_dataset.index)

# output the CSV files
training_dataset.to_csv("for_model_training.csv",index=False)
validation_dataset.to_csv("for_model_validation.csv",index=False)
testing_dataset.to_csv("for_model_testing.csv",index=False)