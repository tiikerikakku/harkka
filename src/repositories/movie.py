class MovieRepository:
    '''movie repository class'''
    def __init__(self, connection):
        '''init instance

        Args:
            connection: db connection
        '''

        self._c = connection

    def get_movies_formatted(self):
        '''get formatted list of movies

        Returns:
            formatted list of movies
        '''

        c = self._c.cursor()

        return [f'{x[1]} [{x[0]}]' for x in c.execute('select * from movies').fetchall()]

    def create_movie(self, name, description):
        '''create movie

        Args:
            name: name of movie
            description: description for movie

        Returns:
            movie id
        '''

        c = self._c.cursor()
        c.execute('insert into movies (movie, info) values (?, ?)', (name, description))
        self._c.commit()

        return c.lastrowid
