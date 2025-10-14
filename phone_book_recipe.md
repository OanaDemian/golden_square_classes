# Phone Book Class Design Recipe

Copy this into a `recipe.md` in your project and fill it out.

## 1. Describe the Problem

> As a user
> So that I can keep track of my phone numbers
> I want to keep a record of all phone numbers I use in my diary entry

* We may want to look through multiple diary entries
* Phone numbers are 11-digit numbers, starting with 0

## 2. Design the Class Interface

_Include the initializer, public properties, and public methods with all parameters, return values, and side-effects._

```python
# EXAMPLE

class PhoneBook:

    def extract_numbers(self, diary_entry):
        # Parameters:
        #   diary_entry: string representing a human readable text, possibly with phone numbers
        # Returns:
        #   Nothing
        # Side-effects
        #   Adds the diary entry to the self object
        pass # No code here yet

    def list_numbers(self):
        # Returns:
        #   A list of strings representing phone numbers
        # Side-effects:
        #   None
        pass # No code here yet
```

## 3. Create Examples as Tests

_Make a list of examples of how the class will behave in different situations._

``` python
# EXAMPLE

"""
Initially, there are no phone numbers
"""
phone_book = PhoneBook()
phone_book.list_numbers() # => []

"""
When we add a diary entry with no number in it
There are no numbers reflected in the list
"""
phone_book = PhoneBook()
phone_book.extract_numbers("My friend's number is not relevant here")
phone_book.list_numbers() # => []

"""
When we add a diary entry with a phone number in it
The phone number is reflected in the list
"""
phone_book = PhoneBook()
phone_book.extract_numbers("My friend's number is 07933333333")
phone_book.list_numbers() # => [07933333333']


"""
When we add a diary entry with three phone numbers in it
We see all phone numbers reflected in the list
"""
phone_book = PhoneBook()
phone_book.extract_numbers("Jimmy's number is 07933333333")
phone_book.extract_numbers("Max's number is 07933333337")
phone_book.extract_numbers("Lorenzo's number is 07933333334")
phone_book.list_numbers() # => ["07933333333", "07933333337", "07933333334"]


"""
When we add a diary entry with multiple phone numbers in it
We see all phone numbers reflected in the list
"""
phone_book = PhoneBook()
phone_book.extract_numbers("Jimmy's number is 07933333334 and Max's number is 07933333333")
phone_book.list_numbers() # => ["07933333334", "07933333333"]

"""
When we try to add a phone numbers that does not start with 0
The phone number is not reflected in the list
"""
phone_book = PhoneBook()
phone_book.extract_numbers("Jimmy's number is 7933333334 and Max's number is 07933333333")
phone_book.list_numbers() # => [ "07933333333"]

"""
When we try to add a phone numbers that is not 11 numbers long
The phone number is not reflected in the list
"""
phone_book = PhoneBook()
phone_book.extract_numbers("Jimmy's number is 0007933333334 and Max's number is 07933333333")
phone_book.list_numbers() # => [ "07933333333"]
```

_Encode each example as a test. You can add to the above list as you go._

## 4. Implement the Behaviour

_After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour._
