from tkinter import ttk, font, Listbox, StringVar, messagebox
from services.movielibrary import movie_library
from helpers import id_from_list_item

class UserView:
    def __init__(self, root, actions):
        self._collection_list = movie_library.get_collection()

        self._r = root
        self._f = ttk.Frame(self._r, padding=(0, 15))

        self._a = actions

        ttk.Label(self._f, text='omat elokuvasi', font=font.Font(weight='bold')).pack()

        movies = ttk.Button(
            self._f,
            text='elokuvien hallinta',
            padding=(5, 0),
            command=self._to_movies
        )
        movies.pack(pady=5)

        collected = Listbox(self._f, height=5, listvariable=StringVar(value=self._collection_list))
        collected.pack()

        remove = ttk.Button(
            self._f,
            text='poista kokoelmasta',
            padding=(5, 0),
            command=lambda: self._remove_from_collection(collected.curselection())
        )
        remove.pack(pady=5)

        logout = ttk.Button(
            self._f,
            text='kirjaudu ulos',
            padding=(5, 0),
            command=self._sign_out
        )
        logout.pack(pady=5)

        self._f.pack()

    def _sign_out(self):
        movie_library.sign_out()
        self._f.destroy()
        self._a['sign_in']()

    def _to_movies(self):
        self._f.destroy()
        self._a['movies']()

    def _remove_from_collection(self, selection):
        if selection:
            movie_library.collection_remove(id_from_list_item(self._collection_list[selection[0]]))
            self._f.destroy()
            self._a['user']()
        else:
            messagebox.showerror(message='et ole valinnut elokuvaa!!')
