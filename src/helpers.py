from re import search

def id_from_list_item(item):
    '''extracts id from a single formatted list item

    Args:
        item: formatted list item, in string format

    Returns:
        id as string
    '''

    return search(r'\[([^\[]*)\]$', item).group(1)
