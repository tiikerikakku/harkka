from tkinter import ttk, font, Listbox, StringVar, IntVar, messagebox
from os import environ
from services.movielibrary import movie_library
from helpers import id_from_list_item

# blame tkinter
# pylint: disable=too-many-statements

class MoviesView:
    '''movie view ui class'''

    def __init__(self, root, actions, mode):
        '''init instance

        Args:
            root: tkinter toplevel widget
            actions: list of app actions
            mode: mode, which determines shown elements in view
        '''

        self._m = mode

        if self._m[0] == 'find':
            self._movie_list = mode[1]
        else:
            self._movie_list = movie_library.get_movies()

        self._r = root
        self._f = ttk.Frame(self._r, padding=(0, 15))

        self._a = actions

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
        '''move to user view'''

        self._f.destroy()
        self._a['user']()

    def _to_movies(self):
        '''move to movies view'''

        self._f.destroy()
        self._a['movies']()

    def _create_movie(self, name, description, collect):
        '''create movie

        Args:
            name: movie name
            description: movie description
            collect: bool that determines if created movie should be added to user's collection
        '''

        if movie_library.create_movie(name, description, collect):
            self._f.destroy()
            self._a['movies']()
        else:
            messagebox.showerror(message='elokuvaa ei voitu luoda')

    def _create_movie_tmdb(self, selection, collect):
        '''create movie with tmdb data

        Args:
            selection: search result list selection
            collect: bool that determines if created movie should be added to user's collection
        '''

        if selection:
            self._create_movie(
                *movie_library.tmdb_details(id_from_list_item(self._movie_list[selection[0]])),
                collect
            )
        else:
            messagebox.showerror(message='et ole valinnut elokuvaa!!')

    def _movie_to_collection(self, selection):
        '''add movie to user collection

        Args:
            selection: movie list selection
        '''

        if selection:
            if movie_library.collection_add(id_from_list_item(self._movie_list[selection[0]])):
                messagebox.showinfo(message='lisätty')
            else:
                messagebox.showerror(message='elokuvaa ei voitu lisätä kokoelmaan')
        else:
            messagebox.showerror(message='et ole valinnut elokuvaa!!')

    def _find_movie(self, name):
        '''find movie through tmdb and show results

        Args:
            name: search term
        '''

        self._f.destroy()
        self._a['movies'](('find', movie_library.tmdb_list(name)))
