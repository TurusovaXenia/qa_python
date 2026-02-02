from unittest.mock import Mock

import pytest

import data
from main import BooksCollector

class TestBooksCollector:

    @pytest.mark.parametrize(
        'book_name', [data.book1, data.book2]
    )
    def test_add_new_book_add_book_success(self, collector, book_name):
        collector.add_new_book(book_name)
        assert len(collector.books_genre) == 1
        assert book_name in collector.books_genre

    def test_add_new_book_when_book_already_exists_one_book_is_added(self, collector):
        collector.add_new_book(data.book1)
        collector.add_new_book(data.book1)
        assert len(collector.books_genre) == 1

    def test_set_book_genre_genre_success(self, collector):
        collector.books_genre = {data.book1 : ''}
        collector.set_book_genre(data.book1, data.genre_1)
        assert collector.books_genre[data.book1] == data.genre_1

    @pytest.mark.parametrize(
        'books_genre, book_name, expected_genre',
        [
            ({data.book1 : data.genre_1}, data.book1, data.genre_1),
            ({data.book2 : ''}, data.book2, ''),
            ({}, data.book1, None)
        ]
    )
    def test_get_book_genre_book_success(self, collector, books_genre, book_name, expected_genre):
        collector.books_genre = books_genre
        result = collector.get_book_genre(book_name)
        assert result == expected_genre

    @pytest.mark.parametrize(
        'books_genre, genre_name, expected_books',
        [
            ({data.book1 : data.genre_1, data.book2 : data.genre_2}, data.genre_1, [data.book1]),
            ({data.book1 : data.genre_2, data.book2 : data.genre_2}, data.genre_2, [data.book1, data.book2]),
            ({data.book1 : data.genre_1, data.book2 : data.genre_1}, data.genre_2, []),
        ]
    )
    def test_get_books_with_specific_genre_genre_success(self, collector, books_genre, genre_name, expected_books):
        collector.books_genre = books_genre
        result = collector.get_books_with_specific_genre(genre_name)
        assert result == expected_books

    def test_get_books_genre_success(self, collector):
        collector.books_genre = {data.book1 : data.genre_1, data.book2 : data.genre_2}
        result = collector.get_books_genre()
        assert result == collector.books_genre
