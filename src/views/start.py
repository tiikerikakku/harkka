from tkinter import ttk, font, Listbox, StringVar, messagebox
from services.movielibrary import movie_library
from helpers import id_from_list_item

class StartView:
    def __init__(self, root, actions):
        self._user_list = movie_library.get_users()

        self._r = root
        self._f = ttk.Frame(self._r, padding=(0, 15))

        self._a = actions

        ttk.Label(
            self._f,
            text='tervetuloa elokuvakirjastoosi',
            font=font.Font(weight='bold')
        ).pack()

        ttk.Label(self._f, text='valitse käyttäjätili', padding=(0, 15)).pack()
        users = Listbox(self._f, height=5, listvariable=StringVar(value=self._user_list))
        users.pack()
        login = ttk.Button(
            self._f, text='kirjaudu',
            padding=(5, 0),
            command=lambda: self._sign_in(users.curselection())
        )
        login.pack(pady=5)

        ttk.Label(
            self._f,
            text='~~~~ luo tili ~~~~',
            padding=(0, 15),
            font=font.Font(weight='bold', size=10)
        ).pack()
        ttk.Label(self._f, text='nimesi').pack()
        username = ttk.Entry(self._f)
        username.pack()
        register = ttk.Button(
            self._f,
            text='rekisteröidy',
            padding=(5, 0),
            command=lambda: self._create_user(username.get())
        )
        register.pack(pady=5)

        self._f.pack()

    def _sign_in(self, selection):
        if selection:
            movie_library.sign_in(id_from_list_item(self._user_list[selection[0]]))
            self._f.destroy()
            self._a['user']()
        else:
            messagebox.showerror(message='et ole valinnut käyttäjää!!')

    def _create_user(self, name):
        if movie_library.create_user(name):
            messagebox.showinfo(message='käyttäjä luotu; siirrytään järjestelmään')
            self._f.destroy()
            self._a['user']()
        else:
            messagebox.showerror(
                message='käyttäjän luominen ei onnistunut; tarkista ettei nimi ole jo varattu'
            )
