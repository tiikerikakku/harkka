from tkinter import Tk
from views.start import StartView
from views.user import UserView
from views.movies import MoviesView
from views.item import ItemView

class UI:
    '''main ui class for the application'''

    def __init__(self, root):
        '''inits instance
        
        Args:
            root: tkinter toplevel widget
        '''

        self._r = root

        self._actions = {
            'user': self._to_user,
            'sign_in': self._to_sign_in,
            'movies': self._to_movies,
            'item': self._to_item
        }

        self._f = StartView(self._r, self._actions)

    def _to_user(self):
        '''instructs app to go to user view'''

        self._f = UserView(self._r, self._actions)

    def _to_sign_in(self):
        '''instructs app to go to sign in view'''

        self._f = StartView(self._r, self._actions)

    def _to_movies(self, mode=('default',)):
        '''instructs app to go to movies view

        Args:
            mode: optional value that can be used to
                  determine what content shall be shown
        '''

        self._f = MoviesView(self._r, self._actions, mode)

    def _to_item(self, cid):
        '''instructs app to go to item view

        Args:
            cid: collection id of item
        '''

        self._f = ItemView(self._r, self._actions, cid)

w = Tk()

w.title('elokuvakirjasto')
w.minsize(500, 200)

UI(w)

w.mainloop()
