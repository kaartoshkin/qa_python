import pytest

from main import BooksCollector

# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:
    @pytest.fixture(autouse=True)
    def collector(self):
        self.collector = BooksCollector()
    # пример теста:
    # обязательно указывать префикс test_
    # дальше идет название метода, который тестируем add_new_book_
    # затем, что тестируем add_two_books - добавление двух книг
    def test_add_new_book_add_two_books(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()

        # добавляем две книги
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        # проверяем, что добавилось именно две
        # словарь books_rating, который нам возвращает метод get_books_rating, имеет длину 2
        assert len(collector.get_books_genre()) == 2

    # напиши свои тесты ниже
    # чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollector()
    @pytest.mark.parametrize("book_name",['','A' * 41])
    def test_add_new_book_invalid_length_book(self, book_name):         
        self.collector.add_new_book(book_name)
        assert book_name not in self.collector.books_genre

    def test_add_new_book_add_existing_book(self):         
        self.collector.add_new_book('Идиот')
        self.collector.add_new_book('Идиот')
        assert len(self.collector.books_genre) == 1

    def test_set_book_genre_success(self):         
        self.collector.add_new_book('Капитал')
        self.collector.set_book_genre('Капитал', 'Фантастика')
        assert self.collector.books_genre ==  {'Капитал':'Фантастика'}    

    def test_get_books_with_specific_genre_success(self):         
        self.collector.add_new_book('Звёздные войны')
        self.collector.set_book_genre('Звёздные войны', 'Фантастика')
        self.collector.add_new_book('Терминатор')
        self.collector.set_book_genre('Терминатор', 'Фантастика')
        self.collector.add_new_book("Колобок")
        self.collector.set_book_genre("Колобок", "Мультфильмы")
        assert  self.collector.get_books_with_specific_genre('Фантастика') == ['Звёздные войны', 'Терминатор']    

    def test_get_book_genre_success(self):         
        self.collector.add_new_book('Гарри Поттер')
        self.collector.set_book_genre('Гарри Поттер', 'Фантастика')
        assert  self.collector.get_book_genre('Гарри Поттер') == ('Фантастика')
                
    def test_get_books_for_children_success(self):        
        self.collector.add_new_book("Колобок")
        self.collector.set_book_genre("Колобок", "Мультфильмы")
        self.collector.add_new_book('Оно')
        self.collector.set_book_genre('Оно', 'Ужасы')
        assert  self.collector.get_books_for_children() == ["Колобок"]

    def test_add_book_in_favorites_success(self):         
        self.collector.add_new_book("1984")  
        self.collector.add_book_in_favorites('1984')
        assert  self.collector.favorites == ['1984']

    def test_add_book_in_favorites_dublicate(self):         
        self.collector.add_new_book("1984")  
        self.collector.add_book_in_favorites('1984')
        self.collector.add_book_in_favorites('1984')
        assert  self.collector.favorites == ['1984']

    def test_delete_book_from_favorites_success(self):        
        self.collector.add_new_book("Ведьмак")
        self.collector.add_book_in_favorites("Ведьмак")
        self.collector.delete_book_from_favorites("Ведьмак")
        assert  self.collector.favorites == []        

    def test_get_list_of_favorites_books_success(self):
        self.collector.add_new_book("Оно")  
        self.collector.add_book_in_favorites('Оно')
        assert  self.collector.get_list_of_favorites_books() == ['Оно']    
        