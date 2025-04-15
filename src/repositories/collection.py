class CollectionRepository:
    def __init__(self, connection):
        self._c = connection

    def get_user_collection_formatted(self, uid):
        c = self._c.cursor()

        return (
            [f'{x[1]} [{x[0]}]' for x in
             c.execute('''select collected.id, movies.movie from movies, collected
                       where collected.movie = movies.id and user = ?''', (uid,))
             .fetchall()
            ]
        )

    def add_to_collection(self, uid, mid):
        c = self._c.cursor()
        c.execute('insert into collected (user, movie) values (?, ?)', (uid, mid))
        self._c.commit()

        return c.lastrowid

    def remove_from_collection(self, cid):
        c = self._c.cursor()
        c.execute('delete from collected where id = ?', (cid,))
        self._c.commit()
