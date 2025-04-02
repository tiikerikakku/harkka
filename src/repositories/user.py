class UserRepository:
    def __init__(self, connection):
        self._c = connection

    def get_users(self):
        c = self._c.cursor()

        return [x[1] for x in c.execute('select * from users').fetchall()]

    def create_user(self, name):
        c = self._c.cursor()
        c.execute('insert into users (user) values (?)', (name,))
        self._c.commit()

        return name
