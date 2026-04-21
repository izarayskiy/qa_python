# qa_python
## Список тестов
1. `test_add_new_book_add_two_books` - Тест из прекода. Проверка добавления книг. 
2. `test_add_new_book_with_valid_name_length` - Проверка добавления книги с корректным именем. Проверяется валидация из `add_new_book`
3. `test_add_new_book_with_invalid_name_length` - Проверка на добавление книги с некорректным именем. Проверяется валидация из `add_new_book`
4. `test_set_book_genre_for_existing_book` - Проверка получения жанра книги. Испульзуются методы `add_new_book`, `set_book_genre`, `get_book_genre` 
5. `test_get_books_with_specific_genre` - Проверка получения книг по жанрам. Проверяется метод `get_books_with_specific_genre`
6. `test_get_books_genre_returns_genre_dictionary` - Проверка формата возвращаемых данных из метода `get_books_genre`
7. `test_get_books_for_children` - Проверка что метод `get_books_for_children` возвращает книги с жанрами для детей
8. `test_add_book_in_favorites` - Проверка добавления книги в избранное. Используются методы `add_new_book`, `add_book_in_favorites`, `get_list_of_favorites_books`
9. `test_delete_book_from_favorites` - Удаление книги из избранного. Используются методы `delete_book_from_favorites`
10. `test_get_current_list_of_favorites_books` - Получение списка избранных книг. Используются методы `add_new_book`, `add_book_in_favorites`, `get_list_of_favorites_books`