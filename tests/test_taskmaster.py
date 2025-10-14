import pytest
from lib.taskmaster import Taskmaster


"""
Given one todo task
#add_todo adds the todo to tasklist
"""

def test_adds_todo_to_tasklist():
    taskmaster = Taskmaster()
    taskmaster.add_todo("Walk the dog")
    assert taskmaster.track_todos() == ["Walk the dog"]

"""
Given no todo task
# track_todos returns []
"""
def test_taskmaster_when_no_todos():
    taskmaster = Taskmaster()
    assert taskmaster.track_todos() == []

"""
Given multiple todo tasks
#track_todos reflects those todos
"""

def test_given_multiple_todos():
    taskmaster = Taskmaster()
    taskmaster.add_todo("Walk the dog")
    taskmaster.add_todo("Take out the bin")
    taskmaster.add_todo("Wash the dishes")
    taskmaster.add_todo("Vacuum the rooms")
    assert taskmaster.track_todos() == ["Walk the dog", "Take out the bin", "Wash the dishes", "Vacuum the rooms"]

"""
Given an empty todo
#add_todo raises an expeption
"""

def test_given_empty_todo_raise_exception():
    taskmaster = Taskmaster()
    with pytest.raises(Exception) as e:
        taskmaster.add_todo("")
    assert str(e.value) == "Please add a valid task!"


"""
Given 4 todo tasks, 
When we marlk one as complete
#track_todos reflects only the two unfinished todos
"""

def test_given_empty_todo_raise_exception():
    taskmaster = Taskmaster()
    taskmaster.add_todo("Walk the dog")
    taskmaster.add_todo("Take out the bin")
    taskmaster.add_todo("Wash the dishes")
    taskmaster.add_todo("Vacuum the rooms")
    taskmaster.mark_complete("Take out the bin")
    assert taskmaster.track_todos() == ["Walk the dog", "Wash the dishes", "Vacuum the rooms"]
    assert taskmaster.track_completed_tasks() == ["Take out the bin"]

"""
Given no todo tasks, 
When we mark one as complete
#mark_complete raises an error
""" 
def test_mark_complete_raises_error_when_no_todos():
    taskmaster = Taskmaster()
    with pytest.raises(Exception) as e:
        taskmaster.mark_complete("Take out the bin") 
    assert str(e.value) == "There are no tasks set, so none can be removed. Set up a task to do!"