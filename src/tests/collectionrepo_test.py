from unittest import TestCase
from repositories.user import UserRepository
from repositories.movie import MovieRepository
from repositories.collection import CollectionRepository
from db import connection, clear

class CollectionrepoTest(TestCase):
    def setUp(self):
        self._c = connection
        clear()

    def test_can_create_user_movie_and_collect(self):
        q = UserRepository(self._c)
        w = MovieRepository(self._c)
        e = CollectionRepository(self._c)

        uid = q.create_user('billy')
        mid = w.create_movie('happy end', '')

        e.add_to_collection(uid, mid)

        self.assertEqual(e.get_user_collection_formatted(uid), ['happy end [1]'])

    def test_can_remove_movie_from_collection(self):
        q = UserRepository(self._c)
        w = MovieRepository(self._c)
        e = CollectionRepository(self._c)

        uid = q.create_user('jessica')
        mids = [w.create_movie('stormskärs maja', ''), w.create_movie('lilja 4-ever', '')]
        cids = [e.add_to_collection(uid, mids[0]), e.add_to_collection(uid, mids[1])]

        e.remove_from_collection(cids[0])

        self.assertEqual(e.get_user_collection_formatted(uid), ['lilja 4-ever [2]'])
