from tkinter import ttk, font, Listbox, StringVar

class UserView:
    def __init__(self, root, user, back):
        self._r = root
        self._f = ttk.Frame(self._r, padding=(0, 15))

        self._b = back

        ttk.Label(self._f, text='omat elokuvasi', font=font.Font(weight='bold')).pack()

        logout = ttk.Button(
            self._f,
            text='kirjaudu ulos',
            padding=(5, 0),
            command=self._sign_out
        )
        logout.pack(pady=5)

        self._f.pack()

    def _sign_out(self):
        self._f.destroy()
        self._b()
