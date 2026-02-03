import pytest
import data

class TestBooksCollector:

    @pytest.mark.parametrize(
        'book_name, expected_books_genre',
        [
            (data.book_1, {data.book_1 : ''}),
            (data.book_6, {})
        ]
    )
    def test_add_new_book_book_success(self, collector, book_name, expected_books_genre):
        collector.add_new_book(book_name)
        assert collector.books_genre == expected_books_genre

        collector.add_new_book(book_name)
        assert collector.books_genre == expected_books_genre

    def test_set_book_genre_genre_success(self, collector):
        collector.books_genre = {data.book_1 : ''}
        collector.set_book_genre(data.book_1, data.genre_1)
        assert collector.books_genre[data.book_1] == data.genre_1

    @pytest.mark.parametrize(
        'books_genre, book_name, expected_genre',
        [
            ({data.book_1 : data.genre_1}, data.book_1, data.genre_1),
            ({data.book_2 : ''}, data.book_2, ''),
            ({}, data.book_1, None)
        ]
    )
    def test_get_book_genre_book_success(self, collector, books_genre, book_name, expected_genre):
        collector.books_genre = books_genre
        assert collector.get_book_genre(book_name) == expected_genre

    @pytest.mark.parametrize(
        'books_genre, genre_name, expected_books',
        [
            (data.books_genre_filter_one, data.genre_2, data.expected_books_genre_one),
            (data.books_genre_filter_many, data.genre_2, data.expected_books_genre_many),
            (data.books_genre_filter_empty, data.genre_2, []),
        ]
    )
    def test_get_books_with_specific_genre_genre_success(self, collector, books_genre, genre_name, expected_books):
        collector.books_genre = books_genre
        assert collector.get_books_with_specific_genre(genre_name) == expected_books

    def test_get_books_genre_success(self, collector):
        collector.books_genre = data.books_genre_all
        assert collector.get_books_genre() == collector.books_genre

    @pytest.mark.parametrize(
        'books_genre, expected_children_books',
        [
            (data.books_genre_all, data.expected_children_books_many),
            (data.books_genre_filter_children_one, data.expected_children_books_one),
            (data.books_genre_filter_children_empty, [])
        ]
    )
    def test_get_books_for_children_books_genre_success(self, collector, books_genre, expected_children_books):
        collector.books_genre = books_genre
        assert collector.get_books_for_children() == expected_children_books

    @pytest.mark.parametrize(
        'books_genre, book_to_add, expected_favorites',
        [
            (data.books_genre_all, data.book_1, data.expected_favorites),
            (data.books_genre_add_favorites_book_empty, data.book_1, []),
        ]
    )
    def test_add_book_in_favorite_book_success(self, collector, books_genre, book_to_add, expected_favorites):
        collector.books_genre = books_genre
        collector.add_book_in_favorites(book_to_add)
        assert collector.favorites == expected_favorites

        collector.add_book_in_favorites(book_to_add)
        assert collector.favorites == expected_favorites

    @pytest.mark.parametrize(
        'favorites, book_to_delete, expected_favorites',
        [
            (data.favorites_book_exist, data.book_2, data.expected_favorites_book_deleted),
            (data.favorites_book_not_exist, data.book_2, data.favorites_book_not_exist)
        ]
    )
    def test_delete_book_from_favorites_book_success(self, collector, favorites, book_to_delete, expected_favorites):
        collector.favorites = favorites
        collector.delete_book_from_favorites(book_to_delete)
        assert collector.favorites == expected_favorites

    def test_get_list_of_favorites_books_success(self, collector):
        collector.favorites = [data.book_1, data.book_5]
        assert collector.get_list_of_favorites_books() == [data.book_1, data.book_5]
