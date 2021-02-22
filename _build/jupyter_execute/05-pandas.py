# Introduction to Pandas 🐼

![](https://i.redd.it/c6h7rok9c2v31.jpg)

> *pandas is a fast, powerful, flexible and easy to use open source data analysis and manipulation tool,
built on top of the Python programming language.*

import pandas as pd

## The `DataFrame`

Our data structure is a basic table of columns and rows.  Below we both create a DataFrame from a dictionary and read in a data file to create a DataFrame

#dictionary


#dataframe


#load in file


#dataframe


#from url


#built in


### Selecting Columns


#examine the column names of diamonds


#select the carat column


#select the carat and rating column


#select many columns


**PROBLEMS**

- Load in dataset as a DataFrame:
- Display column names
- Select one column
- Select multiple columns









### Selecting Columns based on Conditions

Perhaps we only want diamonds that have more than 1 carat.  We can filter the data to identify these using our comparison operators.

#larger than 1 carat?


#subset based on these


#more than one condition


#a second example


#### PROBLEMS

1. Go to `kaggle.com` and signup for an account. 
2. Search for a dataset of interest and see if there is a reasonably sized `.csv` file to download.
3. Download the data, and load this into a jupyter notebook.
4. Look at the `.info()`.
5. Look at the top 5 rows of data with `.head()`.
6. Select one column from your data.
7. Select multiple columns from your data.
8. Select rows based on a condition.
9. Find a second dataset and repeat.  
























### More Functions

#sort values


#largest values


#missing values


#smallest values


#replace


#drop
