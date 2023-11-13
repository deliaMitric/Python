#Design a library catalog system with a base class LibraryItem and subclasses for different types of items like Book,
# DVD, and Magazine. Include methods to check out, return, and display information about each item.
class LibraryItem:
    def __init__(self, id, title, authors):
        if isinstance(id, int) and isinstance(title, str) and isinstance(authors, list):
            self._id = id
            self._title = title
            self._authors = authors
            self._checked_out = False

    def check_out(self):
        if not self._checked_out:
            self._checked_out = True
            return f"The item {self._title} has been successfully checked."
        return f"The item {self._title} is already checked!"

    def return_item(self):
        if self._checked_out:
            self._checked_out = False
            return f"The item {self._title} has been successfully returned."
        return f"The item {self._title} isn't checked!"

    def __str__(self):
        str_authors = ""
        for index, author in enumerate(self._authors, start=1):
            str_authors += f"Author {index}: {author} "
        return f"TITLE: {self._title} AUTHORS: {str_authors} ID: {self._id}"

class Book(LibraryItem):
    def __init__(self, id, title, authors, chapters, genre, language, num_pages):
        super().__init__(id, title, authors)
        if isinstance(chapters, list) and isinstance(genre, str) and isinstance(language, str) and isinstance(num_pages,int) and num_pages > 0:
            self._chapters = chapters
            self._genre = genre
            self._language = language
            self._num_pages = num_pages

    def __str__(self):
        str_authors = ""
        for index, author in enumerate(self._authors, start=1):
            str_authors += f"Author {index}: {author} "

        str_chapters = ""
        for index, chapter in enumerate(self._chapters, start=1):
            str_chapters += f"Chapter {index}: {chapter}"

        return f"TITLE: {self._title} AUTHORS: {str_authors} ID: {self._id} CHAPTERS: {str_chapters} GENRE: {self._genre} LANGUAGE: {self._language} PAGES: {self._num_pages}"

    def is_long(self):
        if self._num_pages > 300:
            return "Is a long book."
        return "Is a short book."

    def average_reading_time(self):
        return (self._num_pages * 5) // 60


class DVD(LibraryItem):
    def __init__(self, id, title, authors, duration, directors, subtitles):
        super().__init__(id, title, authors)
        if isinstance(duration, (int, float)) and duration > 0 and isinstance(directors, list) and isinstance(subtitles, list):
            self._duration = duration
            self._directors = directors
            self._subtitles = subtitles

    def __str__(self):
        str_authors = ""
        for index, author in enumerate(self._authors, start=1):
            str_authors += f"Author {index}: {author} "

        str_directors = ""
        for index, director in enumerate(self._directors, start=1):
            str_directors += f"Director {index}: {director} "

        str_subtitles = ""
        for index, subtitle in enumerate(self._subtitles, start=1):
            str_subtitles += f"Director {index}: {subtitle} "

        return f"TITLE: {self._title} AUTHORS: {str_authors} ID: {self._id} DURATION: {self._duration} DIRECTORS: {str_directors} SUBTITLES: {str_subtitles}"


class Magazine(LibraryItem):
    def __init__(self, id, title, authors, num_articles, issue_number, theme):
        super().__init__(id, title, authors)
        if isinstance(num_articles, int) and num_articles > 0 and isinstance(issue_number, int) and issue_number > 0 and isinstance(theme, str):
            self._num_articles = num_articles
            self._issue_number = issue_number
            self._theme = theme

    def __str__(self):
        str_authors = ""
        for index, author in enumerate(self._authors, start=1):
            str_authors += f"Author {index}: {author} "

        return f"TITLE: {self._title} AUTHORS: {str_authors} ID: {self._id} ARTICLES NUMBER: {self._num_articles} ISSUE_NUMBER: {self._issue_number} THEME: {self._theme}"

if __name__ == '__main__':
    items = [Book(4, "Ion", ["Liviu Rebreanu"], ["Sosirea lui Ion "], "Roman", "Romanian", 500), Magazine(103, "Star", ["author1", "author2"], 5, 12, "Moda")]
    print(str(items[0]))
    print(items[0].average_reading_time())

    for item in items:
        print(str(item))

    print(items[1].check_out())
    print(items[1].return_item())
    print(items[1].return_item())
