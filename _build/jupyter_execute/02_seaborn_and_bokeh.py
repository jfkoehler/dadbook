# Plotting with `seaborn`

import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

tips = sns.load_dataset('tips')

penguins = sns.load_dataset('penguins')

titanic = sns.load_dataset('titanic')

sns.countplot(titanic['sex'], hue = titanic['survived'])

#seaborn has a special plot for counts
sns.countplot(titanic['survived'])
#titanic['survived'].value_counts().plot(kind = 'bar')

penguins.head()

sns.boxplot(x = penguins['species'], y = penguins['flipper_length_mm'])
plt.title('Penguins by Species and Distribution of Bill Length')
plt.xlabel('Species of Penguin');

penguins.info()

sns.scatterplot(penguins['bill_length_mm'], penguins['bill_depth_mm']);

penguins = penguins.dropna()

sns.pairplot(penguins, hue = 'island')

titanic.head(1)

#Histogram of ages on the titanic 
#with appropriate title and x axis labels.
plt.hist(titanic['age']);
plt.title('Ages on the Titanic')
plt.xlabel('Ages');

titanic.head(1)

titanic['class'].value_counts()

#Barplot of counts of passengers by class on titanic.
titanic['pclass'].value_counts().plot(kind = 'bar');

#Boxplots of penguins


penguins.head(1)

penguins['species'].unique()

colors = []
#write a loop -- loop over the species
#if Adelie -- blue
#if Chinstrap -- yellow
#if Gentoo -- red
for species in penguins['species']:
    #test if Adelie
    if species == 'Adelie':
        colors.append('blue')
    #test if Chinstrap
    elif species == 'Chinstrap':
        colors.append('yellow')
    #test if Gentoo
    else:
        colors.append('red')

#Scatterplot of penguins
plt.scatter(penguins['bill_length_mm'], penguins['bill_depth_mm'], 
            c = colors)

#barplot for survival
titanic['survived'].value_counts().plot(kind = 'bar')

survival_counts = titanic['survived'].value_counts()

plt.bar([0, 1], survival_counts);

#histograms of flipper lengths








sns.boxplot(x = 'island', y = 'bill_length_mm', data = penguins);

















tips.head()

sns.stripplot('total_bill', data = tips)

iris = sns.load_dataset("iris")
sns.catplot(data=iris, orient="h", kind="box");

sns.catplot(x="day", y="total_bill", hue="smoker",
            col="time", aspect=.6,
            kind="swarm", data=tips);

titanic = sns.load_dataset("titanic")
sns.catplot(x="sex", y="survived", hue="class", kind="bar", data=titanic);

from bokeh.plotting import figure 
from bokeh.io import output_notebook, show

output_notebook()

x = [1, 2, 3, 4, 5]
y = [4, 2, 5, 6, 2]

p = figure(width = 600, height = 300)
p.circle(x, y)
show(p)

p = figure(width = 600, height = 300)
p.circle(x, y,  color = 'red', size = 10, alpha = 0.5)
show(p)

p = figure(width = 600, height = 400)
p.vbar(x= [0,0.5, 1], bottom = [0, 1, 1], top = [4, 3, 2], width = 0.2)
show(p)

### From a DataFrame

df = pd.read_csv('data/happiness/2015.csv')

df.head(2)

from bokeh.models import ColumnDataSource
from bokeh.layouts import gridplot
source = ColumnDataSource(df)


p1 = figure(title="Happiness and Economy", width = 600, height = 300)
p1.circle("Happiness Score", "Economy (GDP per Capita)", color="firebrick", size = 10,
          alpha = 0.5, 
          source=source)
p1.xaxis[0].axis_label = "Happiness Score"
p1.yaxis[0].axis_label = "GDP per Capita"

show(p1)

