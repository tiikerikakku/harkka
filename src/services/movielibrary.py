from sqlite3 import IntegrityError
from themoviedb import TMDb
from db import connection
from repositories.user import UserRepository
from repositories.collection import CollectionRepository
from repositories.movie import MovieRepository

class MovielibraryService:
    def __init__(self):
        self._ur = UserRepository(connection)
        self._cr = CollectionRepository(connection)
        self._mr = MovieRepository(connection)
        self._user = None

        self._tmdb = TMDb(language='fi-FI', region='FI')

    def sign_in(self, user):
        self._user = user

    def sign_out(self):
        self._user = None

    def create_user(self, user):
        try:
            self._user = self._ur.create_user(user)
            return True
        except IntegrityError:
            return False

    def create_movie(self, movie, desc, collect):
        try:
            mid = self._mr.create_movie(movie, desc)
            if collect:
                self._cr.add_to_collection(self._user, mid)

            return True
        except IntegrityError:
            return False

    def collection_add(self, mid):
        try:
            self._cr.add_to_collection(self._user, mid)
            return True
        except IntegrityError:
            return False

    def collection_remove(self, cid):
        self._cr.remove_from_collection(cid)

    def get_users(self):
        return self._ur.get_users_formatted()

    def get_collection(self):
        return self._cr.get_user_collection_formatted(self._user)

    def get_movies(self):
        return self._mr.get_movies_formatted()

    def tmdb_list(self, name):
        # it's just how it is
        # pylint: disable=line-too-long

        return [f'{x.title} ({x.original_title}{f", {x.release_date.year}" if x.release_date else ""}) [{x.id}]'
                for x in self._tmdb.search().movies(name).results]

        # pylint: enable=line-too-long

    def tmdb_details(self, tmdb):
        x = self._tmdb.movie(tmdb).details()

        return (x.title, x.overview)

movie_library = MovielibraryService()
