from main import BooksCollector
import pytest


class TestBooksCollector:

    def test_add_new_book_add_two_books(self, collector):

        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        assert len(collector.get_books_genre()) == 2

    def test_add_new_book_add_two_identical_books(self, collector):

        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Гордость и предубеждение и зомби')
        assert len(collector.get_books_genre()) == 1

    @pytest.mark.parametrize('len_name', ["КнигаКнигаКнигаКнигаКнигаКнигаКнигаКнига","КнигаКнигаКнигаКнигаКнигаКнигаКнигаКниг"])
    def test_add_new_book_len_name_39_and_40_symbols_negative(self, collector, len_name):

        collector.add_new_book(len_name)
        assert len_name in collector.get_books_genre()

    def test_add_new_book_len_name_41_symbols(self, collector):

        book = "КнигаКнигаКнигаКнигаКнигаКнигаКнигаКнигаK"
        collector.add_new_book(book)
        assert book not in collector.get_books_genre()

    def test_set_book_genre_book_from_list(self, collector):

        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.set_book_genre('Гордость и предубеждение и зомби', 'Ужасы')

        assert collector.books_genre['Гордость и предубеждение и зомби'] == 'Ужасы'

    def test_get_book_genre_matches_assigned_genre(self, collector):

        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.set_book_genre('Гордость и предубеждение и зомби', 'Ужасы')
        collector.get_book_genre('Гордость и предубеждение и зомби')

        assert collector.get_book_genre('Гордость и предубеждение и зомби') == 'Ужасы'

    def test_get_books_with_specific_genre_matches_assigned_book(self, collector):
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('1984')
        collector.set_book_genre('1984', 'Фантастика')
        collector.set_book_genre('Гордость и предубеждение и зомби', 'Ужасы')
        collector.get_books_with_specific_genre('Фантастика')

        assert collector.get_books_with_specific_genre('Фантастика') == ['1984']

    def test_get_books_genre_empty(self, collector):
        books_genre = collector.get_books_genre()

        assert books_genre == {}

    def test_get_books_genre_with_books(self, collector):
        collector.add_new_book('Дядя Федор')
        collector.set_book_genre('Дядя Федор', 'Мультфильмы')
        collector.add_new_book('1984')
        collector.set_book_genre('1984', 'Фантастика')

        assert collector.get_books_genre() == {'Дядя Федор': 'Мультфильмы', '1984': 'Фантастика'}

    def test_get_books_for_children_genre(self, collector):
        collector.add_new_book('Дядя Федор')
        collector.set_book_genre('Дядя Федор', 'Мультфильмы')
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.set_book_genre('Гордость и предубеждение и зомби', 'Ужасы')
        collector.get_books_for_children()

        assert collector.get_books_for_children() == ['Дядя Федор']

    def test_add_book_in_favorites_add_one_book(self, collector):
        collector.add_new_book('Дядя Федор')
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_book_in_favorites('Дядя Федор')

        assert collector.favorites == ['Дядя Федор']

    def test_delete_book_from_favorites_delete_one_book(self, collector):
        collector.add_new_book('Дядя Федор')
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_book_in_favorites('Дядя Федор')
        collector.delete_book_from_favorites('Дядя Федор')

        assert len(collector.favorites) == 0

    def test_get_list_of_favorites_books_one_book(self, collector):
        collector.add_new_book('Дядя Федор')
        collector.add_book_in_favorites('Дядя Федор')

        assert collector.get_list_of_favorites_books() == ['Дядя Федор']

















