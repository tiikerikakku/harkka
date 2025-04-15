class UserRepository:
    def __init__(self, connection):
        self._c = connection

    def get_users_formatted(self):
        c = self._c.cursor()

        return [f'{x[1]} [{x[0]}]' for x in c.execute('select * from users').fetchall()]

    def create_user(self, name):
        c = self._c.cursor()
        c.execute('insert into users (user) values (?)', (name,))
        self._c.commit()

        return c.lastrowid
