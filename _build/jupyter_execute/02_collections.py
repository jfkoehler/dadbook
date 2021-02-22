# Collections

In addition to individual variables that contain information, Python also can create collections of objects including variables.  There are three main types of these:

**Ordered Collections**

- list
- tuple

**Unordered Collections**

- dictionary

## LIST

#a simple list
simple_list = [1, 2, 3, 'steve']

type(simple_list)

#work like strings for indexing
simple_list[0]

#start at 2 and go to end
simple_list[2:]

#can alter the list easily
simple_list[2] = 'hardy'

simple_list

## TUPLE

#a basic tuple
simple_tuple = (1, 2, 3, 'steve')

type(simple_tuple)

simple_tuple[0]

simple_tuple[2:]

#main difference from a list!
simple_tuple[2] = 'hardy'

## Dictionary

Here, we have a key rather than an index, and a value associated with this key.  Because there is not a numeric index, we have to explicitly provide these.

dog = {'name': 'hardy', 'hobbies': ['naps', 'snacks', 'fetch']}

type(dog)

dog['name']

dog['hobbies']

#add a new value
dog['new_value'] = 'something totally new'

dog

## Methods on Collections

Lists and Dictionaries will occupy most of our time so we will limit our exploration to these collections and their associated methods for now.  Much like strings, we have methods for dictionaries and for lists, and they follow the same patterns of:

```python
collection.method()
```

#append a value to the end of a list
simple_list.append('oden')

simple_list

simple_list.insert( 1, 'sebastian')

simple_list

dog.items()

dog.keys()

dog.values()

### PROBLEMS

1. Create a list containing a string, int, float, and boolean object.  Save this to ans_1 below.
2. Create a tuple containing the same elements as problem 1.
3. Append the word *dogs* to your list.
4. Create a dictionary of your five favorites using a list of length five for each entry:

```python
favorites = {'songs': [],
             'numbers': [],
             'movies': []}
```

5. Add another key value pair to your favorites dictionary that has values for your five favorite fruits.

ans1 = ''

ans2 = ''

ans3 = ''

ans4 = ''

ans5 = ''