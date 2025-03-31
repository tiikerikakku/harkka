from tkinter import Tk
from views.start import StartView
from views.movielist import MovielistView

class UI:
  def __init__(self, root):
    self._r = root
    self._f = StartView(self._r, self._to_movielist)

  def _to_movielist(self, user):
    self._f = MovielistView(self._r, user, self._to_sign_in)

  def _to_sign_in(self):
    self._f = StartView(self._r, self._to_movielist)

w = Tk()

w.title('elokuvakirjasto')
w.minsize(500, 200)

UI(w)

w.mainloop()
