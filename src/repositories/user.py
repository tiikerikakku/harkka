class UserRepository:
    '''user repository class'''

    def __init__(self, connection):
        '''init instance

        Args:
            connection: db connection
        '''

        self._c = connection

    def get_users_formatted(self):
        '''get formatted list of users

        Returns:
            formatted list of users
        '''

        c = self._c.cursor()

        return [f'{x[1]} [{x[0]}]' for x in c.execute('select * from users').fetchall()]

    def create_user(self, name):
        '''create user

        Args:
            name: user name

        Returns:
            user id
        '''

        c = self._c.cursor()
        c.execute('insert into users (user) values (?)', (name,))
        self._c.commit()

        return c.lastrowid
