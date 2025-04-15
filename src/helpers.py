from re import search

def id_from_list_item(item):
    return search(r'\[([^\[]*)\]$', item).group(1)
