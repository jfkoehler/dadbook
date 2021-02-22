

# Functions



---

### Lesson objectives

By the end of this lesson, you should be able to:

1. Successfully **create** and **invoke** a function
2. Understand how to use parameters in a function
3. Understand how to return a value from a function
4. Know what a lambda function is and how to create one




## Activity: Basic function
---

Create a function in cell below called `greeting` that prints `"Howdy"`.

# Declare the function

# Invoke the function

## Activity: Function parameters
---

In the [Kaggle Titanic competition](https://www.kaggle.com/c/titanic/data), the names of everyone in the manifest look like this:
> Last, Title. First

Create a function called `titanic_name` that accepts 3 parameters:
- `first_name`
- `last_name`
- `title` 

And prints the full name in the format above.



## Named parameters vs Ordered parameters
---

In the above example, you must order in which you add your arguments coincides with the order of the parameters in the function declaration. If you called them out of order like so:
```python
titanic_name('Doe', 'Captain', 'John')
```

Then the following would happen:

1. `'Doe'` would be assigned to `first_name`
2. `'Captain'` would be assigned to `last_name`
3. `'John'` would be assigned to `title`.

As a result, the function would print `'Captain, John. Doe'`. No bueno.



You can get around this by referencing the parameters by name:

```python
titanic_name(last_name='Doe', title='Captain', first_name='John')
```

Notice the order is the same as our bug: `('Doe', 'Captain', 'John')`. Only now the function will work properly.

To summarize, ordering your parameters matters **unless you reference the parameters by name**.



## Returning values from a function
---

Let's say we want to use the result from our `titanic_name` function elsewhere in our code. To do this, we'll set a variable like so:
```python
formatted_name = titanic_name(last_name='Doe', title='Captain', first_name='John')
```

We'd expect `formatted_name` to be `'Doe, Captain. John'`, but that's not the case. When we output `formatted_name` in a cell, we see that nothing shows up. This is because our function **prints** the name `'Doe, Captain. John'`, but nothing gets returned. 

**Remember** printing is merely for you the developer to debug your code. In order to use result from `titanic_name` elsewhere in our code, we need to explicitly return it:
```python
def titanic_name(first_name, last_name, title):
    return f'{last_name}, {title}. {first_name}'
```



## Lambda functions
---

[Lambda functions](https://docs.python.org/3/tutorial/controlflow.html#lambda-expressions) allow us to create an anonymous function on the fly. We'll use them extensively when we learn about `pandas` next week.

Here's a simple named function:
```python
def greeting(name):
    return f'Howdy, {name}'
```

And here is its `lambda` equivalent:
```python
lambda name: f'Howdy, {name}'
```

The primary differences between named and lambda functions are:

1. `lambda` functions don't have a name
2. `lambda` functions are written on one line
3. `lambda` functions don't require a `return`. It's implied that the `lambda` function above will return `"Howdy, NAME"`



## Challenge: DNA to RNA
---

If you've taken a Biology class, you know that DNA is essentially a long string comprised of 4 nucleotides:

- Cytosine (C)
- Thymine (T)
- Adenine (A)
- Guanine (G)

Example:
```python
dna = 'ACGTAAAACGTGGTGGATTTGACGTGTTTG'
```

RNA is similar to DNA with one exception: all instances of Thymine (T) are replaced with Uracil (U). Our DNA from above would look like this:
```python
rna = 'ACGUAAAACGUGGUGGAUUUGACGUGUUUG'
```

In the cell below, create a function called `dna_to_rna` that accepts a string of DNA and converts it to RNA.



## Challenge: Hamming Distance
---

The DNA strand `'AAAA'` is similar to the strand `'AAAT'` with one exception: the 4th nucleotide is different. In other words, the two strands have a **hamming distance** of 1, where hamming distance is the number of nucleotides that differ between two strands.

In the cell below, create a function called `hamming_distance` that accepts two parameters (`dna1` and `dna2`) and calculates the hamming distance between the two strands. 

**NOTE:** You can assume the two strands will have the same length.



## Challenge: Find the divisors
---

From [codewars](https://www.codewars.com/kata/find-the-divisors/train/python). Create a function called `divisors` that accepts a number and returns a list of all the divisors for that number. 

For example: `divisors(12)` will return the list `[2, 3, 4, 6]`. 

**Note**: 1 doesn't count as a divisor.
**Note**: If the number doesn't have any divisors, it is prime (e.g. 13, 23, etc). In cases where the number is prime, simply return the string `'13 is prime'`.

