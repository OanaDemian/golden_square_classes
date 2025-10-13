# {{GrammarStats}} Class Design Recipe

Copy this into a `recipe.md` in your project and fill it out.

## 1. Describe the Problem

As a user
So that I can check my grammar 
I want to see if a text begins with a capital letter and ends with a sentence-ending punctuation mark.

As a user
So that I can see my performance 
I want to see the percentage of texts checked so far that have passed the check

## 2. Design the Class Interface

_Include the initializer, public properties, and public methods with all parameters, return values, and side-effects._

```python
# EXAMPLE

class GrammarStats:
    def __init__(self):
        pass

    def check(self, text):
        # Parameters:
        #   text: string
        # Returns:
        #   bool: true if the text begins with a capital letter and ends with a
        #         sentence-ending punctuation mark, false otherwise
        pass

    def percentage_good(self):
        # Returns:
        #   int: the percentage of texts checked so far that passed the check
        #        defined in the `check` method. The number 55 represents 55%.
        pass

```

## 3. Create Examples as Tests

_Make a list of examples of how the class will behave in different situations._

``` python
# EXAMPLE

"""
Given the text Walk the dog, Kay!
#check returns True because the text begins with a capital letter and ends with a sentence-ending punctuation mark
"""
grammar_stats = GrammarStats()
grammar_stats.check("Walk the dog, Kay!") # => True


"""
Given the text Walk the dog, Kay
#check returns False because the text begins with a capital letter but doesn't end with a sentence-ending punctuation mark
"""
grammar_stats = GrammarStats()
grammar_stats.check("Walk the dog, Kay") # => False

"""
Given the texts "Walk the dog, Kay!", "Vacuum the rooms, Oana" and "Take the garbage out, Simon"
#percentage_good returns 33
"""
grammar_stats = GrammarStats()
grammar_stats.check("Walk the dog, Kay!") # => True
grammar_stats.check("Vacuum the rooms, Oana!") # => True
grammar_stats.check("Take the garbage out, Simon!") # => False
grammar_stats.percentage_good() # => 33
"""

Given no text
#check raises an exception
"""
grammar_stats = GrammarStats()
grammar_stats.check() # => raises an error with the message "No text provided."

"""
Given no texts
#percentage_good raises an exception
"""
grammar_stats = GrammarStats()
grammar_stats.percentage_good() # => raises an error with the message "Cannot calculate a percentage of checked texts when no texts provided."
"""

```

_Encode each example as a test. You can add to the above list as you go._

## 4. Implement the Behaviour

_After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour._
