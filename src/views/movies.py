from tkinter import ttk, font, Listbox, StringVar, IntVar, messagebox
from os import environ
from themoviedb import TMDb
from services.movielibrary import movie_library
from helpers import id_from_list_item

# blame tkinter
# pylint: disable=too-many-statements

class MoviesView:
    def __init__(self, root, actions, mode):
        self._m = mode

        if self._m[0] == 'find':
            self._movie_list = mode[1]
        else:
            self._movie_list = movie_library.get_movies()

        self._r = root
        self._f = ttk.Frame(self._r, padding=(0, 15))

        self._a = actions

        self._tmdb = TMDb(language='fi-FI', region='FI')

        ttk.Label(self._f, text='elokuvien hallinta', font=font.Font(weight='bold')).pack()

        movies = Listbox(
            self._f, height=5, width=50, listvariable=StringVar(value=self._movie_list)
        )
        movies.pack()

        if self._m[0] == 'default':
            add = ttk.Button(
                self._f,
                text='lisää omaan kokoelmaan',
                padding=(5, 0),
                command=lambda: self._movie_to_collection(movies.curselection())
            )

            add.pack(pady=5)
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

            if 'TMDB_KEY' in environ:
                find = ttk.Button(
                    self._f,
                    text='hae nimellä verkosta',
                    padding=(5, 0),
                    command=lambda: self._find_movie(movie.get())
                )
                find.pack(pady=5)

            ttk.Label(self._f, text='kuvaus').pack()
            description = ttk.Entry(self._f)
            description.pack()

        collect = IntVar(value=1)
        ttk.Checkbutton(self._f, text='lisää suoraan omaan kokoelmaan', variable=collect).pack()

        if self._m[0] == 'default':
            create = ttk.Button(
                self._f,
                text='luo',
                padding=(5, 0),
                command=lambda: self._create_movie(movie.get(), description.get(), collect.get())
            )
            create.pack(pady=5)

        if self._m[0] == 'find':
            create = ttk.Button(
                self._f,
                text='valitse',
                padding=(5, 0),
                command=lambda: self._create_movie_tmdb(movies.curselection(), collect.get())
            )
            create.pack(pady=5)

        if self._m[0] == 'find':
            back = ttk.Button(
                self._f,
                text='takaisin',
                padding=(5, 0),
                command=self._to_movies
            )
            back.pack(pady=5)

        self._f.pack()

    def _to_user(self):
        self._f.destroy()
        self._a['user']()

    def _to_movies(self):
        self._f.destroy()
        self._a['movies']()

    def _create_movie(self, name, description, collect):
        if movie_library.create_movie(name, description, collect):
            self._f.destroy()
            self._a['movies']()
        else:
            messagebox.showerror(message='elokuvaa ei voitu luoda')

    def _create_movie_tmdb(self, selection, collect):
        if selection:
            movie = self._tmdb.movie(id_from_list_item(self._movie_list[selection[0]])).details()
            self._create_movie(movie.title, movie.overview, collect)
        else:
            messagebox.showerror(message='et ole valinnut elokuvaa!!')

    def _movie_to_collection(self, selection):
        if selection:
            if movie_library.collection_add(id_from_list_item(self._movie_list[selection[0]])):
                messagebox.showinfo(message='lisätty')
            else:
                messagebox.showerror(message='elokuvaa ei voitu lisätä kokoelmaan')
        else:
            messagebox.showerror(message='et ole valinnut elokuvaa!!')

    def _find_movie(self, name):
        self._f.destroy()

        # it's just how it is
        # pylint: disable=line-too-long

        self._a['movies'](
            ['find',
             [f'{x.title} ({x.original_title}{f", {x.release_date.year}" if x.release_date else ""}) [{x.id}]'
              for x in self._tmdb.search().movies(name).results]]
        )

        # pylint: enable=line-too-long
