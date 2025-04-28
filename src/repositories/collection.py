class CollectionRepository:
    '''collection repository class'''

    def __init__(self, connection):
        '''init instance

        Args:
            connection: db connection
        '''

        self._c = connection

    def get_user_collection_formatted(self, uid):
        '''get formatted list of user collection

        Args:
            uid: user id

        Returns:
            formatted list of user collection
        '''

        c = self._c.cursor()

        return (
            [f'{x[1]} [{x[0]}]' for x in
             c.execute('''select collected.id, movies.movie from movies, collected
                       where collected.movie = movies.id and user = ?''', (uid,))
             .fetchall()
            ]
        )

    def add_to_collection(self, uid, mid):
        '''add movie to user collection

        Args:
            uid: user id
            mid: id of movie to be added

        Returns:
            id for collection item
        '''

        c = self._c.cursor()
        c.execute('insert into collected (user, movie) values (?, ?)', (uid, mid))
        self._c.commit()

        return c.lastrowid

    def remove_from_collection(self, cid):
        '''remove item from collection

        Args:
            cid: collection id
        '''

        c = self._c.cursor()
        c.execute('delete from collected where id = ?', (cid,))
        self._c.commit()
