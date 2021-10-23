def creaza_rezervare(id_rezervare:int,nume,clasa,pret,checkin_facut):
    """
    Creaza o rezervare
    :param id_rezervare: Identificator numeric pentru rezervare,Unic<trebuie sa fie int
    :param nume: Numele celui care a facut rezervarea
    :param clasa: Tipul de rezervare
    :param pret: Pretul rezervarii
    :param checkin_facut: Daca sa facut check-in sau nu
    :return: o rezervare
    """
    return{
        'id': id_rezervare,
        'nume': nume,
        'clasa': clasa,
        'pret': pret,
        'checkin_facut': checkin_facut,
    }


def get_id(rezervare):
    """
    Getter pentru id-ul unei rezervarii
    :param rezervare:
    :return: id-ul unei rezervarii
    """
    return rezervare['id']


def get_nume(rezervare):
    """
    Getter pentru numele unei rezervarii
    :param rezervare:
    :return: numele unei rezervari
    """
    return rezervare['nume']


def get_clasa(rezervare):
    """
    Getter pentru clasa unei rezervarii
    :param rezervare:
    :return: lasa unei rezervari
    """
    return rezervare['clasa']


def get_pret(rezervare):
    """
    Getter pentru pretul unei rezervarii
    :param rezervare:
    :return: pretul unei rezervari
    """
    return rezervare['pret']


def get_checkin(rezervare):
    """
    Getter pentru checkin-ul unei rezervarii
    :param rezervare:
    :return: checkin-ul unei rezrevari
    """
    return rezervare['checkin']