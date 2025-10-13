import math

class DiaryEntry():

    def __init__(self, title, contents):
        self._title = title
        self._contents = contents
        self._text = title + ": " + contents

    def format(self):
        if self._title == "" or self._contents == "":
            raise Exception("Diary entries must have a title and a content.")
        return f"{self._title}: {self._contents}"

    def count_words(self):
        words = self.format().split()
        return len(words)

    def reading_time(self, wpm):
        if wpm == 0:
            raise Exception("Cannot calculate reading time with wpm of 0.")
        return math.ceil(self.count_words() / wpm)

    def reading_chunk(self, wpm, minutes):
        words_can_read_in_given_time = wpm * minutes
        text_read = " ".join(self._text.split()[:words_can_read_in_given_time])
        self._text = " ".join(self._text.split()[words_can_read_in_given_time:])
        return text_read