from unittest import TestCase
from repositories.user import UserRepository
from db import connection, clear

class UserrepoTest(TestCase):
    def setUp(self):
        self._c = connection
        clear()

    def test_can_create_and_list_user(self):
        q = UserRepository(self._c)

        q.create_user('amanda')

        self.assertEqual(q.get_users_formatted(), ['amanda [1]'])
