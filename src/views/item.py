from tkinter import ttk, font, messagebox
from services.movielibrary import movie_library

class ItemView:
    '''item view ui class'''

    def __init__(self, root, actions, cid):
        '''init instance

        Args:
            root: tkinter toplevel widget
            actions: list of app actions
            cid: collection id of item
        '''

        self._i = cid
        self._collected_item = movie_library.get_item(cid)

        self._r = root
        self._f = ttk.Frame(self._r, padding=(0, 15))

        self._a = actions

        ttk.Label(self._f, text=self._collected_item[0], font=font.Font(weight='bold')).pack()

        ttk.Label(
            self._f, text=f'kuvaus: {self._collected_item[1]}', padding=(0, 15), wraplength=450
        ).pack()

        ttk.Label(self._f, text='oma arviosi 1-5 (nolla == ei arviota)').pack()
        rating = ttk.Entry(self._f)
        rating.insert(0, self._collected_item[2])
        rating.pack()
        rate = ttk.Button(
            self._f,
            text='tallenna arvio',
            padding=(5, 0),
            command=lambda: self._rate(rating.get())
        )
        rate.pack(pady=5)

        ttk.Label(self._f, text=f'keskiarvo: {self._collected_item[3]}', padding=(0, 15)).pack()

        ttk.Label(
            self._f, text=f'muut, joilla on sama elokuva: {self._collected_item[4]}',
            padding=(0, 15)
        ).pack()

        back = ttk.Button(
            self._f,
            text='palaa takaisin',
            padding=(5, 0),
            command=self._to_user
        )
        back.pack(pady=5)

        self._f.pack()

    def _to_user(self):
        '''go back to user view'''

        self._f.destroy()
        self._a['user']()

    def _rate(self, rating):
        '''set item rating

        Args:
            rating: rating to be set
        '''

        if movie_library.rate_item(self._i, rating):
            messagebox.showinfo(message='arvio tallennettu')
            self._f.destroy()
            self._a['item'](self._i)
        else:
            messagebox.showerror(message='arviota ei voitu tallentaa, tarkista arvo!!!')
