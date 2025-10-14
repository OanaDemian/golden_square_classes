class PhoneBook():

    def __init__(self):
        self.numbers = []

    def extract_numbers(self, diary_entry):
        for word in diary_entry.split():
            if len(word) == 11 and word.isdigit() and word[0] == '0':
                self.numbers += [word]
        

    def list_numbers(self):
        return self.numbers

# phone_book = PhoneBook()
# phone_book.extract_numbers("My friend's number is 07933333333")
# print(phone_book.list_numbers())