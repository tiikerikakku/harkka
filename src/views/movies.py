from tkinter import ttk, font, Listbox, StringVar, IntVar, messagebox
from sqlite3 import IntegrityError
from db import connection
from repositories.movie import MovieRepository

# blame tkinter
# pylint: disable=too-many-statements

class MoviesView:
    def __init__(self, root, user, actions):
        self._movie_repo = MovieRepository(connection)
        self._movie_list = self._movie_repo.get_movies()

        self._r = root
        self._f = ttk.Frame(self._r, padding=(0, 15))

        self._u = user

        self._a = actions

        ttk.Label(self._f, text='elokuvien hallinta', font=font.Font(weight='bold')).pack()

        movies = Listbox(self._f, height=5, listvariable=StringVar(value=self._movie_list))
        movies.pack()

        logout = ttk.Button(
            self._f,
            text='takaisin omaan näkymään',
            padding=(5, 0),
            command=self._to_user
        )
        logout.pack(pady=5)

        ttk.Label(
            self._f,
            text='~~~~ lisää elokuva ~~~~',
            padding=(0, 15),
            font=font.Font(weight='bold', size=10)
        ).pack()

        ttk.Label(self._f, text='nimi').pack()
        movie = ttk.Entry(self._f)
        movie.pack()

        ttk.Label(self._f, text='kuvaus').pack()
        description = ttk.Entry(self._f)
        description.pack()

        collect = IntVar(value=1)
        ttk.Checkbutton(self._f, text='lisää suoraan omaan kokoelmaan', variable=collect).pack()

        create = ttk.Button(
            self._f,
            text='luo',
            padding=(5, 0),
            command=lambda: self._create_movie(movie.get(), description.get(), collect.get())
        )
        create.pack(pady=5)

        self._f.pack()

    def _to_user(self):
        self._f.destroy()
        self._a['user'](self._u)

    def _create_movie(self, name, description, collect):
        try:
            print(collect)
            self._movie_repo.create_movie(name, description)
            messagebox.showinfo(message='elokuva luotu')
            self._f.destroy()
            self._a['movies'](self._u)
        except IntegrityError:
            messagebox.showerror(message='elokuvaa ei voitu luoda')
