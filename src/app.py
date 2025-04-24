from tkinter import Tk
from views.start import StartView
from views.user import UserView
from views.movies import MoviesView

class UI:
    def __init__(self, root):
        self._r = root

        self._actions = {
            'user': self._to_user,
            'sign_in': self._to_sign_in,
            'movies': self._to_movies
        }

        self._f = StartView(self._r, self._actions)

    def _to_user(self):
        self._f = UserView(self._r, self._actions)

    def _to_sign_in(self):
        self._f = StartView(self._r, self._actions)

    # not an issue, mode is not modified
    # pylint: disable=dangerous-default-value
    def _to_movies(self, mode=['default']):
        self._f = MoviesView(self._r, self._actions, mode)

    # pylint: enable=dangerous-default-value

w = Tk()

w.title('elokuvakirjasto')
w.minsize(500, 200)

UI(w)

w.mainloop()
