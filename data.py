book_1 = 'Q'
book_2 = 'Тени у забытой реки среди снов или огня!'
book_3 = 'Вокруг света за 80 дней'
book_4 = 'Крокодил Гена и его друзья'
book_5 = 'Ревизор'

genre_1 = 'Ужасы'
genre_2 = 'Детективы'
genre_3 = 'Фантастика'
genre_4 = 'Мультфильмы'
genre_5 = 'Комедии'

books_genre_all = {book_1 : genre_1, book_2: genre_2, book_3: genre_3, book_4: genre_4, book_5: genre_5}

#for test_get_books_with_specific_genre_genre_success
books_genre_filter_one = {book_1 : genre_1, book_2: genre_2, book_3: genre_3, book_4: genre_4}
books_genre_filter_many = {book_1 : genre_1, book_2: genre_2, book_3: genre_3, book_4: genre_2}
books_genre_filter_empty = {book_3 : genre_3, book_4: genre_4}

expected_books_genre_one = [book_2]
expected_books_genre_many = [book_2, book_4]

#for test_get_books_for_children_books_genre_success
books_genre_filter_children_one = {book_1 : genre_1, book_3: genre_3}
books_genre_filter_children_empty = {book_1 : genre_1, book_2 : genre_2}

expected_children_books_many = [book_3, book_4, book_5]
expected_children_books_one = [book_3]

#for test_add_book_in_favorite_book_success
books_genre_add_favorites_book_empty = {book_2 : genre_2, book_4: genre_4}

expected_favorites = [book_1]

#for test_delete_book_from_favorites_book_success
favorites_book_exist = [book_1, book_2, book_3]
favorites_book_not_exist = [book_3, book_4]

expected_favorites_book_deleted = [book_1, book_3]