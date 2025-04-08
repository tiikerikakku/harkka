class MovieRepository:
    def __init__(self, connection):
        self._c = connection

    def get_movies(self):
        c = self._c.cursor()

        return [x[1] for x in c.execute('select * from movies').fetchall()]

    def create_movie(self, name, description):
        c = self._c.cursor()
        c.execute('insert into movies (movie, info) values (?, ?)', (name, description))
        self._c.commit()

        return name
