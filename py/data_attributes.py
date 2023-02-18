# EECS 4412 - Data Mining
# Stage 6a Preprocessing: data_attributes.py
# Author: Gian Carlo Alix

# import necessary libraries
import pandas as pd

# Get the list of attributes
train_set = pd.read_csv("for_model_training.csv")
train_col = list(trainset.columns)

# construct the arff-formatted headings
output_file = open("attribute_list.txt", "w")
output_file.write("@relation\n\n")
for attribute in train_col:
	output = "@attribute " + attribute + " numeric\n"
	output_file.write(output)
output_file.write("@attirbute class {positive, negative, neutral}\n\n")
output_file.write("@data")

output_file.close()