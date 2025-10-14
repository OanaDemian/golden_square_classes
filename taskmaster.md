# Taskmaster Class Design Recipe

Copy this into a `recipe.md` in your project and fill it out.

## 1. Describe the Problem

As a user
So that I can keep track of my tasks
I want a program that I can add todo tasks to and see a list of them.

As a user
So that I can focus on tasks to complete
I want to mark tasks as complete and have them disappear from the list.

## 2. Design the Class Interface

_Include the initializer, public properties, and public methods with all parameters, return values, and side-effects._

```python
# EXAMPLE

class Taskmaster:
    # User-facing properties:
    # None

    def __init__(self, name):
        # Parameters:
        #   tasklist: list of strings 
        #   completed_tasks: list of strings
        # Side effects:
        #   Sets the tasklist property of the self object
        pass # No code here yet

    def add_todo(self, todo):
        # Parameters:
        #   todo: string representing a single todo task
        # Returns:
        #   Nothing
        # Side-effects
        #   Saves the todo task to the self object
        pass # No code here yet

    def track_todos(self):
        # Returns:
        #   A list of strings representing all the todos added by the user
        # Side-effects:
        #   None
        pass # No code here yet

    def mark_complete(self, todo):
        # Returns:
        #   Nothing
        # Side-effects:
        #   removes todo task from tasklist, adds it to completed_tasks
        pass # No code here yet

    def track_completed_tasks(self):
        # Returns:
        # a list of strings representing all the completed tasks
        pass # No code here yet

```

## 3. Create Examples as Tests

_Make a list of examples of how the class will behave in different situations._

``` python
# EXAMPLE

"""
Given one todo task
#add_todo adds the todo to tasklist
"""
taskmaster = Taskmaster()
taskmaster.add_todo("Walk the dog")
taskmaster.track_todos() # => ["Walk the dog"]

"""
Given no todo task
# track_todos returns []
"""
taskmaster = Taskmaster()
taskmaster.track_todos() # => []

"""
Given multiple todo tasks
#track_todos reflects those todos
"""
taskmaster = Taskmaster()
taskmaster.add_todo("Walk the dog")
taskmaster.add_todo("Take out the bin")
taskmaster.add_todo("Wash the dishes")
taskmaster.add_todo("Vacuum the rooms")
taskmaster.track_todos() # => ["Walk the dog", "Take out the bin", "Wash the dishes", ("Vacuum the rooms"]

"""
Given an empty todo
#add_todo raises an expeption
"""
taskmaster = Taskmaster()
taskmaster.add_todo("") # =>raises exception


"""
Given 4 todo tasks, 
When we marlk one as complete
#track_todos reflects only the two unfinished todos
"""

taskmaster = Taskmaster()
taskmaster.add_todo("Walk the dog")
taskmaster.add_todo("Take out the bin")
taskmaster.add_todo("Wash the dishes")
taskmaster.add_todo("Vacuum the rooms")
taskmaster.mark_complete("Take out the bin")
taskmaster.track_todos() # => ["Walk the dog", "Wash the dishes", ("Vacuum the rooms"]
taskmaster.track_completed_tasks # => ["Take out the bin"]

"""
Given no todo tasks, 
When we mark one as complete
#mark_complete raises an error
"""

taskmaster = Taskmaster()
taskmaster.mark_complete("Take out the bin")  # => [ raises error
```

_Encode each example as a test. You can add to the above list as you go._

## 4. Implement the Behaviour

_After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour._
