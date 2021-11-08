from Domain.rezevare import get_pret


def find_price(rezervare):
    """
    Primeste o rezervare si returneaza pretul acesteia
    :param rezervare: rezervare
    :return: pretul rezervarii
    """
    return get_pret(rezervare)


def ord_price(lst_rezervari, lst_undo: list = None, lst_redo: list = None):
    """
    Ordoneaza lista in functie de pret
    :param lst_redo: Resetam lista de redo
    :param lst_undo: Salveaza lista inainte de ordonare pentru a putea face undo
    :param lst_rezervari: lista cu rezervari
    :return: lista ordonata
    """
    if (lst_undo is not None) & (lst_redo is not None):
        lst_undo.append(lst_rezervari)
        lst_redo.clear()
    return sorted(lst_rezervari, key=find_price)
