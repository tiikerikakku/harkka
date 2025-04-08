from unittest import TestCase
from repositories.movie import MovieRepository
from db import connection, clear

class UserrepoTest(TestCase):
    def setUp(self):
        self._c = connection
        clear()

    def test_can_create_and_list_movie(self):
        q = MovieRepository(self._c)

        q.create_movie('les parapluies de cherbourg', 'musikaali vuodelta 1964')

        self.assertEqual(q.get_movies(), ['les parapluies de cherbourg'])
