from sqlite3 import IntegrityError
from themoviedb import TMDb
from db import connection
from repositories.user import UserRepository
from repositories.collection import CollectionRepository
from repositories.movie import MovieRepository

class MovielibraryService:
    '''movie library service that is used by ui to communicate with repos etc.'''

    def __init__(self):
        '''inits instance'''

        self._ur = UserRepository(connection)
        self._cr = CollectionRepository(connection)
        self._mr = MovieRepository(connection)
        self._user = None

        self._tmdb = TMDb(language='fi-FI', region='FI')

    def sign_in(self, user):
        '''signs in a user

        Args:
            user: which user to sign in
        '''

        self._user = user

    def sign_out(self):
        '''signs out user'''

        self._user = None

    def create_user(self, user):
        '''creates a user

        Args:
            user: user name for new user

        Returns:
            True if created, False if not created
        '''

        try:
            self._user = self._ur.create_user(user)
            return True
        except IntegrityError:
            return False

    def create_movie(self, movie, desc, collect):
        '''creates a movie

        Args:
            movie: name of movie
            desc: description for movie
            collect: bool to indicate if a movie is to be added to user's collection

        Returns:
            True if created, False if not created
        '''

        try:
            mid = self._mr.create_movie(movie, desc)
            if collect:
                self._cr.add_to_collection(self._user, mid)

            return True
        except IntegrityError:
            return False

    def collection_add(self, mid):
        '''add movie to user collection

        Args:
            mid: movie id to be added

        Returns:
            True if added, False if not added
        '''

        try:
            self._cr.add_to_collection(self._user, mid)
            return True
        except IntegrityError:
            return False

    def collection_remove(self, cid):
        '''remove movie from collection

        Args:
            cid: id of collected item
        '''

        self._cr.remove_from_collection(cid)

    def get_users(self):
        '''get list of users

        Returns:
            formatted list of movies
        '''

        return self._ur.get_users_formatted()

    def get_collection(self):
        '''get user collection

        Returns:
            formatted list of collected items
        '''

        return self._cr.get_user_collection_formatted(self._user)

    def get_movies(self):
        '''get movies in system

        Returns:
            formatted list of movies
        '''

        return self._mr.get_movies_formatted()

    def tmdb_list(self, name):
        '''list movies based on search term from tmdb

        Args:
            name: search term

        Returns:
            a formatted list with search results
        '''

        # it's just how it is
        # pylint: disable=line-too-long

        return [f'{x.title} ({x.original_title}{f", {x.release_date.year}" if x.release_date else ""}) [{x.id}]'
                for x in self._tmdb.search().movies(name).results]

        # pylint: enable=line-too-long

    def tmdb_details(self, tmdb):
        '''find details based on a tmdb id

        Args:
            tmdb: tmdb id

        Returns:
            tuple with movie title and description
        '''

        x = self._tmdb.movie(tmdb).details()

        return (x.title, x.overview)

movie_library = MovielibraryService()
