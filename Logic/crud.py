from Domain.rezevare import creaza_rezervare, get_id


def adaug_rezervare(lst_rezervari,
                    id_rezervare:int,nume,clasa,pret,checkin_facut):
    """
    Adauga o rezervare la lista cu rezervari
    :param lst_rezervari: Lista cu rezervari
    :param id_rezervare: id-ul rezervarii care trebuie adaugata
    :param nume: Numele persoanei care a facut rezervarea
    :param clasa: clasa rezervarii ce trebuie adaugata
    :param pret: pretul rezervarii adaugarte
    :param checkin_facut: daca sa facut checkinul rezervarii
    :return: lista cu rezervarii
    """

    rezervare=creaza_rezervare(id_rezervare,nume,clasa,pret,checkin_facut)
    return lst_rezervari+[rezervare]


def citeste_rezervare(lst_rezervari, id_rezervare):
    """
    Cauta in lista de rezerbari, rezervarea cu id-ul dat
    :param lst_rezervari: lista cu rezervari
    :param id_rezervare: id-ul rezervarii ce trebuie cautate
    :return: Rezervarea cu id-ul dat sau lista cu rezervari daca aceasta nu exista
    """
    rezervare_cu_id=None
    for rezervare in lst_rezervari:
        if get_id(rezervare)==id_rezervare:
            rezervare_cu_id=rezervare
    if rezervare_cu_id:
        return rezervare_cu_id
    return lst_rezervari


def modifica_rezervare(lst_rezervari, new_rezervare):
    """

    :param lst_rezervari:
    :param new_rezervare:
    :return:
    """
    new_lst_rezervari=[]
    for rezervare in lst_rezervari:
        if get_id(rezervare) != get_id(new_rezervare):
            new_lst_rezervari.append(rezervare)
        else:new_lst_rezervari.append(new_rezervare)
    return new_lst_rezervari


def sterge_rezervare(lst_rezervari,id_rezervare):
    """

    :param lst_rezervari:
    :param id_rezervare:
    :return:
    """
    new_lst_rezervari=[]
    for rezervare in lst_rezervari:
        if get_id(rezervare)!=id_rezervare:
            new_lst_rezervari.append(rezervare)
    return new_lst_rezervari


