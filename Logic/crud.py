from Domain.rezevare import creaza_rezervare, get_id, get_clasa, get_checkin


def adaug_rezervare(lst_rezervari,
                    id_rezervare: int, nume, clasa, pret, checkin_facut):
    """
    Adauga o rezervare la lista cu rezervari
    :param lst_rezervari: Lista cu rezervari
    :param id_rezervare: id-ul rezervarii care trebuie adaugata
    :param nume: Numele persoanei care a facut rezervarea
    :param clasa: clasa rezervarii ce trebuie adaugata
    :param pret: pretul rezervarii adaugarte
    :param checkin_facut: daca sa facut checkinul rezervarii
    :return: lista cu rezervari la care s-a adaugat o rezervare
    """

    if citeste_rezervare(lst_rezervari, id_rezervare) is not None:
        raise ValueError(f'Exista deja o rezervare cu id-ul {id_rezervare}')
    if (clasa != "economy") & (clasa != "economy plus") & (clasa != "business"):
        raise ValueError(f'Clasa poate fi doar:"economy","economy plus" sau "business"')
    if (checkin_facut != "da") & (checkin_facut != "nu"):
        raise ValueError(f'Statusul de checkin poate fi doar :"da" sau "nu"')
    rezervare = creaza_rezervare(id_rezervare, nume, clasa, pret, checkin_facut)
    return lst_rezervari + [rezervare]


def citeste_rezervare(lst_rezervari, id_rezervare: int = None):
    """
    Cauta in lista de rezervari, rezervarea cu id-ul dat si o returneaza
    :param lst_rezervari: lista cu rezervari
    :param id_rezervare: id-ul rezervarii ce trebuie cautate
    :return:
        -Rezervarea cu id-ul dat, dace exista
        -lista cu rezervari daca id_rezervare=None
        -None dace nu exista o rezervare cu id_rezervare
    """
    if not id_rezervare:
        return lst_rezervari

    rezervare_cu_id = None
    for rezervare in lst_rezervari:
        if get_id(rezervare) == id_rezervare:
            rezervare_cu_id = rezervare
    if rezervare_cu_id:
        return rezervare_cu_id
    return None


def modifica_rezervare(lst_rezervari, new_rezervare):
    """
    Cauta in lista cu rezervari, dupa id, rezervarea care trebuie modificata
    si o inlocuieste cu noua rezervare cu datele modificate
    :param lst_rezervari: lista cu rezervari
    :param new_rezervare: o rezervare a carei id este deja in lista
    :return: o noua lista cu noua rezervare sau vhechea lista
    """
    if citeste_rezervare(lst_rezervari, get_id(new_rezervare)) is None:
        raise ValueError(f'Nu exista o rezervare cu id-ul {get_id(new_rezervare)} care sa fie modificata')
    if (get_clasa(new_rezervare) != "economy") & (get_clasa(new_rezervare) != "economy plus") & (get_clasa(new_rezervare) != "business"):
        raise ValueError(f'Clasa poate fi doar:"economy","economy plus" sau "business"')
    if (get_checkin(new_rezervare) != "da") & (get_checkin(new_rezervare) != "nu"):
        raise ValueError(f'Statusul de checkin poate fi doar :"da" sau "nu"')
    new_lst_rezervari = []
    for rezervare in lst_rezervari:
        if get_id(rezervare) != get_id(new_rezervare):
            new_lst_rezervari.append(rezervare)
        else:
            new_lst_rezervari.append(new_rezervare)
    return new_lst_rezervari


def sterge_rezervare(lst_rezervari, id_rezervare: int):
    """
    Returneaza o noua lista fara rezervarea cu id-ul dat ca parametru
    :param lst_rezervari: lista cu rezervari
    :param id_rezervare: id-ul rezervarii care trebuie sterse
    :return: o noua lista fara rezervarea cu id-ul dat
    """
    if citeste_rezervare(lst_rezervari, id_rezervare) is None:
        raise ValueError(f'Nu exista o rezervare cu id-ul {id_rezervare} care sa fie stearsa')

    new_lst_rezervari = []
    for rezervare in lst_rezervari:
        if get_id(rezervare) != id_rezervare:
            new_lst_rezervari.append(rezervare)
    return new_lst_rezervari
