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

    def get_collected_item(self, cid):
        '''get item from collection

        Args:
            cid: collection id

        Returns:
            item details as tuple
        '''

        c = self._c.cursor()
        return c.execute('''select movies.movie, movies.info, collected.rating
                         from collected, movies
                         where collected.id = ?
                         and collected.movie = movies.id''', (cid,)).fetchone()

    def set_rating(self, cid, rating):
        '''set item rating

        Args:
            cid: collection id
            rating: rating to be set
        '''

        c = self._c.cursor()
        c.execute('update collected set rating = ? where id = ?', (rating, cid))
        self._c.commit()

    def mean_rating(self, cid):
        '''get mean rating for item

        Args:
            cid: collection id

        Returns:
            item mean rating in a tuple
        '''

        c = self._c.cursor()
        return c.execute('''select avg(rating) from collected
                         where movie = (select movie from collected where id = ?)
                         and rating between 1 and 5''', (cid,)).fetchone()

    def other_collectors(self, cid):
        '''get names of other collectors of an item

        Args:
            cid: collection id

        Returns:
            list of user names as tuples
        '''

        c = self._c.cursor()
        return c.execute('''select users.user from collected, users
                         where collected.movie = (select collected.movie
                         from collected where id = ?)
                         and collected.user = users.id
                         and collected.id != ?''', (cid, cid)).fetchall()
