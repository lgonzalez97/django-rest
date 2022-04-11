import pytest
from library.books.models import *

@pytest.mark.django_db
@pytest.mark.parametrize(
	'nombre , apellido',
	(
		('Paul','Coelho'),
		('Haruki','Murakami),
		('Garcia','Marquez'),
	)
)

@pytest.mark.django_db
def test_author_name(nombre, apellido):
    author = Author.objects.create(name='nombre', last_name='apellido')
    print('This is my authors name:',author.name)
    assert author.last_name == 'apellido'
    assert Author.objects.all().count() == 1
    author.delete()
    assert Author.objects.all().count() == 0
    

@pytest.mark.django_db
def test_genre_name():
    genre = Genre.objects.create(gen_name='Fantasy')
    print('This is my book genre:', genre.gen_name)
    assert genre.gen_name == 'Fantasy'
    assert Genre.objects.all().count() == 1
    genre.delete()

@pytest.mark.django_db
def test_editorial_name():
    editorial = Editorial.objects.create(edi_name='Awesome Books',phone='31523')
    print('The editorial for this book is:',editorial.edi_name)
    assert editorial.edi_name == "Awesome Books"
    assert Editorial.objects.all().count() == 1
    editorial.delete()

@pytest.mark.django_db
def test_editorial_phone():
    editorial = Editorial.objects.create(phone='31523')
    print('You can contact this editorial with this phone number:',editorial.phone)
    assert editorial.phone == "31523"
    assert Editorial.objects.all().count() == 1
    editorial.delete()

# @pytest.mark.django_db
# def test_author_with_monkey(monkeypatch):
#         author = Author.objects.create(name='nombre', last_name='apellido')
#     def model_count_mock():
#         return 4

#     monkeypatch.setattr(Author.objects.all(), 'count',model_count_mock)
#     assert Author.objects.all().count() == 4
#     print('Haciendo el mokeypatch')