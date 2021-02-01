#!/usr/bin/env python
# coding: utf-8

# # Collections
# 
# In addition to individual variables that contain information, Python also can create collections of objects including variables.  There are three main types of these:
# 
# **Ordered Collections**
# 
# - list
# - tuple
# 
# **Unordered Collections**
# 
# - dictionary

# ## LIST

# In[1]:


#a simple list
simple_list = [1, 2, 3, 'steve']


# In[2]:


type(simple_list)


# In[3]:


#work like strings for indexing
simple_list[0]


# In[4]:


#start at 2 and go to end
simple_list[2:]


# In[5]:


#can alter the list easily
simple_list[2] = 'hardy'


# In[6]:


simple_list


# ## TUPLE

# In[7]:


#a basic tuple
simple_tuple = (1, 2, 3, 'steve')


# In[8]:


type(simple_tuple)


# In[9]:


simple_tuple[0]


# In[10]:


simple_tuple[2:]


# In[11]:


#main difference from a list!
simple_tuple[2] = 'hardy'


# ## Dictionary
# 
# Here, we have a key rather than an index, and a value associated with this key.  Because there is not a numeric index, we have to explicitly provide these.

# In[14]:


dog = {'name': 'hardy', 'hobbies': ['naps', 'snacks', 'fetch']}


# In[16]:


type(dog)


# In[17]:


dog['name']


# In[27]:


dog['hobbies']


# In[28]:


#add a new value
dog['new_value'] = 'something totally new'


# In[29]:


dog


# ## Methods on Collections
# 
# Lists and Dictionaries will occupy most of our time so we will limit our exploration to these collections and their associated methods for now.  Much like strings, we have methods for dictionaries and for lists, and they follow the same patterns of:
# 
# ```python
# collection.method()
# ```

# In[19]:


#append a value to the end of a list
simple_list.append('oden')


# In[20]:


simple_list


# In[22]:


simple_list.insert( 1, 'sebastian')


# In[23]:


simple_list


# In[24]:


dog.items()


# In[25]:


dog.keys()


# In[26]:


dog.values()


# ### PROBLEMS
# 
# 1. Create a list containing a string, int, float, and boolean object.  Save this to ans_1 below.
# 2. Create a tuple containing the same elements as problem 1.
# 3. Append the word *dogs* to your list.
# 4. Create a dictionary of your five favorites using a list of length five for each entry:
# 
# ```python
# favorites = {'songs': [],
#              'numbers': [],
#              'movies': []}
# ```
# 
# 5. Add another key value pair to your favorites dictionary that has values for your five favorite fruits.

# In[30]:


ans1 = ''


# In[31]:


ans2 = ''


# In[32]:


ans3 = ''


# In[33]:


ans4 = ''


# In[34]:


ans5 = ''

