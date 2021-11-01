from Domain.rezevare import get_nume, get_clasa, creaza_rezervare, get_id, get_pret, get_checkin


def upgrade_clasa(lst_rezervari, nume):
    """
    Upgradeaza clasa rezervarii (economy -> economy plus -> business) pentru toate rezervarile facute pe un anumit nume
    :param lst_rezervari: lista cu rezervari
    :param nume: Numele pentru care trebuie facute upgrade-uri
    :return:
        -O noua lista cu rezervarile  modificate (economy -> economy plus -> business)
        -O noua lista identica cu lista primita: -daca nu exista rezervari pe numele dat
                                                 -daca toate rezervarile de pe numele dat sunt clasa "business"
    """
    new_lst_rezervari = []
    exceptie = 0
    for rezervare in lst_rezervari:
        if get_nume(rezervare) != nume:
            new_lst_rezervari.append(rezervare)
            exceptie = 1
        elif get_clasa(rezervare) == 'business':
            new_lst_rezervari.append(rezervare)
            exceptie = 2
        elif get_clasa(rezervare) == 'economy':
            newrezervare = creaza_rezervare(get_id(rezervare), get_nume(rezervare), 'economy plus',
                                            get_pret(rezervare), get_checkin(rezervare))
            new_lst_rezervari.append(newrezervare)
        elif get_clasa(rezervare) == 'economy plus':
            newrezervare = creaza_rezervare(get_id(rezervare), get_nume(rezervare), 'business',
                                            get_pret(rezervare), get_checkin(rezervare))
            new_lst_rezervari.append(newrezervare)
    if exceptie == 1:
        print("Upgrade invalid:\nNu exista rezervari pentru acest nume\n")
    elif exceptie == 2:
        print("Atentie:\nRezervarile de clasa business nu se pot upgrada.\nOrice alta rezervare a fost upgradata\n")
    return new_lst_rezervari
