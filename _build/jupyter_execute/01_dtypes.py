#!/usr/bin/env python
# coding: utf-8

# # Intro to Python
# 
# To use the code cells, we hold down the `shift` and `enter` key to execute code.  Right away, we can use Python as a calculator.

# In[1]:


#addition (remember to hit shift + enter)
2 + 5


# In[2]:


#subtraction
5 - 4


# In[3]:


#multiplication
4 * 5


# In[4]:


#division
10/5


# In[5]:


#exponents
4 ** 2


# ## Data Types
# 
# There are four main *datatypes* we will be concerned with.  To begin, we will use numbers, words, and the results of comparisons as the main defining characteristics.  Additionally, we will differentiate between two kinds of numbers, with and without decimals.  Specifically:
# 
# - **STRINGS**: treated like text; words -- we tell Python we are using a string by enclosing something in either single or double quotes.

# In[6]:


'this is a string; it might have a number in it 8'


# In[7]:


#shows us what kind of a "thing" we are working with
type('this is a string; it might have a number in it 8')


# - **INT**: Whole numbers.  We type a whole number without quotes around it and have an int.

# In[8]:


8


# In[9]:


type(8)


# - **FLOAT**: Decimal numbers.  Use the period for a decimal and still no quotes.

# In[10]:


12.3


# In[11]:


type(12.3)


# - **BOOL**: determines the truthiness of something -- True or False.

# In[12]:


True


# In[13]:


type(False)


# ## Comparisons
# 
# We can test whether or not things are the same, one thing is greater than another, or greater than or equal to (and less than as well).
# 
# - `==`: are two things equal
# - `!=`: are two things not equal
# - `>`: greater than
# - `<`: less than
# - `>=`: greater than or equal
# - `<=`: less than or equal

# In[14]:


4 == 4.0


# In[15]:


4 < 8


# In[16]:


5 != 'steve'


# ### PROBLEMS

# The reason these seemingly boring things matter is that depending on the kind of object you are working with, different things will be allowed.  

# 1. What happens when you add two strings?
# ```python
# 'drake' + 'six_nine'
# ```
# 2. What happens when you add a string and an integer?
# ```python
# 'drake' + 8
# ```
# 3. What happens when you add a number and a boolean?
# 
# ```python
# 8.3 + True
# ```

# In[ ]:





# In[ ]:





# In[ ]:





# ## Variables
# 
# Typically we will store things in variables.  For example, the variable `age` and the variable `name` represent two different data types, stored in variables.

# In[17]:


name = 'Hennessy'
age = 14


# In[18]:


type(name)


# In[19]:


type(age)


# In[20]:


age + 15


# In[21]:


name + ' the dog'


# Some rules apply for variable names.  We cannot start names with numbers, and we cannot have spaces in our variable names.  As another rule, we do not want to use any Python functions or objects as names for the variable either.

# ## String Methods

# The variable `in_my_feelings` below contains a verse from Drake's song *In My Feelings*.  It is a string, and with a longer string there are some methods we can use to manipulate the object.  To use these, the general pattern will be:
# 
# ```python
# variable.method()
# ```
# 
# 

# In[22]:


in_my_feelings = '''Look, the new me is really still the real me
I swear you gotta feel me before they try and kill me
They gotta make some choices, they runnin' out of options
'Cause I've been goin' off and they don't know when it's stoppin'
And when you get to toppin', I see that you've been learnin'
And when you get to shoppin', you spend it like you earned it
And when you popped off on your ex he deserved it
I thought you were the one from the jump that confirmed it
TrapMoneyBenny
I buy you Champagne but you love some Henny
From the block like you Jenny
I know you special, girl, 'cause I know too many
'''


# In[23]:


#make everything uppercase
print(in_my_feelings.upper())


# In[24]:


#replace girl with boy
print(in_my_feelings.replace('girl', 'boy'))


# In[25]:


print(in_my_feelings.find('Champagne'))


# ## Slicing Strings
# 
# The last function to find the word "Champagne" returned the number 480.  This is the location of the word in the string.  We can slice a string to limit it to a certain range; may take some getting used to that we start counting at zero rather than 1.

# In[26]:


one_dance = '''That's why I need a one dance
Got a Hennessy in my hand
'''


# In[27]:


one_dance.find('dance')


# In[28]:


#start at letter 24 and go until 29
one_dance[24:29]


# ### Problem: Drake
# 
# <center>
#     <img src = https://cdn.vox-cdn.com/thumbor/7SKoV9-tOn9XQXZIwwrZoDKU96A=/0x0:3200x1800/1200x800/filters:focal(1344x644:1856x1156)/cdn.vox-cdn.com/uploads/chorus_image/image/60257237/drake.0.png width = 50%/>
#     </center>

# In[29]:


gods_plan = '''
Yeah, they wishin' and wishin' and wishin' and wishin'
They wishin' on me

I been movin' calm, don't start no trouble with me
Tryna keep it peaceful is a struggle for me
Don't pull up at 6 AM to cuddle with me
You know how I like it when you lovin' on me
I don't wanna die for them to miss me
Yes, I see the things that they wishin' on me
Hope I got some brothers that outlive me
They gon' tell the story, shit was different with me

God's plan, God's plan
I hold back, sometimes I won't (yeah)
I feel good, sometimes I don't, ayy, don't
I finessed down Weston Road, ayy, 'nessed
Might go down a G.O.D., yeah, wait
I go hard on Southside G, (yeah, wait)
I make sure that north-side eat

And still
Bad things
It's a lot of bad things
That they wishin' and wishin' and wishin' and wishin'
They wishin' on me
Bad things
It's a lot of bad things
That they wishin' and wishin' and wishin' and wishin'
They wishin' on me
Yuh, ayy, ayy

She said, "Do you love me?" I tell her, "Only partly"
I only love my bed and my momma, I'm sorry
Fifty Dub, I even got it tatted on me
81, they'll bring the crashers to the party
And you know me
Turn the O2 into the O3, dog
Without 40, Oli, there would be no me
Imagine if I never met the broskies

God's plan, God's plan
I can't do this on my own, ayy, no, ayy
Someone watchin' this shit close, yep, close
I've been me since Scarlett Road, ayy, road, ayy
Might go down as G.O.D., yeah, wait
I go hard on Southside G, ayy, wait
I make sure that north-side eat
And still

Bad things
It's a lot of bad things
That they wishin' and wishin' and wishin' and wishin'
They wishin' on me
Yeah, yeah
Bad things
It's a lot of bad things
That they wishin' and wishin' and wishin' and wishin'
They wishin' on me
Yeah
'''


# **PROBLEMS**
# 
# Using the variable *God's Plan* above, please answer the following questions:
# 
# 1. How many characters in the string?  (**Hint**: look at its length!)
# 2. Replace the word wishin with fishin.
# 3. What happens if we use the `.split()` method on the string?
# 4. Save the results of splitting the string to a variable called `tokens`.
# 5. What kind of an object is `tokens`?  (**Hint**: use `type()`)

# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




