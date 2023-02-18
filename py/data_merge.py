# EECS 4412 - Data Mining
# Stage 3 Preprocessing: data_merge.py
# Author: Gian Carlo Alix

# import necessary libraries
import pandas as pd

# temporarily merge the training and testing sets
# do not mess up the order; the first 56K rows are train_sets
# while the remaining ones are test_sets
train_stemmed = pd.read_csv("train_stemmed.csv")
test_stemmed = pd.read_csv("test_stemmed.csv")
merged_dataset = train_stemmed.append(test_stemmed)
merged_dataset.to_csv("merged_set.csv",index=False)