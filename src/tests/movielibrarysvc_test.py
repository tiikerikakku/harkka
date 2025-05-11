from unittest import TestCase
from services.movielibrary import movie_library
from db import clear

class MovielibrarysvcTest(TestCase):
    def setUp(self):
        clear()

    def test_basic_functionality(self):
        movie_library.create_user('Amy')

        movie_library.sign_out()

        self.assertEqual(movie_library.get_users(), ['Amy [1]'])

        movie_library.sign_in(1)

        self.assertEqual(movie_library._user, 1)

        movie_library.create_movie('The Substance', 'Academy Awards - ja BAFTA-nominoitu', True)

        self.assertEqual(movie_library.get_collection(), ['The Substance [1]'])

        movie_library.rate_item(1, 4)

        self.assertEqual(movie_library.get_item(1), (
            'The Substance', 'Academy Awards - ja BAFTA-nominoitu', 4, 4.0, 'ei kukaan'
        ))

        self.assertEqual(movie_library.get_movies(), ['The Substance [1]'])

        movie_library.create_movie('Flow', 'Elokuva eräästä kissasta', False)
        movie_library.collection_add(2)

        self.assertEqual(movie_library.get_item(2), (
            'Flow', 'Elokuva eräästä kissasta', 0, 'ei arvioita', 'ei kukaan'
        ))

        movie_library.collection_remove(2)

        self.assertEqual(movie_library.get_collection(), ['The Substance [1]'])

        movie_library.sign_out()

        movie_library.create_user('Vili')

        movie_library.collection_add(1)

        movie_library.rate_item(2, 5)

        self.assertEqual(movie_library.get_item(2), (
            'The Substance', 'Academy Awards - ja BAFTA-nominoitu', 5, 4.5, 'Amy'
        ))
