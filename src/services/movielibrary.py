from sqlite3 import IntegrityError
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
        
    def get_users(self):
        return self._ur.get_users_formatted()
        
    def get_collection(self):
        return self._cr.get_user_collection_formatted(self._user)
    
    def get_movies(self):
        return self._mr.get_movies_formatted()

movie_library = MovielibraryService()
