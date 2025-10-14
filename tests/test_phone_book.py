from lib.phone_book import PhoneBook

"""
Initially, there are no phone numbers
"""

def test_phonebook_initially_it_has_no_phone_numbers():
    phone_book = PhoneBook()
    assert phone_book.list_numbers() == []
    

"""
When we add a diary entry with no number in it
There are no numbers reflected in the list
"""

def test_diary_entry_with_no_numbers():
    phone_book = PhoneBook()
    phone_book.extract_numbers("My friend's number ios not relevant here")
    assert phone_book.list_numbers() == []

"""
When we add a diary entry with a phone number in it
The phone number is reflected in the list
"""

def test_diary_entry_with_one_number():
    phone_book = PhoneBook()
    phone_book.extract_numbers("My friend's number is 07933333333")
    actual = phone_book.list_numbers()
    print('actual is', actual)
    expected = ["07933333333"]
    assert actual == expected


"""
When we add a diary entry with three phone numbers in it  
We see all phone numbers reflected in the list
"""

def test_diary_entry_with_three_numbers():
    phone_book = PhoneBook()
    phone_book.extract_numbers("Jimmy's number is 07933333333")
    phone_book.extract_numbers("Max's number is 07933333337")
    phone_book.extract_numbers("Lorenzo's number is 07933333334")
    assert phone_book.list_numbers() == ["07933333333", "07933333337", "07933333334"]


"""
When we add a diary entry with multiple phone numbers in it
We see all phone numbers reflected in the list
"""
def test_diary_entry_with_multiple_numbers():
    phone_book = PhoneBook()
    phone_book.extract_numbers("Jimmy's number is 07933333334 and Max's number is 07933333333")
    assert phone_book.list_numbers() == ["07933333334", "07933333333"]

"""
When we try to add a phone numbers that does not start with 0
The phone number is not reflected in the list
"""
def test_diary_entry_with_number_not_starting_with_0():
    phone_book = PhoneBook()
    phone_book.extract_numbers("Jimmy's number is 7933333334 and Max's number is 07933333333")
    assert phone_book.list_numbers() == [ "07933333333"]

"""
When we try to add a phone numbers that is not 11 numbers long
The phone number is not reflected in the list
"""
def test_diary_entry_with_number_not_11_numbers_long():
    phone_book = PhoneBook()
    phone_book.extract_numbers("Jimmy's number is 0007933333334 and Max's number is 07933333333")
    assert phone_book.list_numbers() == [ "07933333333"]