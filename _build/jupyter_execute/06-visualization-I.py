# Plotting with `Matplotlib`



import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

#define some points


#a basic plot


#add a title


#change the color and marker


#add x and y labels


import pandas as pd

## Basic Plots

- Histogram: one continuous set of values
- Line Plot: two continuous values
- Bar Plot: counts of categories
- Scatter Plot: two continuous values
- Boxplot: one continuous value

import seaborn as sns

titanic = sns.load_dataset('titanic')
penguins = sns.load_dataset('penguins')

#titanic time


#age vs. fare


#counts per class


#fare vs. age


#boxplot of survivals by age


### Using Seaborn

#scatterplot


#distplot


#countplot


#boxplot


#swarmplot


### `.groupby`

#group by gender


#group by island


#group by island and species


#group by age


#multiple summaries


### Subplots

#single subplot


#two columns 


#two rows


#two rows two columns


### Saving and Displaying Figures

#same image


#view in markdown cell
