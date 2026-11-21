# Юнит-тесты для приложения BooksCollector

## Реализованные проверки в `tests.py`:
- `test_add_new_book_add_two_books` — добавление двух новых книг в словарь.
- `test_add_new_book_name_length_validation` — проверка граничных значений длины названия книги (1, 40, 0 и 41 символ).
- `test_add_new_book_duplicate_not_added` — запрет повторного добавления уже существующей книги.
- `test_set_book_genre` — установка валидного жанра и игнорирование несуществующего жанра.
- `test_get_book_genre_returns_assigned_genre` — получение жанра книги по её имени.
- `test_get_books_with_specific_genre_returns_matching_books` — фильтрация и вывод списка книг по заданному жанру.
- `test_get_books_genre_returns_full_dictionary` — получение текущего словаря `books_genre`.
- `test_get_books_for_children_excludes_age_restricted_genres` — проверка, что в список книг для детей не попадают книги с возрастным рейтингом («Ужасы», «Детективы»).
- `test_add_book_in_favorites_adds_unique_existing_book` — добавление существующей книги в «Избранное» с защитой от дублей и несуществующих книг.
- `test_delete_book_from_favorites_removes_book` — удаление книги из списка «Избранного».
- `test_get_list_of_favorites_books_returns_favorites_list` — получение списка избранных книг.
