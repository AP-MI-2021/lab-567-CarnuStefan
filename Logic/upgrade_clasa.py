from Domain.rezevare import get_nume, get_clasa, creeaza_rezervare, get_id, get_pret, get_checkin


def upgrade_clasa(lst_rezervari, nume,lst_undo: list = None, lst_redo: list = None):
    """
    Upgradeaza clasa rezervarii (economy -> economy plus -> business) pentru toate rezervarile facute pe un anumit nume
    :param lst_redo: Resetam lista de redo
    :param lst_undo: Salveaza lista inainte de upgrade pentru a putea face undo
    :param lst_rezervari: lista cu rezervari
    :param nume: Numele pentru care trebuie facute upgrade-uri
    :return:
        -O noua lista cu rezervarile  modificate (economy -> economy plus -> business)
        -O noua lista identica cu lista primita: -daca nu exista rezervari pe numele dat
                                                 -daca toate rezervarile de pe numele dat sunt clasa "business"
    """
    new_lst_rezervari = []
    if (lst_undo is not None) & (lst_redo is not None):
        lst_undo.append(lst_rezervari)
        lst_redo.clear()

    for rezervare in lst_rezervari:
        if get_nume(rezervare) != nume:
            new_lst_rezervari.append(rezervare)
        elif get_clasa(rezervare) == 'business':
            new_lst_rezervari.append(rezervare)
        elif get_clasa(rezervare) == 'economy':
            newrezervare = creeaza_rezervare(get_id(rezervare), get_nume(rezervare), 'economy plus',
                                             get_pret(rezervare), get_checkin(rezervare))
            new_lst_rezervari.append(newrezervare)
        elif get_clasa(rezervare) == 'economy plus':
            newrezervare = creeaza_rezervare(get_id(rezervare), get_nume(rezervare), 'business',
                                             get_pret(rezervare), get_checkin(rezervare))
            new_lst_rezervari.append(newrezervare)
    return new_lst_rezervari
