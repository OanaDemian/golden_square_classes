import pytest
from lib.grammar_stats import GrammarStats

"""
Given the text Walk the dog, Kay!
#check returns True because the text begins with a capital letter and ends with a sentence-ending punctuation mark
"""

def test_check_when_correct_text():
    grammar_stats = GrammarStats()
    actual = grammar_stats.check("Walk the dog, Kay!") # => True     
    expected = True
    assert actual == expected


"""
Given the text Walk the dog, Kay
#check returns False because the text begins with a capital letter but doesn't end with a sentence-ending punctuation mark
"""

def test_check_when_text_misses_ending_punctuation():
    grammar_stats = GrammarStats()
    actual = grammar_stats.check("Walk the dog, Kay") # => False   
    expected = False
    assert actual == expected


"""
Given the text walk the dog, Kay!
#check returns False because the text doesn't begin with a capital letter 
"""
grammar_stats = GrammarStats()
grammar_stats.check("Walk the dog, Kay!") # => True

def test_check_when_text_does_not_start_with_capital():
    grammar_stats = GrammarStats()
    actual = grammar_stats.check("walk the dog, Kay!") # => False   
    expected = False
    assert actual == expected


"""
Given the texts "Walk the dog, Kay!", "Vacuum the rooms, Oana" and "Take the garbage out, Simon"
#percentage_good returns 33
"""

def test_percentage_good_when_2_texts_correct_one_incorrect():
    grammar_stats = GrammarStats()
    grammar_stats.check("Walk the dog, Kay!") # => True
    grammar_stats.check("Vacuum the rooms, Oana!") # => True
    grammar_stats.check("take the garbage out, Simon!") # => False
    actual = grammar_stats.percentage_good() # => 66
    expected = 66
    assert actual == expected

"""
Given empty string
#check raises an exception
"""

def test_check_when_no_text_provided():
    grammar_stats = GrammarStats()
    with pytest.raises(Exception) as e:
        grammar_stats.check("") 
    actual = str(e.value)
    expected = "No text provided."
    assert actual == expected


"""
Given string with whitespaces
#check raises an exception
"""

def test_check_when_text_with_whitespaces_only_provided():
    grammar_stats = GrammarStats()
    with pytest.raises(Exception) as e:
        grammar_stats.check("   ") 
    actual = str(e.value)
    expected = "No text provided."
    assert actual == expected

"""
Given string with only one character
#check returns false
"""

def test_check_when_text_with_only_one_character_provided():
    grammar_stats = GrammarStats()
    actual = grammar_stats.check("m") # => False   
    expected = False
    assert actual == expected

"""
Given string starting a non alphabetical value
#check returns false
"""

def test_check_when_text_starts_with_non_aplha_character():
    grammar_stats = GrammarStats()
    actual = grammar_stats.check(",") # => False   
    expected = False
    assert actual == expected


"""
Given no texts
#percentage_good raises an exception
"""

def test_percentage_good_when_no_texts_provided():
    grammar_stats = GrammarStats()
    with pytest.raises(Exception) as e:
        grammar_stats.percentage_good() 
    actual = str(e.value)
    expected = "Cannot calculate a percentage of checked texts when no texts provided."
    assert actual == expected