

import pytest
from lib.diary_entry import *

'''
Given a title and contents,
#format returns a formatted entry like: 
"My title: These are the contents."
'''

def test_given_diary_entry_formats_entry():
    diary_entry = DiaryEntry("Friday, 10th of October", "Today we're going to the Natural History Museum.")
    actual = diary_entry.format()
    expected = "Friday, 10th of October: Today we're going to the Natural History Museum."
    assert actual == expected

'''
Given a title and contents,
#count_words returns the number of words in the title and contents
'''

def test_counts_words_in_both_title_and_entry():
    diary_entry = DiaryEntry("Friday, 10th of October", "Today we're going to the Natural History Museum.")
    actual = diary_entry.count_words()
    expected = 12
    assert actual == expected

'''
Given no title and no contents,
#count_words raises an error
'''

def test_given_diary_entry_calculates_words_in_diary_entry():
    diary_entry = DiaryEntry("Friday, 10th of October", "Today we're going to the Natural History Museum.")
    actual = diary_entry.count_words()
    expected = 12
    assert actual == expected

'''
Given a wpm of 2
And a text with 12 words
# reading_time returns 6 minutes
'''

def test_minutes_it_takes_to_read_diary_entry():
    diary_entry = DiaryEntry("Friday, 10th of October", "Today we're going to the Natural History Museum.")
    actual = diary_entry.reading_time(2)
    expected = 6
    assert actual == expected

'''
Given a a text of 12 words
And a wpm of 2 
And an interval of 4 minutes
# reading_chunk returns the first 8 words
'''

def test_when_user_does_not_finish_reading_contents_in_given_time():
    diary_entry = DiaryEntry("Friday, 10th of October", "Today we're going to the Natural History Museum.")
    actual = diary_entry.reading_chunk(2, 4)
    expected = "Friday, 10th of October: Today we're going to"
    assert actual == expected

def test_when_user_finishes_reading_contents_in_given_times():
    diary_entry = DiaryEntry("Friday, 10th of October", "Today we're going to the Natural History Museum.")
    actual = diary_entry.reading_chunk(4, 4)
    expected = "Friday, 10th of October: Today we're going to the Natural History Museum."
    assert actual == expected

def test_when_user_continues_reading():
    diary_entry = DiaryEntry("Friday, 10th of October", "Today we're going to the Natural History Museum to see the new David Attenborough exhibition and to see the dinosaurs.")
    a = diary_entry.reading_chunk(2, 4)
    b = diary_entry.reading_chunk(2, 4)
    actual = diary_entry.reading_chunk(2, 4)
    expected =   "David Attenborough exhibition and to see the dinosaurs."
    assert actual == expected

'''
Given an empty title,
It raises an error
'''
def test_given_empty_title_raises_error():
    diary_entry = DiaryEntry("", "Today we're going to the Natural History Museum.")
    with pytest.raises(Exception) as e:
        diary_entry.format()
    assert str(e.value) == "Diary entries must have a title and a content."
    
'''
Given an empty content,
It raises an error
'''
def test_given_empty_content_raises_error():
    diary_entry = DiaryEntry("Friday, 10th of October", "")
    with pytest.raises(Exception) as e:
        diary_entry.format()
    assert str(e.value) == "Diary entries must have a title and a content."

'''
Given a wpm of 0
#reading_time raises and error
'''

def test_given_empty_title_raises_error():
    diary_entry = DiaryEntry("Friday, 10th of October", "Today we're going to the Natural History Museum.")
    with pytest.raises(Exception) as e:
        diary_entry.reading_time(0)
    assert str(e.value) == "Cannot calculate reading time with wpm of 0."