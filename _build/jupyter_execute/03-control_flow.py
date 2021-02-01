#!/usr/bin/env python
# coding: utf-8

# 
# # Conditional Statements
# 
# 
# 
# We'll use an `if` statement if we want some code to only run if a certain condition is true.
# 
# 

# ![](if-flow.png)

# **QUESTION: Do you like Travis Scott?**
# 
# Below we have a variable that will be saved as `travis_scott`.  If it is yes, recommend your favorite Travis Scott song.  If no, please provide another recommendation.

# In[1]:


travis_scott = input("Do you like Travis Scott? (yes or no)")


# In[12]:


if travis_scott == 'yes':
    print('Maybe you will like Butterfly Effect on the Astroworld album.')
else:
    print('Maybe you would like Patsy Cline?')


# ## Loops
# 
# 
# 
# A `for` loop will iterate over any collection in python.  For example, if we wanted to iterate over the following list, we could do something like:
# 
# ```python
# for name in names:
#     print(name)
# ```

# In[7]:


names = ['lenny', 'hennessy', 'oden', 'hardy']


# In[8]:


for name in names:
    print(name)


# You can also loop through sequences of numbers with the built in `range()` function.

# In[13]:


# Range
for num in range(4):
    print(num)


# ### Putting it together
# 
# Now, if we have a collection of objects, we can loop over that collection and run a test.  This is typically how we would use these ideas.

# In[15]:


for name in names:
    if name == 'hennessy':
        print('Hennessy is here.')
    elif name == 'oden':
        print('Oden in the house.')
    else:
        print(f'{name.capitalize()} is here.')


# ### PROBLEMS

# 1. Loop over the following list of artists and determine whether or not the artist is "Drake".  If yes, print "yeah, it's Drake" otherwise print "nope, not Drake".
# 
# ```python
# artists = ['nipsey hussle', 'travis scott', 'drake', 'patsy cline', 'loretta lynne']
# ```

# 2. Loop over the artists list and print the capitalized version of each name.
# 3. Loop over the artists list and print the length of each string.

# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




