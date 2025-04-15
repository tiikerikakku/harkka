from unittest import TestCase
from helpers import id_from_list_item

class CollectionrepoTest(TestCase):
    def test_ifli_helper(self):
        self.assertEqual(id_from_list_item('[[monimutkainen]] [nimi]'), 'nimi')
