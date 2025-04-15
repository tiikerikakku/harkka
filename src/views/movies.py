from tkinter import ttk, font, Listbox, StringVar, IntVar, messagebox
from services.movielibrary import movie_library
from helpers import id_from_list_item

# blame tkinter
# pylint: disable=too-many-statements

class MoviesView:
    def __init__(self, root, actions):
        self._movie_list = movie_library.get_movies()

        self._r = root
        self._f = ttk.Frame(self._r, padding=(0, 15))

        self._a = actions

        ttk.Label(self._f, text='elokuvien hallinta', font=font.Font(weight='bold')).pack()

        movies = Listbox(self._f, height=5, listvariable=StringVar(value=self._movie_list))
        movies.pack()

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
        self._a['user']()

    def _create_movie(self, name, description, collect):
        if movie_library.create_movie(name, description, collect):
            messagebox.showinfo(message='elokuva luotu')
            self._f.destroy()
            self._a['movies']()
        else:
            messagebox.showerror(message='elokuvaa ei voitu luoda')

    def _movie_to_collection(self, selection):
        if selection:
            if movie_library.collection_add(id_from_list_item(self._movie_list[selection[0]])):
                messagebox.showinfo(message='lisätty')
            else:
                messagebox.showerror(message='elokuvaa ei voitu lisätä kokoelmaan')
        else:
            messagebox.showerror(message='et ole valinnut elokuvaa!!')
