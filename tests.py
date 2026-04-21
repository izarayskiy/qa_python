import pytest


# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:

    # пример теста:
    # обязательно указывать префикс test_
    # дальше идет название метода, который тестируем add_new_book_
    # затем, что тестируем add_two_books - добавление двух книг
    def test_add_new_book_add_two_books(self, collector):
        # добавляем две книги
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        # проверяем, что добавилось именно две
        # словарь books_rating, который нам возвращает метод get_books_rating, имеет длину 2
        assert len(collector.get_books_genre()) == 2

    # напиши свои тесты ниже
    # чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollector()

    @pytest.mark.parametrize(
        'name',
        [
            'Пепел и сталь',
            'А' * 40,
        ],
    )
    def test_add_new_book_with_valid_name_length(self, name, collector):
        """Добавляем книгу с корректным именем"""
        collector.add_new_book(name)

        assert name in collector.get_books_genre()
        assert collector.get_book_genre(name) == ''

    @pytest.mark.parametrize(
        'name',
        [
            '',
            'B' * 41,
        ],
    )
    def test_add_new_book_with_invalid_name_length(self, name, collector):
        """Добавляем книгу с некорректным именем"""
        collector.add_new_book(name)

        assert name not in collector.get_books_genre()

    def test_set_book_genre_for_existing_book(self, collector):
        """Получаем жанр книги"""
        collector.add_new_book('Дюна')

        collector.set_book_genre('Дюна', 'Фантастика')

        assert collector.get_book_genre('Дюна') == 'Фантастика'

    def test_get_books_with_specific_genre(self, collector):
        """Получаем книги по жанрам"""
        collector.add_new_book('Дюна')
        collector.add_new_book('Оно')
        collector.set_book_genre('Дюна', 'Фантастика')
        collector.set_book_genre('Оно', 'Ужасы')

        books = collector.get_books_with_specific_genre('Фантастика')

        assert books == ['Дюна']
    
    def test_get_books_genre_returns_genre_dictionary(self, collector):
        """Получаем словарь в котором содержатся книги и их жанры"""
        collector.add_new_book('Дюна')
        collector.set_book_genre('Дюна', 'Фантастика')

        books_genre = collector.get_books_genre()

        assert books_genre == {'Дюна': 'Фантастика'}

    def test_get_books_for_children(self, collector):
        """Получаем список книг для детей"""
        collector.add_new_book('Дюна')
        collector.add_new_book('Шерлок Холмс')
        collector.add_new_book('Винни-Пух')
        collector.set_book_genre('Дюна', 'Фантастика')
        collector.set_book_genre('Шерлок Холмс', 'Детективы')
        collector.set_book_genre('Винни-Пух', 'Комедии')

        books_for_children = collector.get_books_for_children()

        assert books_for_children == ['Дюна', 'Винни-Пух']
    
    def test_add_book_in_favorites(self, collector):
        """Добавляем книгу в избранное"""
        collector.add_new_book('Дюна')

        collector.add_book_in_favorites('Дюна')
        collector.add_book_in_favorites('Дюна')
        collector.add_book_in_favorites('Несуществующая книга')

        assert collector.get_list_of_favorites_books() == ['Дюна']
    
    def test_delete_book_from_favorites(self, collector):
        """Удаляем книгу из избранного"""
        collector.add_new_book('Дюна')
        collector.add_book_in_favorites('Дюна')

        collector.delete_book_from_favorites('Дюна')

        assert collector.get_list_of_favorites_books() == []

    def test_get_current_list_of_favorites_books(self, collector):
        """Получаем список текущих книг в избранном"""
        collector.add_new_book('Дюна')
        collector.add_new_book('Оно')
        collector.add_book_in_favorites('Дюна')
        collector.add_book_in_favorites('Оно')

        favorites = collector.get_list_of_favorites_books()

        assert favorites == ['Дюна', 'Оно']
