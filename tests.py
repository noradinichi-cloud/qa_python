import pytest
from main import BooksCollector


class TestBooksCollector:

    def test_add_new_book_add_two_books(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        assert len(collector.get_books_genre()) == 2

    @pytest.mark.parametrize(
        'book_name, expected_count',
        [
            ('А', 1),
            ('А' * 40, 1),
            ('', 0),
            ('А' * 41, 0),
        ]
    )
    def test_add_new_book_name_length_validation(self, book_name, expected_count):
        collector = BooksCollector()
        collector.add_new_book(book_name)
        assert len(collector.get_books_genre()) == expected_count

    def test_add_new_book_duplicate_not_added(self):
        collector = BooksCollector()
        collector.add_new_book('Дюна')
        collector.add_new_book('Дюна')
        assert len(collector.get_books_genre()) == 1

    @pytest.mark.parametrize(
        'genre, expected_genre',
        [
            ('Фантастика', 'Фантастика'),
            ('Несуществующий жанр', ''),
        ]
    )
    def test_set_book_genre(self, genre, expected_genre):
        collector = BooksCollector()
        collector.add_new_book('Дюна')
        collector.set_book_genre('Дюна', genre)
        assert collector.get_book_genre('Дюна') == expected_genre

    def test_get_book_genre_returns_assigned_genre(self):
        collector = BooksCollector()
        collector.add_new_book('Оно')
        collector.set_book_genre('Оно', 'Ужасы')
        assert collector.get_book_genre('Оно') == 'Ужасы'

    def test_get_books_with_specific_genre_returns_matching_books(self):
        collector = BooksCollector()
        collector.add_new_book('Оно')
        collector.set_book_genre('Оно', 'Ужасы')
        collector.add_new_book('Дюна')
        collector.set_book_genre('Дюна', 'Фантастика')
        assert collector.get_books_with_specific_genre('Ужасы') == ['Оно']

    def test_get_books_genre_returns_full_dictionary(self):
        collector = BooksCollector()
        collector.add_new_book('Шрек')
        collector.set_book_genre('Шрек', 'Мультфильмы')
        assert collector.get_books_genre() == {'Шрек': 'Мультфильмы'}

    def test_get_books_for_children_excludes_age_restricted_genres(self):
        collector = BooksCollector()
        collector.add_new_book('Шрек')
        collector.set_book_genre('Шрек', 'Мультфильмы')
        collector.add_new_book('Оно')
        collector.set_book_genre('Оно', 'Ужасы')
        collector.add_new_book('Шерлок Холмс')
        collector.set_book_genre('Шерлок Холмс', 'Детективы')
        assert collector.get_books_for_children() == ['Шрек']

    def test_add_book_in_favorites_adds_unique_existing_book(self):
        collector = BooksCollector()
        collector.add_new_book('Ревизор')
        collector.add_book_in_favorites('Ревизор')
        collector.add_book_in_favorites('Ревизор')
        collector.add_book_in_favorites('Несуществующая книга')
        assert collector.get_list_of_favorites_books() == ['Ревизор']

    def test_delete_book_from_favorites_removes_book(self):
        collector = BooksCollector()
        collector.add_new_book('Ревизор')
        collector.add_book_in_favorites('Ревизор')
        collector.delete_book_from_favorites('Ревизор')
        assert collector.get_list_of_favorites_books() == []

    def test_get_list_of_favorites_books_returns_favorites_list(self):
        collector = BooksCollector()
        collector.add_new_book('Ревизор')
        collector.add_book_in_favorites('Ревизор')
        assert collector.get_list_of_favorites_books() == ['Ревизор']
