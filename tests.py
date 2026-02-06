import pytest
import data

class TestBooksCollector:

    def test_add_new_book_new_book_added_successfully(self, collector):
        collector.add_new_book(data.book_1)
        assert collector.books_genre == {data.book_1 : ''}

    def test_add_new_book_existing_book_shows_no_change(self, collector):
        collector.add_new_book(data.book_1)
        collector.add_new_book(data.book_1)
        assert collector.books_genre == {data.book_1 : ''}

    def test_set_book_genre_existing_book_genre_updated(self, collector):
        collector.books_genre = {data.book_1 : ''}
        collector.set_book_genre(data.book_1, data.genre_1)
        assert collector.books_genre[data.book_1] == data.genre_1

    def test_get_book_genre_existing_book_returns_genre(self, collector):
        collector.books_genre = {data.book_1 : data.genre_1}
        assert collector.get_book_genre(data.book_1) == data.genre_1

    @pytest.mark.parametrize(
        'books_genre, genre_name, expected_books',
        [
            (data.books_genre_filter_one, data.genre_2, data.expected_books_genre_one),
            (data.books_genre_filter_many, data.genre_2, data.expected_books_genre_many),
            (data.books_genre_filter_empty, data.genre_2, []),
        ],
        ids=[
            'one_book_in_genre_returns_book', 'many_books_in_genre_returns_books', 'empty_books_for_genre_returns_empty_list'
        ]
    )
    def test_get_books_with_specific_genre(self, collector, books_genre, genre_name, expected_books):
        collector.books_genre = books_genre
        assert collector.get_books_with_specific_genre(genre_name) == expected_books

    def test_get_books_genre_all_books_returns_all_books_genre(self, collector):
        collector.books_genre = data.books_genre_all
        assert collector.get_books_genre() == data.books_genre_all

    @pytest.mark.parametrize(
        'books_genre, expected_children_books',
        [
            (data.books_genre_filter_children_one, data.expected_children_books_one),
            (data.books_genre_all, data.expected_children_books_many),
            (data.books_genre_filter_children_empty, [])
        ],
        ids=['one_children_book_returns_book', 'many_children_books_returns_books', 'empty_books_for_children_returns_empty_list']
    )
    def test_get_books_for_children(self, collector, books_genre, expected_children_books):
        collector.books_genre = books_genre
        assert collector.get_books_for_children() == expected_children_books

    @pytest.mark.parametrize(
        'books_genre, book_to_add, expected_favorites',
        [
            (data.books_genre_all, data.book_1, data.expected_favorites),
            (data.books_genre_add_favorites_book_empty, data.book_1, []),
        ],
        ids=['exising_book_added_successfully','not_existing_book_shows_no_change']
    )
    def test_add_book_in_favorites(self, collector, books_genre, book_to_add, expected_favorites):
        collector.books_genre = books_genre
        collector.add_book_in_favorites(book_to_add)
        assert collector.favorites == expected_favorites

    @pytest.mark.parametrize(
        'favorites, book_to_delete, expected_favorites',
        [
            (data.favorites_book_exist, data.book_2, data.expected_favorites_book_deleted),
            (data.favorites_book_not_exist, data.book_2, data.favorites_book_not_exist)
        ],
        ids=['existing_book_deleted_successfully', 'not_existing_book_shows_no_change']
    )
    def test_delete_book_from_favorites(self, collector, favorites, book_to_delete, expected_favorites):
        collector.favorites = favorites
        collector.delete_book_from_favorites(book_to_delete)
        assert collector.favorites == expected_favorites

    def test_get_list_of_favorites_books_two_books_returns_list(self, collector):
        collector.favorites = data.favorites_books_list
        assert collector.get_list_of_favorites_books() == data.favorites_books_list