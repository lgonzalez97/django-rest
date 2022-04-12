import pytest
from library.books.models import *

@pytest.mark.django_db
@pytest.mark.parametrize(
	'nombre , apellido',
	(
		('Paul','Coelho'),
		('Haruki','Murakami'),
		('Garcia','Marquez'),
	)
)

@pytest.mark.django_db
def test_author_name(nombre, apellido):
    author = Author.objects.create(name='nombre', last_name='apellido')
    print('This is my authors name:',nombre)
    print('In case you wanna know this author full name:',nombre, apellido)
    assert author.name == 'nombre'
    assert author.last_name == 'apellido'
    assert Author.objects.all().count() == 1
    author.delete()
    assert Author.objects.all().count() == 0
    
@pytest.mark.django_db
@pytest.mark.parametrize(
	'genre_name',
	(
		('Horror'),
		('Fantasy'),
		('Sci-Fi'),
	)
)

@pytest.mark.django_db
def test_genre_name(genre_name):
    genre = Genre.objects.create(gen_name='genre_name')
    set1 = set("genre_name")
    set2 = set("genre_name")
    print('This is my book genre:',genre_name)
    assert genre.gen_name == 'genre_name'
    assert set1 == set2
    assert Genre.objects.all().count() == 1
    genre.delete()


@pytest.mark.django_db
@pytest.mark.parametrize(
	'editorial_name, phone_n',
	(
		('Awesome books', 31256),
		('Besto editorialu', 31256),
		('Totally real editorial', 31256),
	)
)
@pytest.mark.django_db
def test_editorial_name(editorial_name, phone_n):
    editorial = Editorial.objects.create(edi_name='editorial_name',phone=phone_n)
    set1 = set("editorial_name")
    set2 = set("editorial_name")
    print('The editorial for this book is:',editorial_name)
    print('You can contact this editorial with this phone number:', phone_n)
    assert editorial.edi_name == "editorial_name"
    assert editorial.phone == phone_n
    assert set1 == set2
    assert Editorial.objects.all().count() == 1
    editorial.delete()

@pytest.mark.django_db
@pytest.mark.parametrize(
	'language_n',
	(
		('English'),
		('Spanish'),
		('Chinese'),
	)
)
@pytest.mark.django_db
def test_language(language_n):
    language = Language.objects.create(language='language_n')
    print('This is my book genre:',language_n)
    assert language.language == 'language_n'
    assert Language.objects.all().count() == 1
    language.delete()
	
@pytest.mark.django_db
@pytest.mark.parametrize(
	'nombre , apellido',
	(
		('Paul','Coelho'),
		('Haruki','Murakami'),
		('Garcia','Marquez'),
	)
)

@pytest.mark.django_db
def test_author_with_monkey(monkeypatch,nombre,apellido):
    author = Author.objects.create(name = 'nombre', last_name = 'apellido')
    def model_count_mock():
       return 'Kevin'
    
    monkeypatch.setattr(author,'name', 'Kevin')
    assert author.name == 'Kevin'
    print('Making the monkeypatch')

# @pytest.mark.django_db
# def test_editorial_phone(phone_n):
#     editorial = Editorial.objects.create(phone=phone_n)
#     print('You can contact this editorial with this phone number:',phone_n)
#     assert editorial.phone == phone_n
#     assert Editorial.objects.all().count() == 1
#     editorial.delete()

# @pytest.mark.django_db
# def test_author_with_monkey(monkeypatch):
#         author = Author.objects.create(name='nombre', last_name='apellido')
#     def model_count_mock():
#         return 4

#     monkeypatch.setattr(Author.objects.all(), 'count',model_count_mock)
#     assert Author.objects.all().count() == 4
#     print('Haciendo el mokeypatch')